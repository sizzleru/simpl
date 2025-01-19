#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from abc import abstractmethod

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.command.base.v0_0_1 import Module as Command

@strict
class Module(Command):

    def root() -> bool:
        return False

    def token() -> str:
        return 'printable'

    def token_name() -> str:
        return 'printable'

    def grammarize(grammars = []):
        return grammars + [(Command, Module)]

    @abstractmethod
    def __str__(self: Module) -> str:
        pass
