> Actualización: la interfaz ahora contiene seis pacientes y trece dietas. Se retiraron la sección de validación académica y sus controles de medición y exportación. Las referencias a la instrumentación CA4 en este documento corresponden a la versión inicial; la prueba actual requiere cronómetro y registro externo. Los avisos académicos quedan fuera de las pantallas del producto.

# Dietas al Día — Entrega de prototipado

**Curso:** Ingeniería de Requisitos · UPB  
**Actividad:** U3A2 · Prototipado: análisis de caso  
**Épica:** EPC 28 · Asignación tratamiento nutricional  
**Autor/a:** completar antes de entregar  
**Versión:** 1.0 · 14 de septiembre de 2026

## 1. Objetivo

Validar mediante un prototipo web de alta fidelidad que un médico puede consultar dietas asociadas al diagnóstico de un paciente, detectar alimentos incompatibles con sus alergias registradas y seleccionar un tratamiento conservando el contexto clínico.

La interfaz incluye navegación, formularios, datos ficticios, cálculo de coincidencia, alertas, ficha técnica, confirmación, historia e informe. Funciona localmente, sin servidor ni conexión a una historia clínica real.

## 2. Fuentes y decisiones de alcance

- `Tarea_Prototipado.pdf`, página 1: caso Dietas al Día, EPC 28, procedimiento y CA1–CA4.
- `rubrica_tarea_prototipado.pdf`, páginas 1–2: funcionalidad (2), validación (1,5) y aceptación (1,5), total 5.
- Solicitud del estudiante: cuatro features, ranking porcentual, análisis de perfil, informe y prescripción directa simulada.
- Decisiones propuestas por esta implementación: fórmula 70/30, bloqueo obligatorio, almacenamiento local y protocolo instrumentado. No se atribuyen estas decisiones a los PDF.
- Se interpreta RFC como solicitud de cambio de requisitos. Los PDF no definen un formato ni un flujo de RFC; RFC-001 es una propuesta documental para revisión en clase, no una aprobación del profesor.

La escala global de niveles que aparece al final de la rúbrica utiliza umbrales de 19, 14 y 9, aunque la suma de los criterios es 5. Se conserva el total explícito de 5 y no se inventa una conversión entre escalas.

## 3. Épica de origen

Como médico del Departamento de Nutrición quiero consultar las dietas compatibles con el diagnóstico de un paciente, señalando explícitamente si alguna dieta contiene alimentos incompatibles con sus alergias registradas, para elegir con seguridad un tratamiento sin cruzar manualmente la historia clínica con el catálogo de dietas.

## 4. Requisitos priorizados y trazabilidad

P0 = indispensable para demostrar la épica. P1 = feature solicitado que complementa el flujo.

| ID | Prioridad | Requisito verificable | Feature / origen | Evidencia |
|---|---|---|---|---|
| RF01 | P0 | Con un paciente activo y diagnóstico registrado, mostrar las dietas asociadas al pulsar Consultar dietas una vez. | F1, F4; CA1 | Laura: cuatro dietas |
| RF02 | P0 | Cruzar las etiquetas de ingredientes con alergias e incompatibilidades e indicar alimento y conflicto. | F1, F4; CA2 | Yogur natural → Leche |
| RF03 | P0 | Bloquear la confirmación si existe alergia, incompatibilidad o contraindicación registrada, incluso con 100 %. | F1, F4; propuesta RFC | D02 y D07 no prescribibles |
| RF04 | P0 | Abrir una ficha con objetivos, definición, kcal, componentes, ingesta, vía, duración, dosificación, pauta y suplementos, conservando el paciente. | CA3 | Diálogo Ver ficha |
| RF05 | P0 | Mostrar coincidencia porcentual explicada por diagnóstico y energía, ordenando primero las dietas sin conflictos. | F1 | Tarjetas y desglose |
| RF06 | P1 | Consultar y modificar diagnóstico, alergias, incompatibilidad, peso, talla y requerimiento, recalculando resultados. | F2 | Historia clínica |
| RF07 | P1 | Confirmar una dieta sin conflictos tras reconocer la revisión y registrar paciente, fecha, dieta, notas y perfil del momento. | F4 | Historial local por paciente |
| RF08 | P1 | Generar un informe individual con perfil y prescripciones para imprimir o guardar como PDF. | F3 | Informe del paciente |
| RF09 | P0 | Mostrar un estado explícito y no permitir seleccionar tratamiento cuando falta diagnóstico o no hay asociaciones. | Completitud; RFC | Diego y diagnóstico sin catálogo |
| RNF01 | P0 | Un usuario nuevo completa una elección sin conflictos en menos de 90 segundos, sin ayuda y sin omitir alertas. | CA4 | Prueba humana pendiente |

