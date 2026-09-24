# Portafolio de Ingeniería de Requisitos

Este repositorio reúne los principales artefactos construidos durante el curso de **Ingeniería de Requisitos**, organizados de acuerdo con los distintos casos de estudio trabajados a lo largo del semestre.

El propósito del portafolio es conservar de manera organizada la evidencia del proceso realizado, desde la identificación de necesidades y definición de requisitos hasta su modelado, validación, trazabilidad y gestión de cambios. La estructura busca que una persona que no haya participado directamente en las actividades pueda comprender el contexto de cada caso, identificar los artefactos construidos y reconocer la relación existente entre ellos.

---

## Información del portafolio

| Metadato | Valor |
|---|---|
| **ID** | PORT-README-001 |
| **Versión** | 1.0 |
| **Estado final** | Final |
| **Autor** | Mary Luna Salcedo |
| **Fecha de cierre** | Septiembre 25 de 2026 |
| **Artefactos relacionados** | Todos los artefactos contenidos y referenciados en este repositorio |

---

## Presentación del portafolio

🎥 **Video explicativo:** [Ver presentación del portafolio](PEGAR_AQUÍ_ENLACE_DEL_VIDEO)

En el video se presenta brevemente la estructura del repositorio, los casos de estudio trabajados durante el curso y los principales artefactos construidos en cada uno.

---

# Casos de estudio

## 01 — Compañía de operaciones aéreas

En este caso se trabajó el proceso desde la identificación inicial de necesidades del negocio hasta la construcción de un backlog y el posterior análisis de solicitudes de cambio.

| ID | Artefacto |
|---|---|
| **AIR-PVB-001** | Product Vision Board |
| **AIR-PB-001** | Product Backlog |
| **AIR-RFC-001** | Request for Change |
| **AIR-IMP-B1** | Diagrama de Impacto — RFC-B1 |
| **AIR-IMP-B2** | Diagrama de Impacto — RFC-B2 |

El **Product Vision Board** permitió identificar los principales usuarios del sistema, sus necesidades, las funcionalidades esperadas y el valor que el producto debía aportar al negocio.

A partir de esta información se construyó el **Product Backlog**, organizado mediante épicas e historias de usuario, incorporando elementos como prioridad, criterios de aceptación, estimación y tareas de ingeniería. El backlog fue administrado mediante Azure DevOps.

Posteriormente se trabajó el proceso de gestión de cambios mediante distintos **Request for Change (RFC)**, analizando aspectos como impacto sobre requisitos existentes, esfuerzo requerido, riesgos, criterios de aceptación y decisiones del CCB.

### Acceso al Product Backlog

