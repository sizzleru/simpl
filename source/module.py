#!/usr/bin/python

from __future__ import annotations

# Standard Library
from pathlib import Path
from typing import List, Any
from importlib import import_module
from os.path import basename, dirname
from typing import Tuple, Callable, Any, TYPE_CHECKING
import sys

# Custom Library
from lark import Lark, Transformer, v_args
from lark.lexer import Token
from lark.tree import Tree
from typeguard import typechecked as strict

# Personal Library
from source.cfg import CFG
if TYPE_CHECKING:
    from source.module import ModulePath

@strict
def load_module(module_path: ModulePath) -> CFG:
    module_name = (dirname(module_path.path()) + '/' + module_path.path().stem).replace("/",".")
    return (import_module(module_name).Module)()

@strict
def load_modules(terminal_module_path: ModulePath) -> List[CFG]:
    module = load_module(terminal_module_path)
    modules = []

    if not module.token:
        raise NotImplementedError # For now can't import non-terminal modules (later can do it but will need a check to verify its closed off)

    while not module._parent is CFG:
        modules.append(module)
        module = module._parent()

    return modules

@strict
class ModulePath:

    def _parse_dir(self: ModulePath, path: str) -> Tuple[str,str]:
        parsed_dir = path.split('/', 1)
        return parsed_dir[0], parsed_dir[1] if len(parsed_dir) == 2 else ""

    def __init__(self: ModulePath, import_path: str) -> None:

        # Root module path
        path = Path('module')
        next_item, import_path = self._parse_dir(import_path)

        # Repository folder
        if (path / next_item).is_dir():
            path /= next_item
            next_item, import_path = self._parse_dir(import_path)
        elif (path / 'base' / next_item).is_dir():
            path /= 'base'
        else:
            raise ValueError("Invalid repository import path")

        # Type folder
        if (path / next_item).is_dir():
            path /= next_item
            next_item, import_path = self._parse_dir(import_path)
        elif next_item == "*":
            raise NotImplementedError
        else:
            raise ValueError("Invalid type import path")

        # Field folder
        if (path / next_item).is_dir():
            path /= next_item
            next_item, import_path = self._parse_dir(import_path)
        elif next_item == "*":
            raise NotImplementedError
        else:
            raise ValueError("Invalid field import path")

        # Object folder
        if (path / next_item).is_dir():
            path /= next_item
            next_item, import_path = self._parse_dir(import_path)
        elif next_item == "*":
            raise NotImplementedError
        else:
            raise ValueError("Invalid object import path")

        # Implementation folder
        if next_item == "" and (path / 'default').is_dir():
            path /= 'default'
        elif (path / next_item).is_dir():
            path /= next_item
            next_item, import_path = self._parse_dir(import_path)
        else:
            raise ValueError("Invalid implementation import path")

        #print(path, '<-', next_item, '<-', import_path)

        # Version folder
        if next_item == "" and (path / 'latest.py').is_file():
            path /= 'latest.py'
        elif (path / (next_item + '.py')).is_file():
            path /= (next_item + '.py')
        else:
            raise ValueError("Invalid version import path")

        self._path = path

    def path(self: ModulePath) -> Path:
        return self._path
