from external.funcparserlib.parser import parse, tokenize


def make_task(script):
    task = parse(tokenize(open(script).read()))
    return task
