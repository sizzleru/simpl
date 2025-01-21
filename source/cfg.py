#!/usr/bin/python

from __future__ import annotations
# Builtin imports
from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Optional

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token

# Personal imports

@strict
class CFG(ABC):

    _instantiated = set()
    _instance = None

    # This shit show is to essentially produce singleton classes
    # of which subclasses also become singleton
    def __new__(cls):
        cls._parent = cls.__bases__[0]

        if not cls in cls._instantiated:
            cls._instantiated.add(cls)
            cls._instance = super(CFG, cls).__new__(cls)

        return cls._instance

    def __init__(self: CFG, delimiter: str = ' ') -> None:
        self._delimiter = delimiter

    # The name of the class (specifically used as the grammar)
    # This should be referenced in rule instead of hardcoding where possible
    @property
    @abstractmethod
    def name(self: CFG) -> str:
        pass

    # Gives the token to accept as this property type (regex)
    # None if doesn't get parsed as a value
    @property
    @abstractmethod
    def token(self: CFG) -> Optional[str]:
        pass

    # Gives the form to parse from parent classes
    # Will also be used by child classes to form grammars
    # Returns none if it has a token attribute
    @abstractmethod
    def rule(self: CFG, *args: CFG) -> Optional[str]:
        pass

    # Inherited function, should provide the rule form
    # of the parent class
    def rule_parent(self: CFG, *args: CFG) -> Optional[str]:
        if self._parent is CFG:
            raise ValueError("rule_parent can not be used for root module")
        else:
            return self._parent().rule(*args)

    # Parse the token from the Abstract Syntax Tree
    @abstractmethod
    def parse(self: CFG, *args: Token) -> Token:
        pass

    # For debugging and printing purposes
    def __str__(self: CFG) -> str:
        return f'Grammar <name: {str(self.name)}, token: {str(self.token)}>'
