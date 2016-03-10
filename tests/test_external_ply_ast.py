import pytest

from external.ply_ast import make_task
from external.ply_ast.parser import ScriptParser, simple_token



def test_parse():
    correct_string = '''
        WITH ".*\.mp3"
        IN "./tests/music"
        SET Artist="Metallica"
        SET Genre="Rock"
    '''
    parser = ScriptParser()
    tokens = parser.parse(correct_string)
    assert tokens == simple_token(
        Name='TASK',
        Value=[
            simple_token(Name='WITH', Value='.*\\.mp3'),
            simple_token(Name='IN', Value='./tests/music'),
            simple_token(Name='RULE_LIST', Value=[
                simple_token(Name='SET', Value=('Artist', 'Metallica')),
                simple_token(Name='SET', Value=('Genre', 'Rock'))
            ])
        ]
    )

def test_make_task():
    task = make_task('./tests/scripts/script.fs')
    assert task.root_dir == './tests/music'
    assert task.file_mask == '.*\.mp3'
    assert len(task.rules) == 2
    assert task.rules[0].update == dict(Artist='Metallica')
