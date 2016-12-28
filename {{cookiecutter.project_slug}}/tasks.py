from invoke import task


@task
def compile(ctx, env='local'):
    """Compile *.in dependencies to *.txt file"""
    ctx.run(f'pip-compile requirements/{env}.in')


@task
def install(ctx, env='local'):
    """Install dependencies from *.txt file"""
    ctx.run(f'pip install -r requirements/{env}.txt')


@task
def start_db(ctx, daemon=False):
    """Start postgres container"""
    d = '-d' if daemon else ''
    ctx.run(f'docker-compose up {d} postgres')


@task
def stop_db(ctx):
    """Stop postgres container"""
    ctx.run('docker-compose stop postgres')
