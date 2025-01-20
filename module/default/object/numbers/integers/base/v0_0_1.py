#!/usr/bin/python

from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.printable.str.v0_0_1 import Module as Printable

@strict
class Module(Printable):

    def root(self: Module) -> bool:
        return False

    def terminal(self: Module) -> bool:
        return True

    def token(self: Module) -> str:
        return Printable().token_terminal() + self.token_name()

    def token_name(self: Module) -> str:
        return 'integer'

    def token_terminal(self: Module) -> str:
        return '/[1-9]+[0-9]*/'

    def str(self: Module) -> str:
        return 'Number'
