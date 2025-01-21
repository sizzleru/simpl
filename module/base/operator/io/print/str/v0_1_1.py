#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.base.grammar.command.default.latest import Module as Command
from source.cfg import CFG

@strict
class Module(Command):

    @property
    def name(self: CFG) -> str:
        return 'print'

    @property
    def token(self: CFG) -> Optional[str]:
        return None

    def rule(self: CFG, object: CFG) -> Optional[str]:
        return object.name

    def parse(self: CFG, tok: str) -> CFG:
        print(tok)
        return None

