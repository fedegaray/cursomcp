from fastmcp import FastMCP

mcp = FastMCP("Mi Primer Servidor")

@mcp.tool()
def saludar(nombre:str) -> str:
  """Saluda a alguien por su nombre"""
  return f"¡Hola {nombre}! Bienvenido a MCP"

if __name__ == "__main__":
  mcp.run()
