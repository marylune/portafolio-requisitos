# Metadatos — Dietas al Día

Este archivo contiene la identificación y relación de los artefactos construidos para el caso de estudio de la aplicación nutricional Dietas al Día.

## Información del caso

| Campo | Valor |
|---|---|
| **Caso de estudio** | Dietas al Día |
| **Curso** | Ingeniería de Requisitos |
| **Autor** | Mary Luna Salcedo |
| **Estado del caso** | Validado mediante prototipo |
| **Fecha de cierre** | Septiembre de 2026 |

## Catálogo de artefactos

| ID | Artefacto | Versión | Estado final | Autor / revisor | Fecha de cierre | Artefactos relacionados |
|---|---|---:|---|---|---|---|
| **DIA-PROT-001** | Prototipo funcional EPC 28 | 1.0 | Validado | Mary Luna Salcedo | 19/09/2026 | DIA-VAL-001, DIA-MAT-001 |
| **DIA-VAL-001** | Documento de validación del prototipo | 1.0 | Final | Mary Luna Salcedo | 19/09/2026 | DIA-PROT-001, DIA-MAT-001 |
| **DIA-MAT-001** | Matriz de trazabilidad | 1.0 | Final | Mary Luna Salcedo | 23/09/2026 | DIA-PROT-001, DIA-VAL-001 |
| **DIA-PROT-REF-001** | Referencia al repositorio del prototipo | 1.0 | Activa | Mary Luna Salcedo | 23/09/2026 | DIA-PROT-001 |

## Archivos

- `DIA-MAT-001_MatrizTrazabilidad.xlsx`
- `DIA-VAL-001_ValidacionPrototipo.docx`
- `DIA-PROT-001_RepositorioPrototipo.md`

### Prototipo funcional

La carpeta:

`DIA-PROT-001_PrototipoEP28/`

contiene los archivos correspondientes al prototipo funcional desarrollado para validar la EPC 28.

## Requisito principal validado

**EPC 28 - Asignación de tratamiento nutricional**

El prototipo fue construido con el propósito de comprobar que el médico pudiera:

- consultar dietas relacionadas con el diagnóstico del paciente;
- identificar incompatibilidades y alergias antes de seleccionar un tratamiento;
- acceder a la ficha técnica de la dieta sin perder el contexto del paciente;
- completar la selección de una alternativa segura dentro del tiempo establecido.

La validación concluyó que EPC 28 cumplió satisfactoriamente los criterios de aceptación definidos.

## Features relacionadas

| ID Azure DevOps | Feature |
|---|---|
| **29** | Análisis del perfil clínico del paciente |
| **30** | Detección automática de la idoneidad clínica de una dieta |
| **31** | Prescripción directa de la dieta en la historia clínica |
| **32** | Generación de informe clínico para impresión o PDF |

## Relaciones principales

El documento de validación define el requisito seleccionado, las Features y los criterios de aceptación utilizados durante la prueba.

El prototipo constituye la evidencia funcional de la implementación, mientras que la matriz permite relacionar estos elementos con los artefactos técnicos y los resultados obtenidos.

**Flujo principal de trazabilidad:**

`EPC 28 → Features → Criterios de aceptación → Prototipo → Evidencias → Matriz de trazabilidad`

## Artefacto externo

El prototipo también se encuentra disponible en un repositorio independiente de GitHub:

https://github.com/marylune/prototipo_u3act2

El archivo `DIA-PROT-001_RepositorioPrototipo.md` funciona como referencia al artefacto externo.