El motor admite varios diagnósticos; la edición de esta versión expone solo un diagnóstico principal. No se simula la administración completa de nutrientes, vitaminas, minerales ni del catálogo de enfermedades: el alcance es EPC 28.

## 5. Reglas de simulación

1. Seleccionar dietas que tengan al menos una indicación coincidente con los diagnósticos registrados.
2. Calcular `70 × (diagnósticos cubiertos / diagnósticos registrados)`.
3. Calcular `30 × max(0, 1 − abs(kcal dieta − kcal paciente) / kcal paciente)`.
4. Redondear la suma. La cifra expresa coincidencia de reglas, no probabilidad de éxito ni validación médica.
5. Comparar cada etiqueta de alérgeno del ingrediente contra alergias e incompatibilidades del paciente; agregar las contraindicaciones por diagnóstico.
6. Ordenar primero sin conflictos y luego por mayor porcentaje. Las dietas bloqueadas siguen visibles para demostrar las alertas.
7. Verificar otra vez los conflictos al confirmar. La confirmación requiere marcar la revisión de la ficha.

Ejemplo: Laura necesita 1800 kcal y tiene diabetes tipo 2 y alergia a leche. D01 obtiene 100 % sin conflictos. D02 también obtiene 100 %, pero queda bloqueada por yogur con leche. D03 obtiene 97 %. Estos resultados son fixtures de prueba, no recomendaciones nutricionales.

Los alérgenos se limitan a las etiquetas del catálogo ficticio. No se evalúan contaminación cruzada, interacciones farmacológicas, laboratorio ni severidad de enfermedades. La dosificación es un campo de ejemplo pendiente de individualización; no se calculan gramos ni se produce una prescripción real.

## 6. Demostración y criterios de aceptación

| Prueba | Pasos | Resultado esperado | Estado técnico |
|---|---|---|---|
| T01 / CA1 | Laura → Consultar dietas | Cuatro tarjetas con una consulta desde paciente activo | Pasó |
| T02 / CA2 | Laura → D02 → Ver ficha | Identifica yogur/leche; confirmación deshabilitada | Pasó |
| T03 / CA3 | Laura → D01 → Ver ficha | Mantiene nombre, diagnóstico, alergias y kcal; muestra campos técnicos | Pasó; inspección de interfaz |
| T04 / RF07 | D01 → marcar revisión → confirmar | Registro en historia de Laura | Pasó |
| T05 / aislamiento | Cambiar a Carlos → Informe | No muestra las prescripciones de Laura | Pasó |
| T06 / múltiples alergias | Carlos → D04 | Alertas de pescado y frutos secos | Pasó |
| T07 / contraindicación | Ana → D07 | Gluten y contraindicación por celiaquía; bloqueo | Pasó |
| T08 / datos faltantes | Diego → Consultar | Mensaje de diagnóstico faltante | Pasó |
| T09 / vacío | Editar diagnóstico a Sin asociación en catálogo | Sin dietas asociadas | Pasó |
| T10 / actualización | Quitar alergia a leche de Laura y guardar | Recalcula; desaparece bloqueo de D02 | Pasó |
| T11 / persistencia | Prescribir, recargar y abrir historia | Conserva registro del mismo paciente | Pasó |
| T12 / informe | Abrir informe → imprimir/guardar PDF | Informe individual imprimible; PDF generado en prueba | Pasó |
| T13 / CA4 instrumental | Iniciar, abrir alerta, confirmar, evaluar y exportar | Registra tiempo y evaluación; 90 segundos exactos no cumplen | Pasó técnicamente |
| T14 / móvil | Abrir a 390 px | Sin desbordamiento horizontal | Pasó |
| T15 / CA4 humano | Usuario nuevo ejecuta el protocolo siguiente | Menos de 90 s, sin ayuda, sin alertas omitidas | Pendiente |

