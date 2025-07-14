#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from typing import Optional
from sys import exit

# Custom imports
from lark.lexer import Token
from typeguard import typechecked as strict

# Personal imports
from module.base.grammar.line.default.latest import Module as Line
from source.cfg import CFG

@strict
class Module(Line):

    @property
    def name(self: CFG) -> str:
        return 'command'

    @property
    def token(self: CFG) -> Optional[str]:
        return None

    def rule(self: CFG, arg: CFG) -> Optional[str]:
        return arg.name

    #def parse(self: CFG, arg: Token) -> Token:
    def parse(self: CFG, arg) -> Token:
        return Token(value=arg, type=list) # Compound of exit statuses
