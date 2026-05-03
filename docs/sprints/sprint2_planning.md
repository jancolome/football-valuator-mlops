# Sprint 2 — Tests y CI/CD

**Fechas:** 29 abril – 30 abril 2026
**Duración:** 2 días
**Objetivo:** Pipeline CI/CD funcionando en verde con tests automatizados, análisis estático y empaquetado en Docker.

---

## Sprint Goal

> *"Al final del sprint, cualquier cambio en el código se valida automáticamente con flake8 y pytest, y el proyecto se puede empaquetar en una imagen Docker reproducible."*

---

## Sprint Backlog

| ID | Historia | Puntos | Estado |
|---|---|---|---|
| US09 | Tests del dataset | 2 | ✅ Done |
| US10 | Tests del modelo | 3 | ✅ Done |
| US11 | Análisis estático con flake8 | 2 | ✅ Done |
| US12 | Pipeline CI con GitHub Actions | 5 | ✅ Done |
| US13 | Dockerfile | 3 | ✅ Done |
| US14 | Trigger automático del pipeline | 1 | ✅ Done |

**Capacidad planificada:** 16 puntos
**Completados:** 16 puntos ✅

---

## Tareas técnicas

### US09 — Tests del dataset
- [x] `test_dataset_existe`: verifica que el CSV existe y tiene > 100K filas
- [x] `test_dataset_columnas_criticas`: valida columnas esenciales y ausencia de nulos críticos

### US10 — Tests del modelo
- [x] `test_modelo_se_carga`: valida que el `.pkl` carga correctamente
- [x] `test_modelo_predice_valores_razonables`: verifica predicción coherente para un jugador de prueba

### US11 — flake8
- [x] Configurar reglas: max-line-length=120, ignore=E501,W293,W292,E303
- [x] Aplicar a carpeta `tests/`

### US12 — Pipeline CI con GitHub Actions
- [x] Crear `.github/workflows/ci.yml`
- [x] Configurar 5 pasos: checkout → setup Python → install → flake8 → pytest
- [x] Triggers: push y pull_request a main

### US13 — Dockerfile
- [x] Imagen base `python:3.13-slim`
- [x] Cacheo de capas: copiar requirements antes que código
- [x] Copia selectiva: data, models, tests, notebooks
- [x] CMD: ejecuta los tests al arrancar el contenedor

### US14 — Trigger automático
- [x] Configurar `on: push` en el workflow
- [x] Verificar que se dispara desde Mac (terminal), web GitHub y github.dev

---

## Bloqueantes encontrados durante el sprint

### Bloqueante 1 — Compilación de pandas en Python 3.13
**Síntoma:** El pipeline tardaba más de 5 minutos instalando dependencias y se quedaba colgado intentando compilar pandas desde código fuente.
**Causa:** Las versiones específicas del `requirements.txt` (pandas==2.2.0, scikit-learn==1.4.0) no tenían wheels precompilados para Python 3.13.
**Solución:** Quitar las versiones específicas del requirements.txt y dejar que pip eligiera las últimas estables compatibles con Python 3.13.
**Tiempo perdido:** ~30 min.

### Bloqueante 2 — Warnings cosméticos de flake8
**Síntoma:** El pipeline fallaba en el paso de flake8 con errores W293 (blank line contains whitespace) y W292 (no newline at end of file).
**Causa:** El editor había dejado espacios en líneas vacías y faltaba un salto de línea al final del archivo.
**Solución:** Configurar flake8 para ignorar warnings cosméticos no críticos: `--extend-ignore=E501,W293,W292,E303`.
**Tiempo perdido:** ~15 min.

### Bloqueante 3 — Personal Access Token sin scope `workflow`
**Síntoma:** `git push` rechazado por GitHub con el error: *"refusing to allow a Personal Access Token to create or update workflow without 'workflow' scope"*.
**Causa:** El PAT del Mac no tenía permisos para escribir archivos de workflow.
**Solución:** Editar el token en GitHub Settings y añadir el scope `workflow`.
**Tiempo perdido:** ~10 min.

---

## Sprint Review

**Demostrado al final del sprint:**
1. Pipeline CI/CD ejecutándose en verde en GitHub Actions (tiempo medio: 38s)
2. Los 4 tests pasando tanto en local como en GitHub
3. Dockerfile funcional (validado conceptualmente)
4. Trigger del pipeline desde 3 orígenes distintos (terminal, web, github.dev)

**Iteraciones del workflow documentadas:**
- Run #1: ❌ Falla por compilación pandas
- Run #2: ❌ Falla por warnings flake8
- Run #3: ✅ Verde, todo funcionando

---

## Reflexión del sprint

Sprint corto pero denso. Lo más valioso fue ver el pipeline CI/CD pasar de fallar 2 veces a quedarse en verde. Cada fallo me obligó a entender mejor cómo funcionan las dependencias en Python y cómo configurar bien las herramientas.

La parte de Docker fue conceptualmente clara pero no llegué a ejecutar `docker build` en mi Mac. Para validar que el Dockerfile estaba bien diseñado, hice los pasos equivalentes en una VM de Azure que monté en clase, donde sí pude ejecutar `docker build` y `docker run` con un Dockerfile simple. Eso me dio confianza en que el mío funcionaría igual.
