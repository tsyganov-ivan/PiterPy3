from ply import lex
from ply import yacc

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
        p[0] = simple_token(Name='TASK', Value=p[1:])

    def p_with(self, p):
        '''with : WITH VALUE'''
        p[0] = simple_token(Name='WITH', Value=p[2][1:-1])

    def p_in(self, p):
        '''in : IN VALUE'''
        p[0] = simple_token(Name='IN', Value=p[2][1:-1])

    def p_rule_list(self, p):
        '''rule_list : rule_list rule
                     | rule'''
        if p[1].Name == 'RULE_LIST':
            p[0] = simple_token(
                Name='RULE_LIST',
                Value=p[1].Value + [p[2]]
            )
        else:
            p[0] = simple_token(
                Name='RULE_LIST',
                Value=[p[1]]
            )

    def p_rule(self, p):
        '''rule : SET ATTRIBUTE EQUALS VALUE'''
        p[0] = simple_token(
            Name='SET',
            Value=(p[2], p[4][1:-1])
        )

    def __init__(self, debug=False):
        self._debug = debug
        self._lexer = lex.lex(module=self, debug=debug)
        self._parser = yacc.yacc(module=self, debug=debug, write_tables=0)

    def parse(self, data):
        return self._parser.parse(data, debug=self._debug)
