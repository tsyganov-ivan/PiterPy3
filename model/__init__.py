import re
import os


class Rule:
    def __init__(self, **kwargs):
        self.update = kwargs

    def process(self, filename):
        for key, value in self.update.items():
            print('Update {}. Set {} to {}'.format(filename, key, value))


class Task:
    def __init__(self, root_dir=None, file_mask=None):
        self.root_dir = root_dir
        self.file_mask = file_mask or '.*'
        self.rules = list()

    def set_root_dir(self, value):
        self.root_dir = value

    def set_mask(self, value):
        self.file_mask = value or '.*'

    def add_rule(self, rule):
        self.rules.append(rule)

    def files(self):
        for *_, files_list in os.walk(self.root_dir):
            for filename in files_list:
                if not re.match(self.file_mask, filename):
                    continue
                yield filename

    def process_rules(self):
        for filename in self.files():
            for rule in self.rules:
                rule.process(filename)
