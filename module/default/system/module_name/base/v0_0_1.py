#!/usr/bin/python

from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.command.base.v0_0_1 import Module as Command
from module.default.system.grammar.base.v0_0_1 import Grammar, GrammarRule

@strict
class Module(Grammar):

    def root() -> bool:
        return False

    def token():
        return '/([A-Za-z0-9]|_|\\/|\\.)+/'

    def token_name() -> str:
        return 'module_name'

    def grammarize(grammars = []):
        return grammars + [(Module, Module)]
