# Dietas al Día

## Abrir

Haz doble clic en **index.html**. Funciona localmente en Chrome o Edge sin instalar nada y sin conexión a Internet. Mantén index.html, styles.css, data.js y app.js juntos.

## Recorrido sugerido

1. Con Laura seleccionada, pulsa **Consultar dietas**.
2. Abre **Control glucémico tradicional**: muestra 100 %, pero está bloqueada por yogur con leche.
3. Cierra la ficha y abre **Control glucémico sin lácteos**.
4. Revisa la ficha, marca la casilla y confirma la prescripción simulada.
5. En Historia clínica, abre **Ver informe** y pulsa **Imprimir / Guardar PDF**.
6. Prueba Carlos (múltiples alergias), Ana (gluten y contraindicación) y Diego (sin diagnóstico).
7. Prueba Valentina (dislipidemia y alergia a frutos secos) y Andrés (anemia ferropénica y alergia al huevo), con tres dietas adicionales para cada uno. La prueba CA4 se realiza con cronómetro y registro externo.

## Entrega

- **ENTREGA.md**: objetivo, requisitos priorizados, criterios de aceptación, pruebas, checklist IEEE adaptado y propuesta RFC-001.
- **referencias/**: capturas de escritorio, alerta y móvil; informe PDF de ejemplo; imágenes de la rúbrica.
- **verificar.py**: prueba automática reproducible (requiere Python, Playwright y Chrome). Ejecutar `python verificar.py`.

Se comprobó el flujo en Chrome. CA4 requiere una prueba humana real; los resultados automatizados no la sustituyen.

## Datos

Todos los pacientes y reglas son ficticios. Las ediciones del perfil duran la sesión; los registros y las pruebas se conservan en el navegador cuando este permite almacenamiento local. No se transmiten datos a servicios externos. Para presentar en otro equipo, copia la carpeta completa; los registros del navegador no viajan con ella.
