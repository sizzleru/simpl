#!/usr/bin/python

from __future__ import annotations

# Builtin imports from abc import ABC, abstractmethod
from typing import Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports
from module.default.system.load.base.v0_0_1 import Module as Load

@strict
class Module(Load):

    def root(self: Module) -> bool:
        return False

    def terminal(self: Module) -> bool:
        return True

    def token(self: Module) -> str:
        return self.load_object('/([A-Za-z0-9]|_|\\/|\\.)+/')
