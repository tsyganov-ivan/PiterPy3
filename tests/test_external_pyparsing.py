import pytest

from external.pyparsing.parser import script_parser
from external.pyparsing import make_task


def test_parse():
    correct_string = '''
        WITH ".*\.mp3"
        IN "./tests/music"
        SET Artist="Metallica"
        SET Genre="Rock"
    '''
    parsed_data = script_parser.parseString(correct_string)[0]
    assert parsed_data['root_dir'] == './tests/music'
    assert parsed_data['mask'] == '.*\\.mp3'
    assert parsed_data['rules'][0] == {'Artist': 'Metallica'}
    assert parsed_data['rules'][1] == {'Genre': 'Rock'}


def test_make_task():
    task = make_task('./tests/scripts/script.fs')
    assert task.root_dir == './tests/music'
    assert task.file_mask == '.*\.mp3'
    assert len(task.rules) == 2
    assert task.rules[0].update == dict(Artist='Metallica')
