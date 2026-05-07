from __future__ import annotations

from llvmlite import ir

from ..ast_nodes import Num, Var, BinOp, Call, FuncDef
from .symbols import SymbolTable


DOUBLE = ir.DoubleType()


class Codegen:
    """AST -> LLVM IR (llvmlite.ir)."""

    def __init__(self, module_name: str = 'repl'):
        self.module = ir.Module(name=module_name)
        self.symbols = SymbolTable()
        self.functions = {}  # name -> ir.Function

    def _get_or_declare_function(self, name: str, arity: int) -> ir.Function:
        if name in self.functions:
            return self.functions[name]
        fnty = ir.FunctionType(DOUBLE, [DOUBLE] * arity)
        fn = ir.Function(self.module, fnty, name=name)
        self.functions[name] = fn
        self.symbols.define(name, arity)
        return fn

    def codegen_expr(self, builder: ir.IRBuilder, env: dict, e):
        if isinstance(e, Num):
            return ir.Constant(DOUBLE, e.value)
        if isinstance(e, Var):
            if e.name not in env:
                raise NameError(f"Undefined variable: {e.name}")
            return env[e.name]
        if isinstance(e, BinOp):
            lhs = self.codegen_expr(builder, env, e.lhs)
            rhs = self.codegen_expr(builder, env, e.rhs)
            if e.op == '+':
                return builder.fadd(lhs, rhs)
            if e.op == '-':
                return builder.fsub(lhs, rhs)
            if e.op == '*':
                return builder.fmul(lhs, rhs)
            if e.op == '/':
                return builder.fdiv(lhs, rhs)
            raise ValueError(f"Unknown operator: {e.op}")
        if isinstance(e, Call):
            callee = self._get_or_declare_function(e.callee, len(e.args))
            argv = [self.codegen_expr(builder, env, a) for a in e.args]
            return builder.call(callee, argv)
        raise TypeError(f"Unknown expr node: {type(e)}")

    def codegen_funcdef(self, f: FuncDef) -> ir.Function:
        fn = self._get_or_declare_function(f.name, len(f.params))
        # Create body only once (disallow redef in MVP)
        if fn.blocks:
            raise ValueError(f"Function '{f.name}' already defined.")
        block = fn.append_basic_block('entry')
        builder = ir.IRBuilder(block)
        env = {p: a for p, a in zip(f.params, fn.args)}
        retv = self.codegen_expr(builder, env, f.body)
        builder.ret(retv)
        return fn

    def codegen_toplevel_expr(self, name: str, expr) -> ir.Function:
        fnty = ir.FunctionType(DOUBLE, [])
        fn = ir.Function(self.module, fnty, name=name)
        block = fn.append_basic_block('entry')
        builder = ir.IRBuilder(block)
        retv = self.codegen_expr(builder, {}, expr)
        builder.ret(retv)
        return fn
