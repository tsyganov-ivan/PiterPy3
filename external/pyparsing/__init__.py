from model import Task, Rule
from external.pyparsing.parser import script_parser


def make_task(script):
    parsed_script = script_parser.parseString(open(script).read())
    data = parsed_script and parsed_script[0] or {}
    task = Task(root_dir=data['root_dir'], file_mask=data.get('mask'))
    for rule in data['rules']:
        task.add_rule(Rule(**rule))

    return task
