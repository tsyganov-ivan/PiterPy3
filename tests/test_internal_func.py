import pytest

from internal.func import settings, set, update


def test_settings():
    result = settings(path='./', mask='.*\.mp3')
    assert result.file_mask == '.*\.mp3'
    assert result.root_dir == './'


def test_set():
    result = set(Artist='Metallica')
    assert result.update == dict(Artist='Metallica')


def test_update(capsys):
    update(
        settings(
            path='./tests/music',
            mask='.*\.mp3'
        ),
        set(Artist='Metallica')
    )
    out, err = capsys.readouterr()
    assert out == 'Update some.mp3. Set Artist to Metallica\n'
