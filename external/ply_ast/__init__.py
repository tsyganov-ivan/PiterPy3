from model import Task, Rule
from external.ply_ast.parser import ScriptParser


def walk_ast(ast, task):
    for token in ast:
        if token.Name == 'RULE_LIST':
            walk_ast(token.Value, task)
        elif token.Name == 'IN':
            task.set_root_dir(token.Value)
        elif token.Name == 'WITH':
            task.set_mask(token.Value)
        elif token.Name == 'SET':
            task.add_rule(Rule(**dict([token.Value])))

def make_task(script):
    parser = ScriptParser()
    tokens = parser.parse(open(script).read())

    task = Task()
    walk_ast(tokens.Value, task)
    return task
