#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.command.base.v0_0_1 import Module as Command

@strict
class Module(Command):

    def root(self: Module) -> bool:
        return False

    def terminal(self: Module) -> bool:
        return False

    def token_name(self: Module) -> str:
        return 'load'

    def token_terminal(self: Module) -> str:
        return '"load' + self._delimiter + '"'
