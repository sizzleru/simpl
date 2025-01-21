#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from abc import abstractproperty
from typing import Optional

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token

# Personal imports
from module.base.operator.io.load.default.latest import Module as Load
from source.module import load_modules, ModulePath
from source.cfg import CFG

@strict
class Module(Load):

    @property
    def name(self: CFG) -> str:
        return 'module'

    @property
    def token(self: CFG) -> Optional[str]:
        return '([A-Za-z0-9]|_|\\/)+'

    def rule(self: CFG, *args: str) -> Optional[str]:
        return None

    def parse(self: CFG, arg: Token) -> Token:
        return arg.update(value=ModulePath(arg), type=ModulePath)
