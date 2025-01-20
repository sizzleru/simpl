#!/usr/bin/python

from __future__ import annotations

# Standard Library
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

@strict
def load_module(module_path: Path) -> CFG:
    if not module_path.is_file():
        raise FileNotFoundError

    module_name = (dirname(module_path) + '/' + module_path.stem).replace("/",".")
    return (import_module(module_name).Module)()

@strict
def load_modules(terminal_module_path: Path) -> List[CFG]:
    module = load_module(terminal_module_path)
    modules = []
    if not module.terminal():
        raise NotImplementedError # For now can't import non-terminal modules (later can do it but will need a check to verify its closed off)
    while not module.root():
        modules.append(module)
        module = module._parent()

    return modules
