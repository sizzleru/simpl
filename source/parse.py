#!/usr/bin/python

from __future__ import annotations

# Standard Library
import argparse
import sys
from pathlib import Path
from typing import List
from importlib import import_module
from os.path import basename, dirname
from typing import Tuple, Callable, Any

# Custom Library
from lark import Lark, Transformer, v_args
from lark.lexer import Token
from lark.tree import Tree
from typeguard import typechecked as strict

# Personal Library
from source.cfg import CFG
from source.module import load_module, load_modules, ModulePath


@strict
def generate_parser(modules):
    final_CFG = "line:command\"\\n\"line?\n"

    modules.sort(key=lambda module: module.token_from())
    seen_modules = set(['line'])

    for module in modules:
        if module.terminal():
            final_CFG += module.token_name() + ":" + module.token_terminal() + "\n"
        if not module.token_from() in seen_modules:
            final_CFG += module.token_from() + ":" + module.token() + "\n"
            seen_modules.add(module.token_from())
        else:
            final_CFG += "|" + module.token() + "\n"

    #print(final_CFG)

    return Lark(final_CFG, start="line")

@v_args(inline=True)
@strict
class SiMPLTransformer(Transformer):

    def __init__(self: SiMPLTransformer, modules: List[CFG] = []) -> None:
        self._modules = modules

    def module(self: Transformer, token: Token):
        self._modules += load_modules(ModulePath(token))

    def integer(self: Transformer, token: Token):
        print(token)
    #def load(self: Transformer, token: Token):
        #self._modules += load_modules(Path(token))

    #def printable(self: Transformer, token: Token):
    #    print(token)
    #    #print(str(token))

    #def command(self, tree: Any):
    #    print(type(tree))
    #    pass

    #def line(self, *tree: Any):
    #    pass
    #    #print(tree)

