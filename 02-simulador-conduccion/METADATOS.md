# Metadatos — Simulador Vehículo de Conducción

Este archivo contiene la identificación y relación de los artefactos construidos para el caso de estudio del Simulador de Transmisión Mecánica.

## Información del caso

| Campo | Valor |
|---|---|
| **Caso de estudio** | Simulador de Transmisión Mecánica |
| **Curso** | Ingeniería de Requisitos |
| **Autor** | Mary Luna Salcedo |
| **Estado del caso** | Finalizado para entrega académica |
| **Fecha de cierre** | Septiembre de 2026 |

## Catálogo de artefactos

| ID | Artefacto | Versión | Estado final | Autor / revisor | Fecha de cierre | Artefactos relacionados |
|---|---|---:|---|---|---|---|
| **SIM-SRS-001** | Especificación de Requisitos de Software (SRS) | 1.00 | Final | Mary Luna Salcedo | 2026 | SIM-UML-CU-001, SIM-UML-CL-001, SIM-UML-SEQ-001, SIM-TC-001 |
| **SIM-UML-CU-001** | Diagrama de casos de uso | 1.0 | Final | Mary Luna Salcedo | 2026 | SIM-SRS-001 |
| **SIM-UML-CL-001** | Diagrama de clases | 1.0 | Final | Mary Luna Salcedo | 2026 | SIM-SRS-001 |
| **SIM-UML-SEQ-001** | Diagrama de secuencia - Cambio de marcha | 1.0 | Final | Mary Luna Salcedo | 2026 | SIM-SRS-001, SIM-TC-001 |
| **SIM-TC-001** | Casos de prueba | 1.0 | Final / Pendiente de ejecución | Mary Luna Salcedo | 2026 | SIM-SRS-001 |

## Archivos

### Documento principal

- `SIM-SRS-001_SRS.pdf`

### Casos de prueba

- `SIM-TC-001_CasosPrueba.docx`

### Diagramas

- `diagramas/SIM-UML-CU-001_CasosUso.pdf`
- `diagramas/SIM-UML-CL-001_Clases.png`
- `diagramas/SIM-UML-SEQ-001_Secuencia.pdf`

## Relaciones principales

El **SRS** funciona como documento principal del caso y contiene la especificación de requisitos funcionales y no funcionales del simulador.

Los modelos UML complementan la especificación:

- El **diagrama de casos de uso** representa las principales interacciones con el sistema.
- El **diagrama de clases** representa la estructura del subsistema.
- El **diagrama de secuencia** representa la interacción entre componentes durante el cambio de marcha.

Los casos de prueba fueron definidos a partir de requisitos incluidos en el SRS y se presentan también como un documento independiente para facilitar su consulta dentro del portafolio.

## Casos de prueba relacionados

| Requisito | Caso de prueba |
|---|---|
| RF-03 | TC_FUNCT_01 |
| RF-06 | TC_FUNCT_02 |
| RNF-01 | TC_NFUNCT_01 |
| RNF-02 | TC_NFUNCT_02 |

**Flujo principal de trazabilidad:**

`SRS → Requisitos → Modelos UML → Casos de prueba`

## Nota sobre los casos de prueba

Los casos de prueba fueron especificados como parte del proceso de ingeniería de requisitos. En el alcance de la actividad se definieron los procedimientos y resultados esperados, pero no se registró una ejecución completa del sistema, por lo que su estado se conserva como pendiente de ejecución.