Ejecución automática: `python verificar.py`, Chrome sin interfaz visible, sin errores JavaScript. Además se verificaron con Node ocho aserciones del motor: porcentajes, bloqueo con 100 %, múltiples conflictos, ausencia de diagnóstico y cobertura parcial. Las comprobaciones automáticas no demuestran aceptación humana ni certifican seguridad clínica.

Capturas: `referencias/01-consulta.png`, `02-alerta.png`, `03-movil.png`. Informe generado: `referencias/informe-ejemplo.pdf`. El PDF contiene una nota que identifica su origen automatizado.

## 7. Protocolo con usuarios sin ayuda

**Participantes:** idealmente tres personas que no hayan visto el prototipo; registrar cada resultado individual. El mínimo de muestra no está fijado por los PDF. No reutilizar a un participante como usuario nuevo después de enseñarle el flujo.

**Preparación:** abrir Validación académica, asignar código anónimo y explicar únicamente esta tarea: «Consulta las dietas de Laura, identifica cualquier alerta y registra una dieta que no tenga conflictos con sus datos clínicos». No indicar botones ni la dieta correcta.

**Inicio:** participante pulsa Iniciar prueba con Laura. La aplicación restablece diagnóstico, alergias, incompatibilidades y kcal del caso. El reloj corre desde ese clic hasta la confirmación.

**Observación:** anotar solicitudes de ayuda, errores de navegación, alertas ignoradas y comentario final del participante sobre el conflicto detectado. El protocolo utiliza abrir la ficha de cada dieta bloqueada como evidencia operativa de revisión. Abrirla por sí solo no demuestra comprensión; el observador debe verificarla.

**Cierre:** entrar a Validación académica y completar la evaluación del observador. Exportar JSON. Una prueba cumple si tarda estrictamente menos de 90 segundos, revisó las fichas con alertas y el observador confirma usuario nuevo, ausencia de ayuda e identificación de todas las alertas.

Cambiar de paciente o editar el perfil cancela la medición; documentar la cancelación como incidencia. Un abandono no genera prescripción ni resultado automático: registrarlo en la tabla de campo.

| Código | Nuevo | Tiempo | Ayuda | Alertas identificadas | Errores / abandono | Resultado |
|---|---|---|---|---|---|---|
| Por completar | | | | | | |
| Por completar | | | | | | |
| Por completar | | | | | | |

## 8. Lista de verificación basada en criterios IEEE

