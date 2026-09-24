from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parent
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    page=browser.new_page(viewport={'width':1440,'height':1050})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((ROOT/'index.html').as_uri())
    page.locator('#search').click()
    assert page.locator('.card').count()==4
    assert page.locator('.blocked').count()==1
    page.screenshot(path=str(ROOT/'referencias'/'01-consulta.png'),full_page=True)
    page.locator('[data-detail="D02"]').click()
    assert 'Yogur natural contiene Leche' in page.locator('dialog').inner_text()
    assert page.get_by_role('button',name='Prescripción no permitida').is_disabled()
    page.screenshot(path=str(ROOT/'referencias'/'02-alerta.png'),full_page=True)
    page.locator('#close').click()
    page.locator('[data-detail="D01"]').click()
    assert page.locator('#prescribe').is_disabled()
    page.locator('#review').check()
    page.locator('#notes').fill('Prueba técnica automatizada; no es evidencia de usuario.')
    page.locator('#prescribe').click()
    assert page.locator('#content').get_by_text('Control glucémico sin lácteos',exact=True).count()==1
    page.locator('[data-view="informe"]').click()
    assert 'Laura Martínez' in page.locator('.report').inner_text()
    page.pdf(path=str(ROOT/'referencias'/'informe-ejemplo.pdf'),format='A4')
    page.locator('#patient').select_option('1')
    assert 'Sin prescripciones registradas' in page.locator('.report').inner_text()
    page.locator('[data-view="consulta"]').click()
    page.locator('#search').click()
    assert page.locator('.card').count()==3
    page.locator('[data-detail="D04"]').click()
    assert 'Pescado contiene Pescado' in page.locator('dialog').inner_text()
    assert 'Nueces contiene Frutos secos' in page.locator('dialog').inner_text()
    page.keyboard.press('Escape')
    page.locator('#patient').select_option('2')
    page.locator('#search').click()
    assert page.locator('.card').count()==2
    page.locator('[data-detail="D07"]').click()
    assert 'Contraindicación por diagnóstico: Celiaquía' in page.locator('dialog').inner_text()
    page.keyboard.press('Escape')
    page.locator('#patient').select_option('3')
    page.locator('#search').click()
    assert 'Falta un diagnóstico registrado' in page.locator('#content').inner_text()
    page.locator('[data-view="historia"]').click()
    page.locator('#diagnosis').select_option(label='Sin asociación en catálogo')
    page.get_by_role('button',name='Guardar perfil y consultar dietas').click()
    assert 'No hay dietas asociadas' in page.locator('#content').inner_text()
    page.locator('#patient').select_option('0')
    page.locator('[data-view="historia"]').click()
    page.locator('[name="allergy"][value="Leche"]').uncheck()
    page.get_by_role('button',name='Guardar perfil y consultar dietas').click()
    assert page.locator('.blocked').count()==0
    page.reload()
    page.locator('[data-view="historia"]').click()
    assert 'Control glucémico sin lácteos' in page.locator('#content').inner_text()
    assert page.locator('#patient option').count()==6
    assert page.locator('[data-view="validacion"]').count()==0
    for index, blocked, safe, allergy in [('4','D09','D08','Frutos secos'),('5','D12','D11','Huevo')]:
        page.locator('#patient').select_option(index)
        page.locator('[data-view="consulta"]').click()
        page.locator('#search').click()
        assert page.locator('.card').count()==3
        assert page.locator('.blocked').count()==1
        page.locator(f'[data-detail="{blocked}"]').click()
        assert allergy in page.locator('dialog').inner_text()
        assert page.get_by_role('button',name='Prescripción no permitida').is_disabled()
        page.locator('#close').click()
        page.locator(f'[data-detail="{safe}"]').click()
        page.locator('#review').check()
        page.locator('#prescribe').click()
        diagnosis=page.locator('#diagnosis').input_value()
        page.get_by_role('button',name='Guardar perfil y consultar dietas').click()
        assert page.locator('.card').count()==3
        assert page.locator('.blocked').count()==1
        for nav in ['consulta','historia','informe']:
            page.locator(f'[data-view="{nav}"]').click()
            text=page.locator('body').inner_text().lower()
            assert not any(word in text for word in ['fictici','simulad','demostración','epc 28','prototipo','épica']), text
    page.evaluate('localStorage.clear()')
    page.reload()
    page.locator('#search').click()
    page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.screenshot(path=str(ROOT/'referencias'/'03-movil.png'),full_page=True)
    assert not errors, errors
    browser.close()
print('PASS: consulta, alertas, bloqueo, prescripcion, aislamiento de pacientes, PDF, perfiles, persistencia, dos pacientes nuevos, seis dietas nuevas y movil. Sin errores JavaScript. Prueba automatizada; NO valida usabilidad humana.')
