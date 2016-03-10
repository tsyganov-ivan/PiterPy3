import sys


def test_replace_finder():
    import internal.import_parser

    assert sys.meta_path[-1] is internal.import_parser.FSScriptFinder


def test_loader():
    import internal.import_parser

    import examples.internal_data.script as script

    script.task.process_rules()
    assert script.task.root_dir == '../tests/music/'
    assert script.task.file_mask == '.*\.mp3'
    assert len(script.task.rules) == 2
    assert script.task.rules[0].update == dict(Artist='Metallica')
