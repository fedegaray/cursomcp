import asyncio
from mcp.server import Server   
from mcp.server.models import InicializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

server = Server("Servidor Tradicional")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            nombre="saludar",
            description="Saluda a alguien",
            inputSchema={
                "type": "object",
                "properties": {
                    "nombre": {"type": "string"}
                },
                "required": ["nombre"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name:str, arguments:dict):
    if name == "saludar":
        nombre = arguments.get("nombre")
        return [TextContent(text=f"Hola {nombre}! Bienvenido a MCP")]
    raise ValueError(f"Herramienta desconocida: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InicializationOptions()
        )

if __name__ == "__main__":
    asyncio.run(main())
