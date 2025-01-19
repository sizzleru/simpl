#!/usr/bin/python

from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.command.base.v0_0_1 import Module as Command
from module.default.system.grammar.base.v0_0_1 import Grammar, GrammarRule
from module.default.system.printable.str.v0_0_1 import Module as Printable

@strict
class Module(Printable):

    def root() -> bool:
        return False

    def token() -> str:
        return '/[1-9][0-9]*/'

    def token_name() -> str:
        return 'integers'

    def grammarize(grammars = []):
        return grammars + [(Printable, Module)]
