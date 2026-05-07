# MiniPy Language (Python + ANTLR + LLVM via llvmlite)

This is a starter template for building a tiny Python-like language:

---

## Source / Target / Implementation Languages

- **Source language (input):** **MiniPy** — the language described by `grammar/MiniPy.g4` (e.g., `def add(x,y): x+y`, `1+2*3`).
- **Implementation language:** **Python** — the compiler pipeline (parser integration, AST, codegen, JIT, REPL) is written in Python.
- **Target:** **LLVM IR** (immediate target) emitted via `llvmlite.ir`, then JIT-compiled to **native machine code** for your host CPU using llvmlite’s **MCJIT** execution engine.

Pipeline (conceptually):

```
MiniPy source  ->  ANTLR parse tree  ->  AST  ->  LLVM IR  ->  MCJIT  ->  native machine code (exec)
```

---

## Project layout

```text
mini_py/
  grammar/   # .g4 grammar sources
  gen/       # generated ANTLR Python files
  src/minipy # language implementation (parser wrapper, AST, codegen, JIT, repl)
  scripts/   # helper scripts (generate parser)
```

---

- **Parsing**: ANTLR4 (Python3 target) generates lexer/parser/visitor.
- **Codegen**: `llvmlite.ir` emits LLVM IR.
- **Execution**: `llvmlite.binding` MCJIT compiles and runs functions.
- **REPL**: `src/minipy/repl.py` reads input, parses, compiles, executes.

## 1) Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## 2) Generate the parser

```bash
bash scripts/gen_parser.sh
# Windows PowerShell:
# ./scripts/gen_parser.ps1
```

This writes generated files into `gen/`.

## 3) Run the REPL

```bash
pip install -e .    
python -m minipy
```

### Example

```text
>>> def add(x, y): x + y
ok
>>> add(40, 2)
42.0
>>> 1 + 2 * 3
7.0
```

## Notes

- This MVP supports **single-line** function bodies: `def f(x): x + 1`
- Extending to indentation-based blocks is doable later (INDENT/DEDENT handling).
