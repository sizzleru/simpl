#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

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

    def rule(self: CFG, grammar: CFG) -> Optional[str]:
        return grammar.name + '"\\n"' + self.name + '?'

    def parse(self: CFG, path: str) -> CFG:
        return None
