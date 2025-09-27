#!/usr/bin/python
from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional, List

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token
from lark import Transformer

# Personal imports
from module.base.operator.io.print.default.latest import Module as Print
from source.cfg import CFG

@strict
class Module(Print):

    @property
    def name(self: CFG) -> str:
        return 'natural'

    @property
    def token(self: CFG) -> Optional[str]:
        return '[0-9]*[1-9][0-9]*'

    def rule(self: CFG, *args: CFG) -> Optional[str]:
        return None

    #def parse(self: CFG, arg: Token) -> Token:
    def parse(self: CFG, args: List[Token]) -> Token:
        value=args[0]
        return value.update(type=Natural, value=Natural(int(value)))
        #return *args.update(type=Natural, value=Natural(int(*args)))
        #print(arg)
        #exit(0)
        #print(arg, type(arg))
        #exit(0)
        #return [Token(type=Natural, value=Natural(int(natural))) for natural in arg]
        #return Token(type=Natural, value=Natural(int(arg[0])))
        #return arg.update(value=Natural(int(arg)), type=int)

    #def transform(self: CFG, arg: Token) -> Any:
    #def transform(self: CFG, arg) -> Any:
    #    print('hello?')
    #    print(arg, type(arg))
    #    exit(0)
    #    return Natural(arg)

class Natural:

    def __init__(self: Natural, value: int) -> None:
        self._value = value

    def __str__(self: Natural) -> str:
        return str(self._value)
