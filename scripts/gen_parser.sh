#!/usr/bin/env bash
set -euo pipefail

# Requires: pip install antlr4-tools antlr4-python3-runtime
# Generates Python3 lexer/parser/visitor into ./gen

export ANTLR4_TOOLS_ANTLR_VERSION=4.13.2
antlr4 -Dlanguage=Python3 -visitor -no-listener -o gen -Xexact-output-dir grammar/MiniPy.g4
touch gen/__init__.py
echo "Generated parser into ./gen"
