from __future__ import annotations

from .parse import parse_line
from .ast_builder import AstBuilder
from .codegen.irgen import Codegen
from .jit.engine import create_engine, compile_ir, get_callable
from .config import DUMP_IR


def run_repl():
    """Read-eval-print loop for MiniPy."""
    engine = create_engine()
    cg = Codegen(module_name="repl")
    ab = AstBuilder()
    anon = 0

    print("MiniPy REPL. Examples: 1+2*3  |  def add(x,y): x+y  |  add(40,2)")
    print("Type 'exit' or 'quit' to exit.")

    while True:
        try:
            line = input(">>> ").rstrip("\n")
        except EOFError:
            print()
            break

        if not line.strip():
            continue

        if line.strip().lower() in ("exit", "quit"):
            break

        tree = parse_line(line)
        stmts = tree.stmt()
        if not stmts:
            continue

        st = stmts[0]

        try:
            if st.funcdef():
                fd = ab.visit(st.funcdef())
                cg.codegen_funcdef(fd)
                compile_ir(engine, str(cg.module))
                if DUMP_IR:
                    print(cg.module)
                print("ok")
            else:
                expr = ab.visit(st.expr())
                fn_name = f"__anon_expr{anon}"
                anon += 1
                cg.codegen_toplevel_expr(fn_name, expr)
                compile_ir(engine, str(cg.module))
                if DUMP_IR:
                    print(cg.module)
                fn = get_callable(engine, fn_name)
                print(fn())
        except Exception as e:
            print(f"error: {e}")