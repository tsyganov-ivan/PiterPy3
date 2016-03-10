# import pytest
import sys


def test_loader():
    import internal.import_tokenizer
    import examples.internal_data.my_script as script

    assert script.task.root_dir == '../tests/music/'
    assert script.task.file_mask == '.*\.mp3'
    assert len(script.task.rules) == 2
    assert script.task.rules[0].update == dict(Artist='Metallica')


def test_replace_finder():
    import internal.import_tokenizer

    assert internal.import_tokenizer.MyFinder in sys.meta_path
