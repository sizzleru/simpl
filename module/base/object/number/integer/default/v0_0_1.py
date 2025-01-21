#!/usr/bin/python

from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.base.operator.io.print.str.v0_0_1 import Module as Print

@strict
class Module(Print):

    def root(self: Module) -> bool:
        return False

    def terminal(self: Module) -> bool:
        return True

    def token(self: Module) -> str:
        return self._parent().token_terminal() + self.token_name()

    def token_name(self: Module) -> str:
        return 'integer'

    def token_terminal(self: Module) -> str:
        return '/[1-9]+[0-9]*/'

    def str(self: Module) -> str:
        return 'Number'
