#'!/usr/bin/python

from __future__ import annotations

# Standard Library
import argparse
from sys import exit
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

    final_CFG = ""
    modules.sort(key=lambda module: module._parent().name)
    seen_modules = set()

    for module in modules:
        if module.token:
            final_CFG += module.name + ":/" + module.token + "/\n"

        if module._parent().name in seen_modules:
            final_CFG += "|" + module.rule_parent(module) + "\n"
        else:
            final_CFG += module._parent().name + ":" + module.rule_parent(module) + "\n"
            seen_modules.add(module._parent().name)

    #print(final_CFG)
    #exit(0)

    return Lark(final_CFG, start="line")

@v_args(inline=True)
@strict
class SiMPLTransformer(Transformer):

    def __init__(self: SiMPLTransformer, modules: List[CFG] = []) -> None:
        self._modules = modules

    def module(self: Transformer, token: Token):
        self._modules += load_modules(ModulePath(token))

        # Probably need to move to load_modules
        for module in self._modules:
            self.__dict__[module.name]=module.parse

        #print((self.__dict__['natural'](Token(int,3))).value._value)
        #sys.exit(0)
        #print(self.__dict__)


        #self.__dict__['test']=lambda x: print('Hello' + str(x))
        #print(self.__dict__)
        #for module in self._modules:
        #    #print(Token(int,3))

        #    try:
        #        pass
        #        print(module.parse(Token(int,3)))
        #        #print(module)
        #        #print(module.parse)
        #        #print(type(module.transform(Token(str,3))))
        #    except:
        #        pass
        #sys.exit(0)

    #def natural(self: Transformer, token: Token):
    #    Natural

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

