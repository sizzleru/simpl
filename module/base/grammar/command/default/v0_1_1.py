#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from typing import Optional
import sys

# Custom imports
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

    def rule(self: CFG, operator: CFG) -> Optional[str]:
        return operator.name

    def parse(self: CFG, path: str) -> CFG:
        return None
