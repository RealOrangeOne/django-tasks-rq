# Recipes
@default:
  just --list

test *ARGS:
    ./manage.py makemigrations --check --noinput
    coverage run --source=django_tasks_rq manage.py test {{ ARGS }}
    coverage report
    coverage html

format:
    ruff check django_tasks_rq tests --fix
    ruff format django_tasks_rq tests

lint:
    ruff check django_tasks_rq tests
    ruff format django_tasks_rq tests --check
    mypy django_tasks_rq tests
