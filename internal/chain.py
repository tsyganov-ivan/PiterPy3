from model import Task, Rule


class FileUpdater:
    def __init__(self):
        self._path = None
        self._mask = None
        self._task = None

    def path(self, path):
        self._path = path
        return self

    def mask(self, mask):
        self._mask = mask
        return self

    def set(self, **kwargs):
        if not self._task:
            self._task = Task(root_dir=self._path, file_mask=self._mask)
        self._task.add_rule(Rule(**kwargs))
        return self

    def do(self):
        self._task.process_rules()

FileUpdater()\
    .path('\music')\
    .mask('.*metallica.*')\
    .set(Genre='Rock')\
    .set(Artist='Metallica')\
    .do()



