from mcp.server import MCPServer

mcp = MCPServer("Evolyn Tools")


@mcp.tool()
def calculate(expression: str) -> str:
    """Evaluate a basic arithmetic expression using Python's restricted evaluator."""
    allowed = set("0123456789+-*/(). %")
    if not expression or any(char not in allowed for char in expression):
        raise ValueError("Only basic arithmetic characters are allowed.")
    try:
        value = eval(expression, {"__builtins__": {}}, {})
    except Exception as exc:
        raise ValueError(f"Invalid arithmetic expression: {exc}") from exc
    return str(value)


def main() -> None:
    mcp.run(transport="stdio")
