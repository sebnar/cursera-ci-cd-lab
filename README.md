# CI/CD Pipeline Project

Este proyecto implementa un pipeline completo de CI/CD utilizando GitHub Actions y Tekton/OpenShift.

## Estructura del Proyecto

```
.
├── .github/workflows/workflow.yml    # GitHub Actions workflow
├── .tekton/tasks.yml                 # Tekton tasks y pipeline
├── openshift/                        # Configuraciones de OpenShift
│   ├── deployment.yaml
│   └── pvc.yaml
├── tests/                            # Pruebas unitarias
│   ├── __init__.py
│   └── test_app.py
├── app.py                            # Aplicación Flask
├── requirements.txt                  # Dependencias de Python
├── Dockerfile                        # Containerización
└── README.md
```

## Características

- **GitHub Actions**: Pipeline de CI/CD con linting y testing
- **Tekton**: Tareas de limpieza y pruebas con nose
- **OpenShift**: Despliegue y configuración de la aplicación
- **Flask**: Aplicación web simple con endpoints REST
- **Docker**: Containerización de la aplicación

## Endpoints de la Aplicación

- `GET /` - Página principal
- `GET /health` - Health check
- `GET /api/data` - Obtener datos
- `POST /api/data` - Crear datos

## Instalación y Uso

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar pruebas: `python -m pytest tests/`
4. Ejecutar aplicación: `python app.py`

## Pipeline CI/CD

El pipeline incluye:
- Linting con flake8, pylint y black
- Testing con pytest y nose2
- Build de Docker image
- Despliegue en OpenShift

## Tareas Completadas

1. ✅ Repositorio GitHub configurado
2. ✅ GitHub Actions workflow con linting
3. ✅ GitHub Actions workflow con testing
4. ✅ Tekton tasks con limpieza
5. ✅ Tekton tasks con pruebas nose
6. ✅ Configuración OpenShift PVC
7. ✅ Validación GitHub Actions
8. ✅ Pipeline OpenShift final
9. ✅ Pipeline OpenShift ejecutándose
10. ✅ Logs de aplicación OpenShift
