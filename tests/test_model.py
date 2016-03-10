import pytest

from model import Task, Rule


def test_rule_init():
    rule = Rule(Artist='Metallica')
    assert rule.update == dict(Artist='Metallica')


def test_rule_process(capsys):
    rule = Rule(Artist='Metallica')
    rule.process('some.mp3')
    out, err = capsys.readouterr()
    assert out == 'Update some.mp3. Set Artist to Metallica\n'


def test_task_init():
    task = Task(root_dir='./', file_mask='.*')
    assert task.root_dir == './'
    assert task.file_mask == '.*'


def test_task_setters():
    task = Task()
    task.set_mask('.*')
    assert task.file_mask == '.*'
    task.set_root_dir('./')
    assert task.root_dir == './'


def test_task_default_mask():
    task = Task('./')
    assert task.file_mask == '.*'
    task.set_mask(None)
    assert task.file_mask == '.*'


def test_task_add_rule():
    task = Task('./')
    rule = Rule(Artist='Metallica')
    task.add_rule(rule)
    assert len(task.rules) == 1
    assert task.rules[0] == rule


def test_task_process_rule(capsys):
    task = Task('./tests/music', '.*\.mp3')
    rule = Rule(Artist='Metallica')
    task.add_rule(rule)
    task.process_rules()
    out, err = capsys.readouterr()
    assert out == 'Update some.mp3. Set Artist to Metallica\n'
