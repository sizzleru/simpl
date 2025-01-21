#!/usr/bin/python

from __future__ import annotations
# Builtin imports
from abc import ABC, abstractmethod
from typing import Any, Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports

@strict
class Grammar(ABC):

    _instantiated = set()
    _instance = None

    def __new__(cls):
        cls._parent = cls.__bases__[0]

        if not cls in cls._instantiated:
            cls._instantiated.add(cls)
            cls._instance = super(Grammar, cls).__new__(cls)

        return cls._instance

    def __init__(self: Grammar, delimiter: str = ' ') -> None:
        self._delimiter = delimiter

    @abstractmethod
    def root(self: Grammar) -> bool:
        pass

    @abstractmethod
    def terminal(self: Grammar) -> bool:
        pass

    @abstractmethod
    def token(self: Grammar) -> str:
        return self.token_name()

    @abstractmethod
    def token_name(self: Grammar) -> str:
        return "line"

    @abstractmethod
    def token_from(self: Grammar) -> str:
        pass

    #@abstractmethod # Move this and terminal method into a terminal class
    def token_terminal(self: Grammar) -> str:
        pass
