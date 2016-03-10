from external.ply_exec.parser import ScriptParser


def make_task(script):
    task = ScriptParser().parse(open(script).read())
    return task
