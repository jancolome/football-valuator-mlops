# Sprint 1 — Datos y modelo

**Fechas:** 27 abril – 29 abril 2026
**Duración:** 3 días
**Objetivo:** Tener un dataset preparado y un modelo entrenado con métricas competitivas.

---

## Sprint Goal

> *"Al final del sprint, tengo el dataset filtrado y limpio, y un modelo entrenado que supera el R² de los baselines académicos con datos públicos."*

---

## Sprint Backlog

| ID | Historia | Puntos | Estado |
|---|---|---|---|
| US01 | Descargar dataset | 2 | ✅ Done |
| US02 | Explorar datos | 3 | ✅ Done |
| US03 | Filtrar dataset (2018+) | 2 | ✅ Done |
| US04 | Crear ventanas temporales | 8 | ✅ Done |
| US05 | Calcular índice de inflación | 5 | ✅ Done |
| US06 | Entrenar modelo baseline | 3 | ✅ Done |
| US07 | Iterar el modelo | 5 | ✅ Done |
| US08 | Persistir el modelo | 1 | ✅ Done |

**Capacidad planificada:** 29 puntos
**Completados:** 29 puntos ✅

---

## Tareas técnicas

### US01 — Descargar dataset
- [x] Cuenta de Kaggle configurada
- [x] Descargar dataset Transfermarkt
- [x] Mover archivos a `data/raw/`

### US02 — Explorar datos
- [x] Cargar `players.csv`, `player_valuations.csv`, `appearances.csv`
- [x] Ver tipos, nulos, distribuciones
- [x] Detectar problemas: muchos valores faltantes en años antiguos, inflación post-Neymar

### US03 — Filtrar dataset
- [x] Probar dataset desde 2012+ → R² log = 0.65
- [x] Probar dataset desde 2018+ → R² log = 0.69
- [x] Decisión: filtrar desde 2018+
- [x] Eliminar año 2026 incompleto

### US04 — Ventanas temporales
- [x] Para cada par de valoraciones consecutivas, calcular partidos jugados en ese intervalo
- [x] Implementar con `merge_asof` de pandas
- [x] Eliminar valoraciones sin partidos en la ventana (66.5% de filas eliminadas)

### US05 — Índice de inflación
- [x] Calcular mediana del top 100 valoraciones por año
- [x] Generar coeficiente de ajuste por año
- [x] Crear columna `valor_ajustado_2025`

### US06 — Random Forest baseline
- [x] One-hot encoding de variables categóricas
- [x] Train/test split 80/20
- [x] Entrenar Random Forest con hiperparámetros por defecto
- [x] Resultado: R² = 0.5416, MAE 4.17M€

### US07 — Iterar el modelo
- [x] Aplicar transformación log al target
- [x] Cambiar a Gradient Boosting
- [x] Resultado: R² log = 0.6901, MAE 3.72M€

### US08 — Persistir modelo
- [x] Guardar con joblib en `models/modelo_final.pkl`
- [x] Guardar lista de features en `models/features.pkl`

---

## Daily reviews (resumen del trabajo diario)

| Día | Avance | Bloqueantes |
|---|---|---|
| 27/04 | Setup repo, descarga dataset, exploración inicial | Ninguno |
| 28/04 | Ventanas temporales y limpieza, índice de inflación calculado | Ninguno |
| 29/04 | RF baseline, iteración a GB con log, modelo guardado | Tiempo de entrenamiento de GB más largo de lo esperado |

---

## Sprint Review

**Demostrado al final del sprint:**
1. Notebook 01 ejecutado de principio a fin: dataset preparado en `data/processed/dataset_modelo.csv` (123.498 filas, 202 features)
2. Notebook 02 con las 2 iteraciones documentadas
3. Modelo guardado en `models/`

**Métricas alcanzadas:**
- R² log = 0.69 ✅ (objetivo: ≥ 0.65, en línea con literatura académica)
- MAE = 3.72M€ ✅ (objetivo: < 5M€)

---

## Reflexión del sprint

Lo más importante de este sprint fue la decisión de filtrar desde 2018. Empecé con datos desde 2012 y el modelo no pasaba de R² log = 0.65. Después de explorar bien los datos, vi dos problemas combinados: los datos antiguos tienen muchos valores faltantes y poca consistencia, y los precios de mercado cambiaron de escala radicalmente después del fichaje de Neymar en 2017. Esa combinación hacía la predicción muy difícil.

Filtrar desde 2018 resolvió los dos problemas a la vez. Es un buen ejemplo de por qué CRISP-DM es iterativa: a veces para mejorar el modelo no hay que tocar el modelo, hay que volver a la fase de datos.
