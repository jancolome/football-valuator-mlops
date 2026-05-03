# Product Backlog — Football Valuator MLOps

**Proyecto:** Pipeline MLOps de predicción de valor de mercado de futbolistas
**Responsable:** Jan Colomé (individual)
**Fechas:** 27 abril – 6 mayo 2026

---

## Sobre el backlog

Este backlog recoge las historias de usuario del proyecto. Las he organizado por prioridad y agrupadas por épica (CRISP-DM): comprensión, datos, modelado, evaluación y despliegue.

Cada historia sigue el formato estándar:
> *"Como [rol], quiero [acción], para [beneficio]."*

La estimación es en story points (escala 1, 2, 3, 5, 8, 13).

---

## Épicas

| Épica | Historias | Sprint asignado |
|---|---|---|
| Comprensión y datos | US01 – US05 | Sprint 1 |
| Modelado y evaluación | US06 – US08 | Sprint 1 |
| Validación automatizada | US09 – US11 | Sprint 2 |
| Empaquetado y despliegue | US12 – US14 | Sprint 2 |
| Documentación | US15 – US17 | Sprint 3 |

---

## Historias de usuario

### US01 — Descargar dataset

**Como** desarrollador del modelo,
**quiero** descargar el dataset público de Transfermarkt desde Kaggle,
**para** tener una base de datos histórica de jugadores y valoraciones.

- Estimación: 2 puntos
- Sprint: 1
- Estado: ✅ Done

---

### US02 — Explorar datos

**Como** desarrollador,
**quiero** explorar los CSVs de jugadores, valoraciones y partidos,
**para** entender la estructura, calidad y limitaciones del dataset.

- Estimación: 3 puntos
- Sprint: 1
- Estado: ✅ Done
- Hallazgos clave: muchos valores faltantes en datos antiguos, inflación post-Neymar 2017

---

### US03 — Filtrar dataset

**Como** desarrollador,
**quiero** filtrar el dataset desde 2018 en adelante,
**para** trabajar solo con datos completos y con escala de precios consistente.

- Estimación: 2 puntos
- Sprint: 1
- Estado: ✅ Done
- Decisión basada en datos: probé 2012+ y 2018+, este último mejoró el R² de 0.65 a 0.69

---

### US04 — Crear ventanas temporales

**Como** desarrollador,
**quiero** generar ventanas de partidos entre cada par de valoraciones consecutivas,
**para** asociar a cada valoración las estadísticas reales del jugador en ese periodo.

- Estimación: 8 puntos
- Sprint: 1
- Estado: ✅ Done
- Innovación: multiplica los datos x10 vs. usar stats agregadas por temporada

---

### US05 — Calcular índice de inflación

**Como** desarrollador,
**quiero** calcular un índice de inflación del mercado por año,
**para** normalizar las valoraciones históricas a escala 2025.

- Estimación: 5 puntos
- Sprint: 1
- Estado: ✅ Done
- Método: mediana del top 100 de valoraciones por año

---

### US06 — Entrenar modelo baseline

**Como** desarrollador,
**quiero** entrenar un modelo Random Forest baseline,
**para** tener una primera referencia de rendimiento.

- Estimación: 3 puntos
- Sprint: 1
- Estado: ✅ Done
- Resultado: R² = 0.5416, MAE 4.17M€

---

### US07 — Iterar el modelo

**Como** desarrollador,
**quiero** probar mejoras (transformación log, Gradient Boosting),
**para** alcanzar un R² competitivo con la literatura académica.

- Estimación: 5 puntos
- Sprint: 1
- Estado: ✅ Done
- Resultado: R² log = 0.6901, MAE 3.72M€ (en línea con Müller 2017, He 2015)

---

### US08 — Persistir el modelo

**Como** desarrollador,
**quiero** guardar el modelo entrenado en disco,
**para** poder cargarlo desde tests, contenedor Docker y futuros entornos.

- Estimación: 1 punto
- Sprint: 1
- Estado: ✅ Done
- Tecnologías: joblib, models/modelo_final.pkl

---

### US09 — Tests del dataset

**Como** desarrollador,
**quiero** validar automáticamente que el dataset existe y tiene las columnas críticas,
**para** detectar problemas de datos antes de entrenar.

- Estimación: 2 puntos
- Sprint: 2
- Estado: ✅ Done
- 2 tests pytest

---

### US10 — Tests del modelo

**Como** desarrollador,
**quiero** validar automáticamente que el modelo carga y predice valores razonables,
**para** detectar regresiones tras cambios.

- Estimación: 3 puntos
- Sprint: 2
- Estado: ✅ Done
- 2 tests pytest

---

### US11 — Análisis estático del código

**Como** desarrollador,
**quiero** ejecutar flake8 sobre el código en cada cambio,
**para** mantener un estilo consistente y detectar errores sintácticos.

- Estimación: 2 puntos
- Sprint: 2
- Estado: ✅ Done
- Configuración: max-line-length=120, ignore=E501,W293,W292,E303

---

### US12 — Pipeline CI

**Como** desarrollador,
**quiero** un workflow que ejecute flake8 y pytest en cada push a main,
**para** validar automáticamente cada cambio sin intervención manual.

- Estimación: 5 puntos
- Sprint: 2
- Estado: ✅ Done
- Tecnología: GitHub Actions
- Tiempo de ejecución medio: 38s

---

### US13 — Dockerfile

**Como** desarrollador,
**quiero** empaquetar el proyecto en una imagen Docker reproducible,
**para** que cualquier usuario pueda ejecutarlo sin instalar dependencias en su sistema.

- Estimación: 3 puntos
- Sprint: 2
- Estado: ✅ Done
- Imagen base: python:3.13-slim
- Buena práctica: cacheo de capas (requirements antes que código)

---

### US14 — Trigger automático del pipeline

**Como** desarrollador,
**quiero** que el pipeline se dispare automáticamente con cualquier commit a main,
**para** garantizar validación continua independientemente del origen del cambio (terminal, web, github.dev).

- Estimación: 1 punto
- Sprint: 2
- Estado: ✅ Done

---

### US15 — Tablero Kanban

**Como** responsable del proyecto,
**quiero** un tablero Trello con las tarjetas etiquetadas por fase CRISP-DM,
**para** registrar visualmente el progreso del trabajo.

- Estimación: 2 puntos
- Sprint: 3
- Estado: ✅ Done

---

### US16 — Memoria del proyecto

**Como** responsable del proyecto,
**quiero** redactar la memoria con resumen ejecutivo, arquitectura y decisiones técnicas,
**para** entregar un documento que respalde la presentación.

- Estimación: 5 puntos
- Sprint: 3
- Estado: 🟡 In progress

---

### US17 — Presentación

**Como** responsable del proyecto,
**quiero** preparar una presentación de 15-20 minutos,
**para** defender el proyecto ante el profesor.

- Estimación: 5 puntos
- Sprint: 3
- Estado: 🟡 In progress

---

## Resumen del backlog

- Total historias: 17
- Total puntos: 57
- Completadas: 15 (52 puntos)
- En curso: 2 (10 puntos)

## Pendientes para futuras versiones

Cosas que se quedan fuera del alcance pero que añadiría en una v2:

- Integración con datos avanzados (Wyscout, FBref) para mejorar features
- Modelos especializados por posición
- API REST con FastAPI para servir predicciones
- Continuous Training programado con cron en GitHub Actions
- Monitorización con MLflow + Grafana
