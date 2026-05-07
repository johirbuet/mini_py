from __future__ import annotations

# Generated visitor + parser contexts
from gen.MiniPyVisitor import MiniPyVisitor
from gen.MiniPyParser import MiniPyParser

from .ast_nodes import Num, Var, BinOp, Call, FuncDef


class AstBuilder(MiniPyVisitor):
    """Build a small AST from the ANTLR parse tree."""

    def visitNum(self, ctx: MiniPyParser.NumContext):
        return Num(float(ctx.NUMBER().getText()))

    def visitVar(self, ctx: MiniPyParser.VarContext):
        return Var(ctx.NAME().getText())

    def visitAddSub(self, ctx: MiniPyParser.AddSubContext):
        return BinOp(ctx.op.text, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitMulDiv(self, ctx: MiniPyParser.MulDivContext):
        return BinOp(ctx.op.text, self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitCall(self, ctx: MiniPyParser.CallContext):
        callee = ctx.NAME().getText()
        args = []
        if ctx.args():
            for e in ctx.args().expr():
                args.append(self.visit(e))
        return Call(callee, args)

    def visitFuncdef(self, ctx: MiniPyParser.FuncdefContext):
        name = ctx.NAME().getText()
        params = []
        if ctx.params():
            params = [n.getText() for n in ctx.params().NAME()]
        body = self.visit(ctx.expr())
        return FuncDef(name, params, body)
