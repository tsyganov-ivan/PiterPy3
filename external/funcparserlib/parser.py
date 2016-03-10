from funcparserlib.lexer import make_tokenizer
from funcparserlib.parser import some, many, skip, maybe

from model import Task, Rule


def tokenize(str):
    specs = [
        ('With', (r'WITH',)),
        ('In', (r'IN',)),
        ('Set', (r'SET',)),
        ('Equals', (r'=',)),
        ('Space', (r'[ \t\r\n]+',)),
        ('Value', (r'\".*?\"',)),
        ('Attribute', (r'[A-Za-z][A-Za-z0-9]*',)),
    ]
    useless = ['Space']
    return list(
        filter(
            lambda x: x.type not in useless,
            make_tokenizer(specs)(str)
        )
    )


def parse(source):
    task = Task()

    get_value = lambda x: x.value
    value_of = lambda t: some(lambda x: x.type == t) >> get_value

    keyword = lambda s: skip(value_of(s))
    make_rule = lambda x: task.add_rule(Rule(**{x[0]: x[1][1:-1]}))
    set_root = lambda value: task.set_root_dir(value[1:-1])
    set_mask = lambda value: task.set_mask(value[1:-1])

    root = keyword('In') + value_of('Value') >> set_root
    mask = keyword('With') + value_of('Value') >> set_mask
    rule = keyword('Set') + \
           value_of('Attribute') + \
           keyword('Equals') + \
           value_of('Value') \
           >> make_rule
    parser = maybe(mask) + root + many(rule)
    parser.parse(source)
    return task



