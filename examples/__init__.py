def create_task():
    yield from [
        (tokenize.NAME, 'from'),
        (tokenize.NAME, 'model'),
        (tokenize.NAME, 'import'),
        (tokenize.NAME, 'Task'),
        (tokenize.OP, ','),
        (tokenize.NAME, 'Rule'),
        (tokenize.NEWLINE, '\n'),
        (tokenize.NAME, 'task'),
        (tokenize.OP, '='),
        (tokenize.NAME, 'Task'),
        (tokenize.OP, '('),
        (tokenize.OP, ')'),
        (tokenize.NEWLINE, '\n')
    ]
