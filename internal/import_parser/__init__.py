import types
import os
import sys

from external.pyparsing import make_task
from importlib.abc import MetaPathFinder, Loader


class FSScriptLoader(Loader):
    def __init__(self, script_path):
        self.script_path = script_path

    def load_module(self, name):
        if name in sys.modules:
            return sys.modules[name]

        task = make_task(self.script_path)

        mod = types.ModuleType(name)
        mod.__loader__ = self
        mod.task = task

        sys.modules[name] = mod
        return mod


class FSScriptFinder(MetaPathFinder):
    @staticmethod
    def get_script_path(directory, name):
        script_path = os.path.join(directory, '{name}.fs'.format(name=name))
        if os.path.isfile(script_path):
            return script_path

    @classmethod
    def find_module(cls, name, path=None):
        for d in sys.path:
            script_path = FSScriptFinder.get_script_path(d, name)
            if script_path is not None:
                return FSScriptLoader(script_path)

        if path is not None:
            name = name.split('.')[-1]
            for d in path:
                script_path = FSScriptFinder.get_script_path(d, name)
                if script_path is not None:
                    return FSScriptLoader(script_path)


sys.meta_path.append(FSScriptFinder)
