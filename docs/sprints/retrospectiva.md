# Retrospectiva — Football Valuator MLOps

**Fecha:** 5 mayo 2026
**Sprints cubiertos:** 1, 2 y 3 (proyecto completo)
**Formato:** Start / Stop / Continue

---

## Reflexión general

El proyecto se planteó como un pipeline MLOps individual, con la idea de aplicar CRISP-DM como metodología y trabajar en sprints cortos para no atascarme en ninguna fase. Antes de mirar atrás cada cosa por separado, quería dejar una valoración global: el proyecto cumple el alcance que me marqué al principio, y los problemas que aparecieron por el camino se pudieron resolver sin afectar la entrega.

---

## ¿Qué fue bien? (Continue)

### Iterar el modelo basándome en datos
La iteración del Random Forest baseline al Gradient Boosting con transformación logarítmica fue una mejora documentada: pasé de R² 0.54 a R² log 0.69. Pero la decisión más importante fue volver a la fase de datos y filtrar desde 2018, no desde 2012. Eso solo, sin tocar el modelo, mejoró el R² log de 0.65 a 0.69. Esa decisión está justificada por dos motivos: los datos antiguos tienen muchos valores faltantes y la inflación post-Neymar 2017 cambió la escala de precios.

### Pipeline CI/CD funcional desde el principio
Configurar GitHub Actions desde el sprint 2 me ayudó a tener feedback inmediato de cada cambio. Aunque los primeros runs fallaron, el coste de cada iteración era bajo (un commit, un push, esperar 1 minuto). Esto se nota mucho en proyectos individuales: tener una "segunda opinión automatizada" suplía no tener un compañero de equipo que revisara el código.

### Storytelling honesto
Como soy futbolista profesional, el conocimiento del dominio me permitió tomar decisiones de feature engineering que probablemente no se le ocurrirían a alguien sin contexto deportivo (por ejemplo, las ventanas temporales entre valoraciones, o la creación de tiers de liga). Defender esto en la presentación es natural y suma puntos.

### Documentar las iteraciones
Mantener un notebook de iteraciones (`02_modelo_iteraciones.ipynb`) y comentar en el commit de cada cambio qué probaba y por qué, me permite ahora reconstruir la historia del proyecto sin esfuerzo.

---

## ¿Qué no funcionó? (Stop)

### Empezar con Python 3.13 sin verificar compatibilidades
Python 3.13 es muy reciente. Las versiones específicas de pandas y scikit-learn que puse en el `requirements.txt` no tenían wheels precompilados, y el primer pipeline tardó más de 5 minutos compilando pandas desde código fuente. Tuve que quitar las versiones específicas para que pip instalara las últimas estables. Para futuros proyectos: verificar antes de fijar el `requirements.txt` que las versiones tienen wheels disponibles para la versión de Python elegida.

### No haber configurado el Personal Access Token al inicio
Al subir el primer workflow YAML, el push fue rechazado porque el token no tenía el scope `workflow`. Resolverlo era trivial (editar el token en GitHub), pero me hizo perder 10 minutos de un commit que ya tenía preparado. Para futuros proyectos: configurar los tokens con todos los scopes necesarios al crear el repo.

### Subestimar el tiempo de los entregables no técnicos
Pensaba que con el código terminado el resto sería rápido, pero la memoria, la presentación y el vídeo se llevan tanto tiempo como el código. La próxima vez bloquearía un sprint entero solo para entregables.

---

## ¿Qué mejoraríamos? (Start)

### Empezar la memoria desde el sprint 1
En lugar de dejar la memoria para el final, ir documentando las decisiones técnicas en un `docs/decisiones.md` desde el primer día. Cuando llegue el momento de redactar la memoria, ya tienes el material recogido y solo hay que darle estructura.

### Configurar pre-commit hooks
Para evitar problemas como el de los warnings cosméticos de flake8, configurar pre-commit hooks que ejecuten flake8 en local antes de cada commit. Así los errores se detectan antes del push, no en el pipeline.

### Pensar en el vídeo desde el principio
Si la entrega final es un vídeo, las decisiones de diseño deberían tener en cuenta cómo se van a contar visualmente. Algunos diagramas que tengo ahora son muy densos para vídeo. La próxima vez los diseñaría pensando en la cámara, no solo en una diapositiva estática.

---

## Reflexión sobre la metodología

¿Sirvió SCRUM/Kanban en un proyecto individual?

Honestamente, **un SCRUM tradicional con sprints semanales y ceremonias completas no encaja en un proyecto individual de menos de 2 semanas**. No tiene sentido hacer daily standups con uno mismo, ni planning meetings de 2 horas para definir 5 historias de usuario.

Lo que SÍ funcionó fue una mezcla:

1. **Backlog real**: una lista priorizada de historias de usuario, escritas en formato estándar. Esto sí lo apliqué desde el primer día y me ayudó a no perderme.
2. **Sprints cortos** (2-5 días) con un objetivo claro: "datos y modelo", "tests y CI/CD", "documentación". Esto funciona bien porque los hitos son verificables.
3. **Tablero Kanban** como registro visual del progreso, no como herramienta de gestión en vivo. Lo monté hacia el final del proyecto, pero las decisiones que reflejaba eran reales.
4. **Retrospectiva escrita** al final del proyecto, como esta. Esto sí aporta mucho valor: forzarse a reflexionar sobre lo que fue bien y lo que no, y dejarlo por escrito.

Lo que el profesor explicó en clase sobre los "carriles de velocidad" del desarrollo (rápido sin SCRUM, medio híbrido, lento con SCRUM tradicional) tiene mucho sentido. Mi proyecto encaja en el carril rápido / medio: iteración continua, decisiones rápidas, documentación a posteriori.

---

## Velocidad por sprint

| Sprint | Puntos planificados | Puntos completados | % completado |
|---|---|---|---|
| Sprint 1 | 29 | 29 | 100% |
| Sprint 2 | 16 | 16 | 100% |
| Sprint 3 | 17 | 4 + 10 en curso | en progreso |
| **Total proyecto** | **62** | **49 done + 10 wip** | **~95%** |

---

## Conclusión personal

El valor real de hacer este proyecto no fue el resultado del modelo (R² log 0.69 está en línea con la literatura, ni más ni menos), sino el proceso completo de MLOps: pasar de un notebook a un pipeline reproducible que cualquier persona puede clonar y ejecutar. Eso es lo que diferencia un ejercicio académico de un producto real.
