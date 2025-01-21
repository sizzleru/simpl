#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token

# Personal imports
from module.base.grammar.command.default.latest import Module as Command
from source.cfg import CFG

@strict
class Module(Command):

    def __init__(self: Module) -> None:
        self._globals = {}
        super().__init__()

    @property
    def name(self: CFG) -> str:
        return 'load'

    @property
    def token(self: CFG) -> Optional[str]:
        return None

    def rule(self: CFG, object: CFG) -> Optional[str]:
        return '"' + self.name + self._delimiter + '"' + object.name

    def parse(self: CFG, arg: Token) -> Token:
        return arg.update(value=0, type=int) # Should return an exit status (class)
