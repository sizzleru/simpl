#!/usr/bin/python

from __future__ import annotations
# Builtin imports
from abc import ABC, abstractmethod
from typing import Any, Optional

# Custom imports
from typeguard import typechecked as strict

# Personal imports

@strict
class CFG(ABC):

    _instantiated = set()
    _instance = None

    def __new__(cls):
        cls._parent = cls.__bases__[0]

        if not cls in cls._instantiated:
            cls._instantiated.add(cls)
            cls._instance = super(CFG, cls).__new__(cls)

        return cls._instance

    def __init__(self: CFG, delimiter: str = ' ') -> None:
        self._delimiter = delimiter

    @abstractmethod
    def root(self: CFG) -> bool:
        pass

    @abstractmethod
    def terminal(self: CFG) -> bool:
        pass

    @abstractmethod
    def token(self: CFG) -> str:
        return self.token_name()

    @abstractmethod
    def token_name(self: CFG) -> str:
        return "line"

    @abstractmethod
    def token_from(self: CFG) -> str:
        pass

    #@abstractmethod # Move this and terminal method into a terminal class
    def token_terminal(self: CFG) -> str:
        pass
