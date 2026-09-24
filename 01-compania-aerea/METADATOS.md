# Metadatos — Compañía de operaciones aéreas

Este archivo contiene la identificación y relación de los artefactos construidos para el caso de estudio de la compañía de operaciones aéreas.

## Información del caso

| Campo | Valor |
|---|---|
| **Caso de estudio** | Compañía de operaciones aéreas |
| **Curso** | Ingeniería de Requisitos |
| **Autor** | Mary Luna Salcedo |
| **Estado del caso** | Finalizado para entrega académica |
| **Fecha de cierre** | Septiembre de 2026 |

## Catálogo de artefactos

| ID | Artefacto | Versión | Estado final | Autor / revisor | Fecha de cierre | Artefactos relacionados |
|---|---|---:|---|---|---|---|
| **AIR-PVB-001** | Product Vision Board | 1.0 | Final | Mary Luna Salcedo | 2026 | AIR-PB-001 |
| **AIR-PB-001** | Product Backlog | 1.0 | Final | Mary Luna Salcedo | 2026 | AIR-PVB-001, AIR-RFC-001 |
| **AIR-RFC-001** | Control de cambios / Request for Change | 1.0 | Final | Mary Luna Salcedo | 2026 | AIR-PB-001, AIR-IMP-B1, AIR-IMP-B2 |
| **AIR-IMP-B1** | Diagrama de Impacto — RFC-B1: Nuevo criterio de puntuación | 1.0 | Final | Mary Luna Salcedo | 2026 | AIR-RFC-001 |
| **AIR-IMP-B2** | Diagrama de Impacto — RFC-B2: Factor ponderador de vuelo real | 1.0 | Final | Mary Luna Salcedo | 2026 | AIR-RFC-001 |

## Archivos

- `AIR-PVB-001_VisionBoard.docx`
- `AIR-PB-001_ProductBacklog.md`
- `AIR-RFC-001_ControlCambios.docx`
- `AIR-IMP-B1_DiagramaImpacto.jpg`
- `AIR-IMP-B2_DiagramaImpacto.jpg`

## Relaciones principales

La trazabilidad de este caso parte de las necesidades identificadas en el **Product Vision Board**, las cuales sirvieron como base para la construcción del **Product Backlog**.

Posteriormente, los requisitos definidos en el backlog fueron utilizados durante el análisis de solicitudes de cambio. Las RFC-B1 y RFC-B2 cuentan además con diagramas de impacto que permiten observar los requisitos y artefactos afectados por los cambios propuestos.

**Flujo principal de trazabilidad:**

`Vision Board → Product Backlog → Request for Change → Diagramas de Impacto`

## Artefactos externos

El Product Backlog original se encuentra gestionado mediante Azure DevOps. El archivo `AIR-PB-001_ProductBacklog.md` contiene la referencia y el enlace al artefacto externo.