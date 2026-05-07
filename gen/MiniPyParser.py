# Generated from grammar/MiniPy.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,3,0,22,8,0,1,0,5,0,25,8,0,
        10,0,12,0,28,9,0,1,0,1,0,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,3,2,
        40,8,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,
        4,1,4,1,4,1,4,3,4,58,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,67,8,4,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,5,1,5,1,5,
        5,5,83,8,5,10,5,12,5,86,9,5,1,5,0,1,8,6,0,2,4,6,8,10,0,2,1,0,1,2,
        1,0,3,4,94,0,17,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,45,1,0,0,0,8,
        66,1,0,0,0,10,79,1,0,0,0,12,13,3,2,1,0,13,14,5,12,0,0,14,16,1,0,
        0,0,15,12,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,21,
        1,0,0,0,19,17,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,21,22,1,0,0,0,
        22,26,1,0,0,0,23,25,5,12,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,
        0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,0,0,1,30,
        1,1,0,0,0,31,34,3,4,2,0,32,34,3,8,4,0,33,31,1,0,0,0,33,32,1,0,0,
        0,34,3,1,0,0,0,35,36,5,5,0,0,36,37,5,10,0,0,37,39,5,8,0,0,38,40,
        3,6,3,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,9,0,0,
        42,43,5,6,0,0,43,44,3,8,4,0,44,5,1,0,0,0,45,50,5,10,0,0,46,47,5,
        7,0,0,47,49,5,10,0,0,48,46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,
        51,1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,54,6,4,-1,0,54,55,5,10,
        0,0,55,57,5,8,0,0,56,58,3,10,5,0,57,56,1,0,0,0,57,58,1,0,0,0,58,
        59,1,0,0,0,59,67,5,9,0,0,60,67,5,10,0,0,61,67,5,11,0,0,62,63,5,8,
        0,0,63,64,3,8,4,0,64,65,5,9,0,0,65,67,1,0,0,0,66,53,1,0,0,0,66,60,
        1,0,0,0,66,61,1,0,0,0,66,62,1,0,0,0,67,76,1,0,0,0,68,69,10,6,0,0,
        69,70,7,0,0,0,70,75,3,8,4,7,71,72,10,5,0,0,72,73,7,1,0,0,73,75,3,
        8,4,6,74,68,1,0,0,0,74,71,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,
        77,1,0,0,0,77,9,1,0,0,0,78,76,1,0,0,0,79,84,3,8,4,0,80,81,5,7,0,
        0,81,83,3,8,4,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,
        1,0,0,0,85,11,1,0,0,0,86,84,1,0,0,0,11,17,21,26,33,39,50,57,66,74,
        76,84
    ]

class MiniPyParser ( Parser ):

    grammarFileName = "MiniPy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'def'", "':'", 
                     "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DEF", "COLON", "COMMA", "LPAREN", "RPAREN", 
                      "NAME", "NUMBER", "NEWLINE", "WS" ]

    RULE_repl = 0
    RULE_stmt = 1
    RULE_funcdef = 2
    RULE_params = 3
    RULE_expr = 4
    RULE_args = 5

    ruleNames =  [ "repl", "stmt", "funcdef", "params", "expr", "args" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    DEF=5
    COLON=6
    COMMA=7
    LPAREN=8
    RPAREN=9
    NAME=10
    NUMBER=11
    NEWLINE=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ReplContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniPyParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.StmtContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniPyParser.NEWLINE)
            else:
                return self.getToken(MiniPyParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniPyParser.RULE_repl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepl" ):
                return visitor.visitRepl(self)
            else:
                return visitor.visitChildren(self)




    def repl(self):

        localctx = MiniPyParser.ReplContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_repl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 12
                    self.stmt()
                    self.state = 13
                    self.match(MiniPyParser.NEWLINE) 
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3360) != 0):
                self.state = 20
                self.stmt()


            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 23
                self.match(MiniPyParser.NEWLINE)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(MiniPyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdef(self):
            return self.getTypedRuleContext(MiniPyParser.FuncdefContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniPyParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniPyParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.funcdef()
                pass
            elif token in [8, 10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(MiniPyParser.DEF, 0)

        def NAME(self):
            return self.getToken(MiniPyParser.NAME, 0)

        def LPAREN(self):
            return self.getToken(MiniPyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniPyParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(MiniPyParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)


        def params(self):
            return self.getTypedRuleContext(MiniPyParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniPyParser.RULE_funcdef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdef" ):
                return visitor.visitFuncdef(self)
            else:
                return visitor.visitChildren(self)




    def funcdef(self):

        localctx = MiniPyParser.FuncdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MiniPyParser.DEF)
            self.state = 36
            self.match(MiniPyParser.NAME)
            self.state = 37
            self.match(MiniPyParser.LPAREN)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 38
                self.params()


            self.state = 41
            self.match(MiniPyParser.RPAREN)
            self.state = 42
            self.match(MiniPyParser.COLON)
            self.state = 43
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(MiniPyParser.NAME)
            else:
                return self.getToken(MiniPyParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniPyParser.COMMA)
            else:
                return self.getToken(MiniPyParser.COMMA, i)

        def getRuleIndex(self):
            return MiniPyParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MiniPyParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MiniPyParser.NAME)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 46
                self.match(MiniPyParser.COMMA)
                self.state = 47
                self.match(MiniPyParser.NAME)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniPyParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(MiniPyParser.NAME, 0)
        def LPAREN(self):
            return self.getToken(MiniPyParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniPyParser.RPAREN, 0)
        def args(self):
            return self.getTypedRuleContext(MiniPyParser.ArgsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(MiniPyParser.NAME, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniPyParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniPyParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(MiniPyParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniPyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = MiniPyParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 54
                self.match(MiniPyParser.NAME)
                self.state = 55
                self.match(MiniPyParser.LPAREN)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3328) != 0):
                    self.state = 56
                    self.args()


                self.state = 59
                self.match(MiniPyParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = MiniPyParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(MiniPyParser.NAME)
                pass

            elif la_ == 3:
                localctx = MiniPyParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(MiniPyParser.NUMBER)
                pass

            elif la_ == 4:
                localctx = MiniPyParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(MiniPyParser.LPAREN)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(MiniPyParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniPyParser.MulDivContext(self, MiniPyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniPyParser.AddSubContext(self, MiniPyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 72
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 73
                        self.expr(6)
                        pass

             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniPyParser.COMMA)
            else:
                return self.getToken(MiniPyParser.COMMA, i)

        def getRuleIndex(self):
            return MiniPyParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = MiniPyParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.expr(0)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 80
                self.match(MiniPyParser.COMMA)
                self.state = 81
                self.expr(0)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




