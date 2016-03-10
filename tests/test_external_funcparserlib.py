import pytest

from external.funcparserlib import make_task
from external.funcparserlib.parser import tokenize, parse
from funcparserlib.lexer import Token, LexerError


def test_tokenize():
    correct_string = '''
        WITH ".*\.mp3"
        IN "./tests/music"
        SET Artist="Metallica"
        SET Genre="Rock"
    '''
    tokens = tokenize(correct_string)
    assert tokens == [
        Token('With', 'WITH'),
        Token('Value', '".*\\.mp3"'),
        Token('In', 'IN'),
        Token('Value', '"./tests/music"'),
        Token('Set', 'SET'),
        Token('Attribute', 'Artist'),
        Token('Equals', '='),
        Token('Value', '"Metallica"'),
        Token('Set', 'SET'),
        Token('Attribute', 'Genre'),
        Token('Equals', '='),
        Token('Value', '"Rock"')
    ]


def test_incorrect_tokenize():
    incorrect_string = '''
        WITH .*\.mp3
    '''
    with pytest.raises(LexerError) as e:
        tokenize(incorrect_string)

    assert 'cannot tokenize data: 2,14:' in str(e.value)


def test_parse():
    correct_string = '''
        WITH ".*\.mp3"
        IN "./tests/music"
        SET Artist="Metallica"
        SET Genre="Rock"
    '''
    task = parse(tokenize(correct_string))
    assert task.root_dir == './tests/music'
    assert task.file_mask == '.*\.mp3'
    assert len(task.rules) == 2
    assert task.rules[0].update == dict(Artist='Metallica')


def test_make_task():
    task = make_task('./tests/scripts/script.fs')
    assert task.root_dir == './tests/music'
    assert task.file_mask == '.*\.mp3'
    assert len(task.rules) == 2
    assert task.rules[0].update == dict(Artist='Metallica')