🔗 [Consultar Product Backlog en Azure DevOps](https://dev.azure.com/marysalcedo/ToutCrews)

---

## 02 — Simulador de Transmisión Mecánica

Este caso se centró principalmente en la especificación formal de requisitos, el modelado del sistema y la definición de mecanismos de verificación.

| ID | Artefacto |
|---|---|
| **SIM-SRS-001** | Especificación de Requisitos de Software (SRS) |
| **SIM-UML-CU-001** | Diagrama de casos de uso |
| **SIM-UML-CL-001** | Diagrama de clases |
| **SIM-UML-SEQ-001** | Diagrama de secuencia — cambio de marcha |
| **SIM-TC-001** | Casos de prueba |

El documento **SRS** describe el alcance del Simulador de Transmisión Mecánica, sus funcionalidades, restricciones, requisitos funcionales, requisitos no funcionales y elementos de interfaz.

Como apoyo a la especificación se construyeron diferentes modelos UML. El diagrama de casos de uso permite observar las principales funciones disponibles para el usuario; el diagrama de clases representa la estructura del subsistema de transmisión mecánica; y el diagrama de secuencia representa la interacción de los elementos involucrados durante el proceso de cambio de marcha.

Los **casos de prueba** fueron definidos originalmente como parte del SRS y posteriormente se presentan también como un artefacto independiente para facilitar su consulta dentro del portafolio. Estos permiten verificar requisitos relacionados con la selección del modo de funcionamiento, el cambio de marcha, el tiempo de respuesta y la estabilidad del simulador.

---

## 03 — Dietas al Día

Este caso permitió llevar los requisitos hasta una evidencia funcional mediante la construcción y validación de un prototipo web orientado a apoyar la toma de decisiones dentro de un servicio de atención nutricional.

| ID | Artefacto |
|---|---|
| **DIA-PROT-001** | Prototipo funcional |
| **DIA-VAL-001** | Documento de validación del prototipo |
| **DIA-CODE-001** | Código fuente |
| **DIA-MAT-001** | Matriz de trazabilidad |
| **DIA-EVID-001** | Evidencias de validación |

La actividad de prototipado se concentró en la **EPC 28 — Asignación de tratamiento nutricional**, a partir de la cual se validaron funcionalidades relacionadas con el análisis del perfil clínico, la detección de incompatibilidades, la consulta de información técnica de las dietas, la prescripción y la generación de informes.

El prototipo permitió comprobar mediante evidencia funcional los criterios de aceptación definidos para la épica seleccionada.

### Acceso al prototipo

🔗 [Repositorio del prototipo en GitHub](https://github.com/marylune/prototipo_u3act2)

La **matriz de trazabilidad** incluida en este portafolio utiliza este caso debido a que permite observar con mayor claridad la relación entre requisitos, criterios de aceptación, implementación, artefactos de código y resultados de validación.

---

## 04 — Empresa de mudanzas

Este caso se incluye como un escenario complementario dentro del portafolio. Durante el curso se construyeron diferentes modelos relacionados con una empresa de mudanzas que inicialmente habían quedado almacenados junto con otros artefactos.

Para mantener correctamente el contexto y evitar atribuir estos modelos al Simulador de Transmisión Mecánica, se presentan en una carpeta independiente.

| ID | Artefacto |
|---|---|
| **MUD-UML-CU-001** | Diagrama de casos de uso |
| **MUD-ER-001** | Diagrama Entidad–Relación |
| **MUD-UML-CL-001** | Diagrama de clases |

El diagrama de casos de uso representa las principales interacciones de los usuarios con el sistema; el modelo Entidad–Relación muestra la estructura de información del caso; y el diagrama de clases permite representar los principales elementos del dominio y las relaciones existentes entre ellos.

---

# Metadatos de los artefactos

Los artefactos del repositorio se encuentran acompañados de la información necesaria para facilitar su identificación y consulta.

Los metadatos utilizados son:

| Metadato | Propósito |
|---|---|
| **ID único** | Identificar cada artefacto dentro del portafolio |
| **Versión** | Reconocer la versión almacenada |
| **Estado final** | Indicar si el artefacto se encuentra finalizado, validado o pendiente |
| **Autor o revisor** | Identificar al responsable del artefacto |
| **Fecha de cierre** | Registrar el momento de finalización |
| **Artefactos relacionados** | Mostrar las relaciones existentes con otros elementos del proyecto |

Cuando un artefacto se encuentra almacenado en una plataforma externa, como Azure DevOps o un repositorio independiente de GitHub, se incluye dentro del portafolio un archivo de referencia con sus metadatos y el enlace correspondiente.

---

# Trazabilidad

Uno de los principales objetivos de la organización del portafolio es conservar la relación entre los distintos elementos generados durante el proceso de ingeniería de requisitos.

Dependiendo del caso, esta trazabilidad puede observarse en diferentes niveles.

En la **Compañía de operaciones aéreas**, es posible seguir el proceso desde las necesidades identificadas en el Product Vision Board hasta las historias de usuario del Product Backlog y posteriormente analizar cómo una solicitud de cambio puede afectar esos requisitos.

En el **Simulador de Transmisión Mecánica**, los requisitos especificados dentro del SRS se relacionan con los modelos UML y con los casos de prueba definidos para verificar algunos de ellos.

En **Dietas al Día**, la trazabilidad alcanza también la implementación y la validación del prototipo, permitiendo representar una cadena como:

**Necesidad → requisito → criterio de aceptación → implementación → evidencia de validación**

Por esta razón, este último caso fue seleccionado para construir la matriz de trazabilidad final del curso.

---

# Lecciones aprendidas

## ¿Qué funcionó bien y debería repetirse?

Una de las prácticas que considero que funcionó mejor fue construir los artefactos de manera progresiva. Partir primero de las necesidades y del contexto del negocio ayudó a que posteriormente fuera más sencillo plantear requisitos, historias de usuario y criterios de aceptación con una intención más clara.

Esto se hizo especialmente evidente en el caso de la compañía aérea. El Product Vision Board sirvió como punto de partida para la construcción del backlog y, posteriormente, cuando fue necesario realizar análisis de impacto, ya existían requisitos e historias que podían relacionarse directamente con los cambios planteados.

También considero que fue útil trabajar con herramientas de gestión y control de versiones. Azure DevOps permitió organizar el backlog mediante épicas, Features y Requirements, mientras que GitHub permitió mantener el prototipo y su código en un entorno accesible y versionado.

Esta forma de trabajo debería repetirse porque reduce la pérdida de contexto entre etapas y facilita reconstruir posteriormente por qué existe un requisito y con qué otros artefactos se relaciona.

---

## ¿Qué falló y cómo se detectó?

Una de las dificultades se presentó durante la estimación inicial del Product Backlog. Inicialmente utilicé los puntos de historia como una medida general de complejidad, pero no había definido claramente cómo se relacionaban posteriormente con el esfuerzo necesario para realizar las tareas de ingeniería.

Esta situación se hizo evidente durante la retroalimentación del profesor, cuando fue necesario revisar las técnicas de estimación relativa y diferenciar con mayor claridad los Story Points de una estimación de esfuerzo expresada en horas.

Otro elemento que, después de revisar el trabajo completo, considero que no resultó tan efectivo fue el **diagrama de secuencia utilizado para representar el proceso de cambio de marcha del Simulador de Transmisión Mecánica**.

El diagrama es técnicamente válido y permite observar el intercambio de mensajes entre los distintos componentes del sistema; sin embargo, al verlo dentro del SRS considero que su nivel de detalle hace que el proceso sea más difícil de interpretar de lo necesario.

Esto es importante porque un SRS no debería ser comprensible únicamente para personas con conocimientos técnicos de UML. También puede ser consultado por clientes, stakeholders u otras personas involucradas en el proyecto que no necesariamente tienen formación en ingeniería de software.

En mi caso, incluso con conocimientos adquiridos durante el curso, la lectura del diagrama requiere detenerse bastante para comprender la secuencia completa. Por esta razón, considero que no fue la representación que más valor aportó para comunicar ese comportamiento específico.

Para explicar el cambio de marcha habría resultado posiblemente más apropiado un **diagrama de actividades**, ya que permitiría representar de manera más directa el flujo del proceso. Este tipo de representación permitiría conservar el comportamiento importante del proceso, pero mediante un flujo visual más fácil de seguir para personas con distintos niveles de conocimiento técnico.

La conclusión no es que los diagramas de secuencia sean innecesarios, sino que la selección del tipo de modelo debería depender también de **quién va a utilizar el documento y qué información necesita comprender**.

---

## ¿Qué haríamos diferente desde el inicio?

Si volviera a iniciar el curso, una de las primeras decisiones sería definir una convención común para los identificadores, las versiones y los metadatos de todos los artefactos.

Durante las primeras actividades cada documento se construyó principalmente pensando en la entrega específica de ese momento. Al llegar al portafolio final fue necesario revisar archivos, separar elementos que pertenecían a contextos diferentes y establecer posteriormente las relaciones entre ellos.

También habría creado el repositorio del curso desde las primeras semanas, almacenando cada artefacto desde el momento de su creación. Esto habría permitido conservar una estructura más consistente y evitar realizar gran parte del trabajo de organización al final.

Además, definiría desde el principio una cadena básica de trazabilidad como:

**Necesidad → requisito → modelo o diseño → implementación → prueba → resultado**

No todos los casos necesariamente llegan hasta la implementación, pero utilizar esta estructura como referencia permitiría identificar desde etapas tempranas dónde termina la evidencia disponible para cada requisito.

Por último, prestaría más atención desde el inicio a la selección de los modelos utilizados. No solamente evaluaría si un diagrama es técnicamente correcto, sino también si realmente facilita la comprensión del sistema para las personas que van a consultar el documento.

---

# Navegación del repositorio

| Carpeta | Contenido |
|---|---|
| `00-presentacion/` | Referencia al video explicativo del portafolio |
| `01-compania-aerea/` | Vision Board, Product Backlog, RFC y diagramas de impacto |
| `02-simulador-transmision/` | SRS, modelos UML y casos de prueba |
| `03-dietas-al-dia/` | Validación, prototipo, código y matriz de trazabilidad |
| `04-empresa-mudanzas/` | Casos de uso, modelo ER y diagrama de clases |

---

# Estado del portafolio

| Campo | Estado |
|---|---|
| **Versión** | 1.0 |
| **Estado** | Final para entrega académica |
| **Fecha de cierre** | Septiembre 25 de 2026 |