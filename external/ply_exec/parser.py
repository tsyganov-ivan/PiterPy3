from model import Task, Rule

from ply import lex, yacc

from collections import namedtuple


simple_token = namedtuple(
    'task_token',
    ['Name', 'Value']
)


class ScriptParser:
    keywords = ('WITH', 'IN', 'SET')
    tokens = keywords + ('EQUALS', 'VALUE', 'ATTRIBUTE')

    t_ignore = ' \t\n'
    t_EQUALS = r'='
    t_VALUE = r'\".*?\"'

    def t_ATTRIBUTE(self, t):
        r'[A-Za-z][A-Za-z0-9]*'
        if t.value in self.keywords:
            t.type = t.value
        return t

    def p_task(self, p):
        '''task : with in rule_list
                | in rule_list'''
        if len(p) == 4:
            _, file_mask, root_dir, rules = p
        else:
            _, root_dir, rules = p
            file_mask = None

        task = Task(root_dir, file_mask)
        for rule in rules:
            task.add_rule(rule)

        p[0] = task

    def p_with(self, p):
        '''with : WITH VALUE'''
        p[0] = p[2][1:-1]

    def p_in(self, p):
        '''in : IN VALUE'''
        p[0] = p[2][1:-1]

    def p_rule_list(self, p):
        '''rule_list : rule_list rule
                     | rule'''
        if isinstance(p[1], list):
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]

    def p_rule(self, p):
        '''rule : SET ATTRIBUTE EQUALS VALUE'''
        _, _, attribute, _, value = p
        p[0] = Rule(**{attribute: value[1:-1]})

    def __init__(self, debug=False):
        self._debug = debug
        self._lexer = lex.lex(module=self, debug=debug)
        self._parser = yacc.yacc(module=self, debug=debug, write_tables=0)

    def parse(self, data):
        p = self._parser.parse(data, debug=self._debug)
        return p
