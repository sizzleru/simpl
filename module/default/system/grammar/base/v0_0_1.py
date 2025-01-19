#!/usr/bin/python

from __future__ import annotations
# Builtin imports
from abc import ABC, abstractmethod
from typing import Any, Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports

class GrammarRule:

    def __init__(self: GrammarRule, LHS: str, RHS: str):
        self._LHS = LHS
        self._RHS = RHS

    def __str__(self: GrammarRule) -> str:
        return self._LHS + " -> " + self._RHS

@strict
class Grammar(ABC):

    delimiter = ' '

    #@abstractmethod
    def token() -> str:
        pass

    @abstractmethod
    def token_name() -> str:
        pass

    @abstractmethod
    def root() -> bool:
        return False

    @abstractmethod
    def grammarize(grammars = []):
        pass
