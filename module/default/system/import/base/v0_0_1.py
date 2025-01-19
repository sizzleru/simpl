#!/usr/bin/python

from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.command.base.v0_0_1 import Module as Command
from module.default.system.grammar.base.v0_0_1 import Grammar, GrammarRule
from module.default.system.module_name.base.v0_0_1 import Module as ModuleName

@strict
class Module(Command):

    def root() -> bool:
        return False

    def token() -> str:
        return '"import' + Module.delimiter + '"' + ModuleName.token_name()

    def token_name() -> str:
        return 'import'

    def grammarize(grammars = []):
        return grammars + [(Command, Module)]
