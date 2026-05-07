grammar MiniPy;

    repl : (stmt NEWLINE)* stmt? NEWLINE* EOF ;

    stmt
      : funcdef
      | expr
      ;

    funcdef : DEF NAME LPAREN params? RPAREN COLON expr ;

    params  : NAME (COMMA NAME)* ;

    expr
      : expr op=('*'|'/') expr         # MulDiv
      | expr op=('+'|'-') expr         # AddSub
      | NAME LPAREN args? RPAREN       # Call
      | NAME                           # Var
      | NUMBER                         # Num
      | LPAREN expr RPAREN             # Parens
      ;

    args    : expr (COMMA expr)* ;

    DEF     : 'def' ;
    COLON   : ':' ;
    COMMA   : ',' ;
    LPAREN  : '(' ;
    RPAREN  : ')' ;

    NAME    : [a-zA-Z_][a-zA-Z_0-9]* ;
    NUMBER  : [0-9]+ ('.' [0-9]+)? ;

    NEWLINE : ('\r'? '\n')+ ;
    WS      : [ \t]+ -> skip ;
