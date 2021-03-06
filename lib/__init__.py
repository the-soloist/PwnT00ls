from . import cache
from . import color
from . import convert
from . import debug
from . import logger
from . import config


def try_import(path, name):
    try:
        exec(f"from {path} import {name}")
    except Exception as e:
        print(f"cannot import lib.{name}, exception: {e}.")


try_import(".", "crypt")
try_import(".", "database")
try_import(".", "emu")
try_import(".", "encode")
try_import(".", "http")
try_import(".", "shellcode")


parser = config.init_parser()

del try_import


__all__ = [x for x in globals().keys() if x != '__name__']
