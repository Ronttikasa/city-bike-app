from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/wsgi.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def robot(ctx):
    ctx.run("robot src/tests/robot/", pty=True)