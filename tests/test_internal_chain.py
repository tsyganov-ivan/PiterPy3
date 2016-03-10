import pytest

from internal.chain import FileUpdater


def test_path():
    updater = FileUpdater()
    assert updater == updater.path('./music')
    assert updater._path == './music'


def test_mask():
    updater = FileUpdater()
    assert updater == updater.mask('.*\.mp3')
    assert updater._mask == '.*\.mp3'


def test_set():
    updater = FileUpdater().path('./music').mask('.*\.mp3').set(
        Artist='Metallica')
    assert updater._task is not None
    assert len(updater._task.rules) > 0


def test_do(capsys):
    FileUpdater().path('./tests/music').mask('.*\.mp3').set(
        Artist='Metallica').do()
    out, err = capsys.readouterr()
    assert out == 'Update some.mp3. Set Artist to Metallica\n'
