#!/usr/bin/python

from __future__ import annotations

# Builtin imports
from abc import ABC, abstractmethod
from typing import Optional, List

# Custom imports
from typeguard import typechecked as strict
from lark.lexer import Token

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

    #def parse(self: CFG, arg: Token) -> Token:
    #def parse(self: CFG, arg: List[Token]) -> List[Token]:
    def parse(self: CFG, args: List[Token]) -> Token:
        value=args[0]
        print(value)
        return value.update(type=int, value=0)
        #print(list(map(lambda token: token.update(type=int, value=0), arg)))
        #print("arg: ", arg)
        #print("type(arg): ", type(arg))
        #print("dir(arg): ", dir(arg))
        #exit(0)
        #return map(lambda token: token.update(type=int, value=0), arg)
        #for command in arg:
        #    print(dir(command))
        #    exit(0)
        #    print(command)
        ##return arg.update(value=0, type=int) # Should return a Exit status (class)
        #print('here: ', arg)
        #return [Token(type=int, value=0) for _ in arg]
