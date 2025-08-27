from fastmcp import FastMCP

mcp = FastMCP("Mi Primer Servidor")

@mcp.tool()
def saludar(nombre:str) -> str:
  """Saluda a alguien por su nombre"""
  return f"¡Hola {nombre}! Bienvenido a MCP"

@mcp.tool()
def calcular_edad(anio_nacimiento: int) -> str:
    """Calcula la edad de alguien"""
    edad = 2025 - año_nacimiento
    return f"Tienes {edad} años"


if __name__ == "__main__":
  mcp.run()
