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
from source.module import load_module, load_modules

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
        self._modules += load_modules(Path(token))

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

if __name__ == "__main__":

    # Allow module imports
    initial_module = Path('module/default/system/module/base/v0_0_1.py')
    modules = load_modules(initial_module)
    transformer = SiMPLTransformer(modules)
    parser = generate_parser(modules)

    if (input_file := arg_parser.parse_args().file) != "":
        file_contents = []
        file_segment = ""

        file = open(input_file, "r")
        for line in file:
            if line.split(' ')[0] == 'load':
                if file_segment != "":
                    file_contents.append(file_segment)
                file_segment = ""
                file_contents.append(line)
            else:
                file_segment += line
        if file_segment != "":
            file_contents.append(file_segment)

        for file_segment in file_contents:
            tree = parser.parse(file_segment)
            #print(tree.pretty())
            leftover = transformer.transform(tree)
            parser = generate_parser(modules)
    else:
        raise NotImplementedError

