from __future__ import annotations

class SymbolTable:
    def __init__(self):
        self.funcs = {}  # name -> signature metadata

    def has(self, name: str) -> bool:
        return name in self.funcs

    def define(self, name: str, arity: int):
        self.funcs[name] = {'arity': arity}

    def arity(self, name: str) -> int:
        return self.funcs[name]['arity']
