from model import Task, Rule

ROOT_DIR = '../tests/music'
MASK = '.*\.mp3'
task = Task()
task.set_root_dir(ROOT_DIR)
task.set_mask(MASK)
task.add_rule(Rule(Artist='Metallica'))
task.add_rule(Rule(Genre='Rock'))
task.process_rules()
