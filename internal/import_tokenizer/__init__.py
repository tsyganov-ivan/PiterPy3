import sys
from importlib.machinery import SourceFileLoader
from importlib.abc import MetaPathFinder
import tokenize


def get_token_value(token):
    _, value, *_ = token
    return value


def create_task():
    yield from [
        (tokenize.NAME, 'from'),
        (tokenize.NAME, 'model'),
        (tokenize.NAME, 'import'),
        (tokenize.NAME, 'Task'),
        (tokenize.OP, ','),
        (tokenize.NAME, 'Rule'),
        (tokenize.NEWLINE, '\n'),
        (tokenize.NAME, 'task'),
        (tokenize.OP, '='),
        (tokenize.NAME, 'Task'),
        (tokenize.OP, '('),
        (tokenize.OP, ')'),
        (tokenize.NEWLINE, '\n')
    ]


def set_mask(token):
    yield from [
        (tokenize.NAME, 'task'),
        (tokenize.OP, '.'),
        (tokenize.NAME, 'set_mask'),
        (tokenize.OP, '('),
        (tokenize.STRING, get_token_value(token)),
        (tokenize.OP, ')'),
        (tokenize.NEWLINE, '\n')
    ]


def set_root(token):
    yield from [
        (tokenize.NAME, 'task'),
        (tokenize.OP, '.'),
        (tokenize.NAME, 'set_root_dir'),
        (tokenize.OP, '('),
        (tokenize.STRING, get_token_value(token)),
        (tokenize.OP, ')'),
        (tokenize.NEWLINE, '\n')
    ]


def create_rule(key_token, value_token):
    yield from [
        (tokenize.NAME, 'task'),
        (tokenize.OP, '.'),
        (tokenize.NAME, 'add_rule'),
        (tokenize.OP, '('),
        (tokenize.NAME, 'Rule'),
        (tokenize.OP, '('),
        (tokenize.NAME, get_token_value(key_token)),
        (tokenize.OP, '='),
        (tokenize.STRING, get_token_value(value_token)),
        (tokenize.OP, ')'),
        (tokenize.OP, ')'),
        (tokenize.NEWLINE, '\n')
    ]


def translate(path):
    tokens = tokenize.generate_tokens(open(path).readline)
    task_created = False
    while tokens:
        current_token, *tokens = tokens
        tok_type, value, *_ = current_token
        if tok_type == tokenize.NAME and \
                        value in ('IN', 'WITH'):
            if not task_created:
                yield from create_task()
                task_created = True
            value_token, *tokens = tokens
            if value == 'IN':
                yield from set_root(value_token)
            elif value == 'WITH':
                yield from set_mask(value_token)
        elif tok_type == tokenize.NAME and value == 'SET':
            attribute_token, equal_token, value_token, *tokens = tokens
            yield from create_rule(attribute_token, value_token)
        else:
            yield (tok_type, value)


class MyLoader(SourceFileLoader):
    def source_to_code(self, data, path, *, _optimize=-1):
        patched_source = tokenize.untokenize(translate(path))
        return compile(
            patched_source,
            path,
            'exec',
            dont_inherit=True,
            optimize=_optimize
        )


_real_pathfinder = next((
    item
    for item in sys.meta_path
    if getattr(item, '__name__', None) == 'PathFinder'
), None)


class MyFinder(MetaPathFinder):
    @classmethod
    def find_module(cls, fullname, path=None):
        spec = _real_pathfinder.find_spec(fullname, path)
        loader = spec.loader
        loader.__class__ = MyLoader
        return loader


sys.meta_path[sys.meta_path.index(_real_pathfinder)] = MyFinder
