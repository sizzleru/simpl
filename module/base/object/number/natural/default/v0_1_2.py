#!/usr/bin/python
from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token

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

    def parse(self: CFG, arg: Token) -> Token:
        return arg.update(value=int(arg), type=int)
