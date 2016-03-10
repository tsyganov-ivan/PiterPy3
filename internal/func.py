from model import Rule, Task

mask = path = lambda value: value

def settings(path, mask):
    return Task(root_dir=path, file_mask=mask)


def set(**kwargs):
    return Rule(**kwargs)


def update(task, *rules):
    for rule in rules:
        task.add_rule(rule)
    task.process_rules()

update(
    settings(
        path('./music'),
        mask('.*\.mp3')
    ),
    set(Artist='Metallica'),
    set(Genre='Rock')
)

update(
    settings(
        path='./music',
        mask='.*\.mp3'
    ),
    set(Artist='Metallica'),
    set(Genre='Rock')
)















