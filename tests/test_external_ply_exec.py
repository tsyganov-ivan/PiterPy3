import pytest

from external.ply_exec import make_task
from external.ply_exec.parser import ScriptParser


def test_parse():
    correct_string = '''
        WITH ".*\.mp3"
        IN "./tests/music"
        SET Artist="Metallica"
        SET Genre="Rock"
    '''
    parser = ScriptParser()
    task = parser.parse(correct_string)
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
