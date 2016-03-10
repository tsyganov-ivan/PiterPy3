from external.pyparsing import make_task

task = make_task('./external_data/script.txt')
task.process_rules()
