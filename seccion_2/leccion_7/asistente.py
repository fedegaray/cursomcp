from fastmcp import FastMCP 
import random
from datetime import datetime
import json


# Inicializamos el servidor
mcp = FastMCP("Asistente Personal MCP")


# generador de contraseñas
@mcp.tool()
def generar_contrasenia(longitud: int = 12, incluir_simbolos: bool = True) -> str:
    """Genera una contraseña segura"""
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    if incluir_simbolos:
        caracteres += "!@#$%^&*"

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return f"Contraseña generada: {contraseña}"


# Lista temporal de tareas (en memoria)
tareas = []
@mcp.tool()
def agregar_tarea(tarea: str, prioridad: str = "media") -> str:
    """Agrega una tarea a la lista"""
    nueva_tarea = {
        "id": len(tareas) + 1,
        "tarea": tarea,
        "prioridad": prioridad,
        "creada": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tareas.append(nueva_tarea)
    return f"✅ Tarea agregada: '{tarea}' con prioridad {prioridad}"


@mcp.tool()
def listar_tareas() -> str:
    """Muestra todas las tareas pendientes"""
    if not tareas:
        return "📝 No hay tareas pendientes"

    resultado = "📋 TAREAS PENDIENTES:\n"
    for t in tareas:
        emoji = {"alta": "🔴", "media": "🟡", "baja": "🟢"}.get(t["prioridad"], "⚪")
        resultado += f"{emoji} [{t['id']}] {t['tarea']} - Creada: {t['creada']}\n"
    return resultado


# Calculadora de Propinas
@mcp.tool()
def calcular_propina(total: float, porcentaje: int = 15, personas: int = 1) -> str:
    """Calcula la propina y divide la cuenta"""
    propina = total * (porcentaje / 100)
    total_con_propina = total + propina
    por_persona = total_con_propina / personas
    
    return f"""💰 CÁLCULO DE PROPINA:
    Cuenta: ${total:.2f}
    Propina ({porcentaje}%): ${propina:.2f}
    TOTAL: ${total_con_propina:.2f}
    Por persona ({personas}): ${por_persona:.2f}"""


# Información del Sistema
@mcp.tool()
def info_sistema() -> str:
    """Muestra información sobre este servidor MCP"""
    return """🤖 ASISTENTE PERSONAL MCP v1.0

Herramientas disponibles:
    • Generar contraseñas seguras
    • Gestionar lista de tareas
    • Calcular propinas
    • Y más por venir...
    
    Creado con ❤️ usando FastMCP"""


if __name__ == "__main__":
    print("Iniciando Asistente Personal MCP...")
    print("Herramientas registradas:")
    print("- Generar contraseñas seguras")
    print("- Gestionar lista de tareas")
    print("- Calcular propinas")
    print("- Información del sistema")
    mcp.run()
