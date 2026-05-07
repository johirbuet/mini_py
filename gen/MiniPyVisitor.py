# Generated from grammar/MiniPy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniPyParser import MiniPyParser
else:
    from MiniPyParser import MiniPyParser

# This class defines a complete generic visitor for a parse tree produced by MiniPyParser.

class MiniPyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniPyParser#repl.
    def visitRepl(self, ctx:MiniPyParser.ReplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#stmt.
    def visitStmt(self, ctx:MiniPyParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#funcdef.
    def visitFuncdef(self, ctx:MiniPyParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#params.
    def visitParams(self, ctx:MiniPyParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#Call.
    def visitCall(self, ctx:MiniPyParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#MulDiv.
    def visitMulDiv(self, ctx:MiniPyParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#AddSub.
    def visitAddSub(self, ctx:MiniPyParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#Var.
    def visitVar(self, ctx:MiniPyParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#Parens.
    def visitParens(self, ctx:MiniPyParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#Num.
    def visitNum(self, ctx:MiniPyParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#args.
    def visitArgs(self, ctx:MiniPyParser.ArgsContext):
        return self.visitChildren(ctx)



del MiniPyParser