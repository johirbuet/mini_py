from __future__ import annotations

from dataclasses import dataclass
from typing import List


class Expr:
    pass


@dataclass
class Num(Expr):
    value: float


@dataclass
class Var(Expr):
    name: str


@dataclass
class BinOp(Expr):
    op: str
    lhs: Expr
    rhs: Expr


@dataclass
class Call(Expr):
    callee: str
    args: List[Expr]


@dataclass
class FuncDef:
    name: str
    params: List[str]
    body: Expr