Adaptación académica de las características de requisitos de IEEE 830-1998; no es una certificación de conformidad ni una afirmación de vigencia de esa edición. Referencia: [IEEE Recommended Practice for Software Requirements Specifications, copia del documento IEEE](https://www.math.uaa.alaska.edu/~afkjm/cs401/IEEE830.pdf). Se utiliza para revisar claridad, consistencia y verificabilidad, no para validar nutrición.

| Criterio | Pregunta aplicada | Evaluación y evidencia |
|---|---|---|
| Corrección | ¿Responde a la necesidad del médico? | Parcial: flujo alineado con EPC 28; falta validación del interesado |
| Ausencia de ambigüedad | ¿Compatibilidad, porcentaje y un paso tienen una interpretación definida? | Precisados en RF01 y reglas; aceptar estas definiciones mediante RFC |
| Completitud | ¿Incluye entradas, salidas y excepciones dentro del alcance? | Sí para escenarios simulados; falta definición clínica exhaustiva para producción |
| Consistencia | ¿El ranking contradice las alertas? | No: el bloqueo tiene prioridad sobre cualquier porcentaje |
| Priorización | ¿Se distinguen requisitos indispensables y complementarios? | Sí: P0/P1 en matriz |
| Verificabilidad | ¿Cada requisito tiene una prueba observable? | Sí: T01–T15; prueba humana pendiente |
| Modificabilidad | ¿Cambiar un requisito o regla es localizable? | Sí: IDs, catálogo separado en data.js y fórmula central evaluate |
| Trazabilidad | ¿Puede seguirse origen → requisito → pantalla → prueba? | Sí: matrices de secciones 4 y 6 |

## 9. RFC-001 — Precisar criterios de asignación

**Estado:** propuesto, pendiente de revisión del docente/interesado.  
**Origen:** EPC 28 y features solicitados.  
**Motivo:** «idoneidad porcentual», «segura» y «un paso» no especifican fórmula, precedencia de alertas ni precondiciones. CA4 necesita una medición reproducible.

**Cambio propuesto:** con un paciente activo y diagnóstico registrado, recuperar dietas asociadas en una acción; explicar el puntaje; señalar alimento y conflicto; impedir la confirmación ante conflicto registrado; conservar contexto al consultar fichas; confirmar con revisión explícita; registrar tratamiento y perfil del momento; habilitar informe individual. El porcentaje no garantiza seguridad clínica.

**Impacto:** interfaz de tarjetas y ficha, esquema de etiquetas de alimentos, motor de cruce, validación de confirmación, historial y pruebas de aceptación. F2 y F3 complementan el flujo sin sustituir CA1–CA4.

**Alternativa a revisar:** permitir excepción clínica con justificación y auditoría. No se implementa porque no fue definida por el caso; el prototipo adopta bloqueo obligatorio para evaluar la propuesta.

**Flujo documental:** solicitud → análisis de impacto → prototipo → verificación técnica → prueba con usuario → decisión del interesado. Esta entrega alcanza la verificación técnica; no suplanta los pasos pendientes.

**Decisión actual:** reformular los aspectos ambiguos mediante este RFC y mantener la validación final pendiente. La épica es demostrable en el prototipo, pero no se declara totalmente validada antes de CA4 y la revisión de las reglas.

**Cierre futuro:** adjuntar evidencias de usuarios, documentar problemas, corregir y repetir con nuevos participantes cuando corresponda. Registrar nombre/rol del aprobador, fecha y versión aprobada.

## 10. Correspondencia con la rúbrica

| Criterio | Evidencia entregada | Pendiente |
|---|---|---|
| Funcionalidad / 2 | Objetivo, requisitos priorizados, diseño viable con HTML/CSS/JS y flujo completo | Evaluación del docente |
| Validación / 1,5 | Demostración de requisitos prioritarios, pruebas automáticas sin errores en escenarios cubiertos | Validación del interesado |
| Aceptación / 1,5 | Navegación coherente, jerarquía visual, etiquetas, foco de teclado, diseño móvil y protocolo sin ayuda | Ejecutar pruebas humanas |

No se asigna una nota estimada: la calificación corresponde al docente.

## 11. Límites y viabilidad

Arquitectura: interfaz → motor evaluate → catálogo local; prescripción → almacenamiento del navegador; informe → impresión nativa. El prototipo abre sin instalar dependencias. Los perfiles editados se restablecen al recargar; prescripciones y pruebas se guardan en localStorage, si el navegador lo permite. Cada registro conserva su perfil histórico.

No incluye autenticación, servidor, interoperabilidad ni validación por nutricionista. Para producción se requerirían catálogo revisado, manejo de información clínica incompleta, permisos, auditoría, seguridad y pruebas del motor. Estos límites no impiden demostrar el alcance académico.
