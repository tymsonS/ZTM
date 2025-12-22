from pathlib import Path
import ast

def load_silnia():
    src_path = Path(__file__).resolve().parents[1] / "main.py"
    src = src_path.read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "silnia":
            mod = ast.Module(body=[node], type_ignores=[])
            code = compile(mod, filename=str(src_path), mode="exec")
            ns = {}
            exec(code, ns)
            return ns["silnia"]
    raise RuntimeError("Funkcja 'silnia' nie znaleziona w main.py")

def test_silnia_5():
    silnia = load_silnia()
    assert silnia(5) == 120