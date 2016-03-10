from pyparsing import (
    Keyword, QuotedString, Word, alphanums, Optional, ZeroOrMore)

mask = Keyword('WITH') + QuotedString('"')('mask')
root_dir = Keyword('IN') + QuotedString('"')('root_dir')
rule = (
    Keyword('SET') +
    Word(alphanums)('key') +
    '=' +
    QuotedString('"')('value')
).setParseAction(lambda r: {r.key: r.value})

script_parser = (
    Optional(mask) +
    root_dir +
    Optional(mask) +
    ZeroOrMore(rule)('rules')
).setParseAction(lambda t: {
    'mask': t.mask,
    'root_dir': t.root_dir,
    'rules': t.rules
})
