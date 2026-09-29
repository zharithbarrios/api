from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import (
    rol_routes, usuario_routes, modulo_routes, modulo_rol_routes,
    estudiante_routes, acudiente_routes, categoria_actividad_routes,
    actividad_routes, inscripcion_routes, autorizacion_routes,
    asistencia_routes, notificacion_routes
)

app = FastAPI(
    title="Gestión de Eventos y Actividades Extracurriculares",
    description="API para gestión de actividades extracurriculares con autorización digital",
    version="1.0.0"
)

# Registrar todas las rutas
app.include_router(rol_routes.router)
app.include_router(usuario_routes.router)
app.include_router(modulo_routes.router)
app.include_router(modulo_rol_routes.router)
app.include_router(estudiante_routes.router)
app.include_router(acudiente_routes.router)
app.include_router(categoria_actividad_routes.router)
app.include_router(actividad_routes.router)
app.include_router(inscripcion_routes.router)
app.include_router(autorizacion_routes.router)
app.include_router(asistencia_routes.router)
app.include_router(notificacion_routes.router)

@app.get("/")
def root():
    return {
        "message": "API Gestión de Eventos y Actividades Extracurriculares",
        "docs": "/docs",
        "status": "Funcionando correctamente"
    }