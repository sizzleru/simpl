#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from typing import Optional

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token

# Personal imports
from source.cfg import CFG

@strict
class Module(CFG):

    @property
    def name(self: CFG) -> str:
        return 'line'

    @property
    def token(self: CFG) -> Optional[str]:
        return None

    def rule(self: CFG, arg: CFG) -> Optional[str]:
        return arg.name + '"\\n"' + self.name + '?'

    def parse(self: CFG, *args: Token) -> Token:
        for arg in args:
            if arg != 0: # Error status should be a class
                raise ValueError("Error was received")
        return None
