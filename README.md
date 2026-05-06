# Football Valuator MLOps

Predicción del valor de mercado de futbolistas profesionales con un pipeline MLOps completo: datos, modelo, tests automatizados y despliegue continuo.

**Jan Colomé · Mayo 2026 · Metodologías de Desarrollo y Despliegue de Aplicaciones para Ciencia de Datos — VIU**

---

## ¿Qué hace este proyecto?

Predice el valor de mercado de un futbolista profesional a partir de datos públicos de Transfermarkt (edad, liga, minutos jugados, internacionalidades, goles). El objetivo no es solo el modelo, sino demostrar un pipeline MLOps profesional: automatizado, testeado y reproducible.

**Métricas del modelo final:**
- R² (escala log): 0.6901
- MAE: 3.72 millones de euros
- RMSE: 9.04 millones de euros

El modelo predice **valor de mercado**, no precio pagado en una operación real. Son conceptos distintos.

---

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Datos | pandas, numpy |
| Modelado | scikit-learn (Gradient Boosting), joblib |
| Tests | pytest, pytest-cov |
| Calidad de código | flake8 |
| Empaquetado | Docker (python:3.13-slim) |
| CI/CD | GitHub Actions |
| Control de versiones | Git, GitHub |

---

## Estructura del repositorio

```
football-valuator-mlops/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI/CD con GitHub Actions
├── data/
│   └── processed/
│       └── dataset_modelo.csv  # Dataset procesado (123.498 filas)
├── models/
│   ├── modelo_final.pkl        # Modelo Gradient Boosting entrenado
│   └── features.pkl            # Lista de features del modelo
├── notebooks/
│   ├── 01_preparacion_datos.ipynb
│   └── 02_modelo.ipynb
├── tests/
│   └── test_modelo.py          # 4 tests automatizados con pytest
├── docs/
│   ├── product_backlog.md
│   └── sprints/                # Documentación de los 3 sprints
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Cómo ejecutar el proyecto

### Opción 1 — Con Docker (recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/jancolome/football-valuator-mlops.git
cd football-valuator-mlops

# Construir la imagen
docker build -t football-valuator .

# Ejecutar los tests dentro del contenedor
docker run football-valuator
```

### Opción 2 — Local con Python

```bash
# Clonar el repositorio
git clone https://github.com/jancolome/football-valuator-mlops.git
cd football-valuator-mlops

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar los tests
pytest tests/ -v

# Ejecutar los tests con cobertura
pytest tests/ --cov=tests --cov-report=term-missing -v
```

---

## Pipeline CI/CD

El workflow de GitHub Actions se dispara automáticamente con cada push a `main` y ejecuta:

1. Checkout del repositorio
2. Configurar Python 3.13
3. Instalar dependencias
4. Análisis estático con flake8
5. Ejecutar tests con pytest

**Tiempo medio de ejecución: 38 segundos.**

---

## Tests automatizados

El proyecto incluye 4 tests que cubren los puntos críticos del pipeline:

| Test | Qué valida |
|------|-----------|
| `test_dataset_existe` | El dataset procesado existe y tiene más de 100.000 filas |
| `test_dataset_columnas_criticas` | Las columnas esenciales están presentes y sin nulos |
| `test_modelo_se_carga` | El modelo .pkl carga correctamente en memoria |
| `test_modelo_predice_valores_razonables` | La predicción sobre un jugador de prueba cae en un rango humano |

---

## Decisiones técnicas clave

- **Filtrado desde 2018+**: Los datos anteriores al fichaje de Neymar (2017) pertenecen a una escala económica extinta. Filtrar mejoró el R² de 0.65 a 0.69 sin modificar el algoritmo.
- **Ventanas temporales**: En lugar de agregar por temporada, cada valoración se asocia a los partidos jugados entre esa valoración y la anterior. Esto multiplica el dataset ×10 y captura el rendimiento reciente.
- **Índice de inflación**: Las valoraciones históricas se normalizan a escala 2025 usando la mediana del top 100 de jugadores por año.
- **Tiers de liga**: Las ligas se agrupan en 4 niveles (Tier 1: 5 grandes, Tier 2: medianas, Tier 3: resto, Tier 99: UEFA) en lugar de tratar cada liga como variable independiente.
- **Transformación logarítmica del target**: La distribución de valores es muy asimétrica. Aplicar log comprime la cola larga y permite al Gradient Boosting capturar mejor la estructura subyacente.

---

## Metodología

El proyecto sigue **CRISP-DM** como marco metodológico y un enfoque ágil adaptado con 3 sprints documentados:

| Sprint | Fechas | Foco | Puntos |
|--------|--------|------|--------|
| Sprint 1 | 27-29 abr | Datos y modelo | 29 pts |
| Sprint 2 | 29-30 abr | Tests y CI/CD | 16 pts |
| Sprint 3 | 1-5 may | Documentación y entrega | 17 pts |

La documentación completa de sprints, backlog y retrospectiva está en `/docs/sprints/`.

---

## Limitaciones honestas

- Predice valor de mercado, no precio pagado en una operación real
- No captura el premium mediático de las superestrellas (>50M €)
- Limitado a datos públicos de Transfermarkt
- Mayor precisión en el rango 5-50M € (donde se realizan la mayoría de fichajes reales)