# Requires: pip install antlr4-tools antlr4-python3-runtime
# Generates Python3 lexer/parser/visitor into .\gen

antlr4 -Dlanguage=Python3 -visitor -no-listener -o gen grammar\MiniPy.g4
Write-Host "Generated parser into .\gen"
