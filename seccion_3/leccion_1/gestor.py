from fastmcp import FastMCP
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict, Any


class EstadoProyecto(Enum):
    """Estados válidos para un proyecto"""
    PLANIFICACION = "planificacion"
    EN_PROGRESO = "en_progreso"
    COMPLETADO = "completado"


# Crear servidor con nombre descriptivo
mcp = FastMCP("Gestor de Proyectos Profesional")


# Base de datos en memoria (por ahora)
proyectos_db: Dict[int, Dict[str, Any]] = {}
contador_id = 0

