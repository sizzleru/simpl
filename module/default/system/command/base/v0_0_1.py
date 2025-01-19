#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.grammar.base.v0_0_1 import Grammar

@strict
class Module(Grammar):

    def root(self: Module) -> bool:
        return True

    def terminal(self: Module) -> bool:
        return False

    def token(self: Module) -> str:
        return 'command'

    def token_from(self: Module) -> str:
        return self._parent().token()
