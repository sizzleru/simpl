#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.grammar.base.v0_0_1 import Grammar, GrammarRule

#@strict
class Module(Grammar):

    def __init__(self, arg):
        print(arg)

    def root() -> bool:
        return True

    def token_name() -> str:
        return 'command'

    def tokenize() -> Optional[GrammarRule]:
        return Module.token_name()
