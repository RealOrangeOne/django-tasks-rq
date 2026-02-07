# Django Tasks RQ

[![CI](https://github.com/RealOrangeOne/django-tasks-rq/actions/workflows/ci.yml/badge.svg)](https://github.com/RealOrangeOne/django-tasks-rq/actions/workflows/ci.yml)
![PyPI](https://img.shields.io/pypi/v/django-tasks-rq.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-tasks-rq.svg)
![PyPI - Status](https://img.shields.io/pypi/status/django-tasks-rq.svg)
![PyPI - License](https://img.shields.io/pypi/l/django-tasks-rq.svg)


A [Django Tasks](https://docs.djangoproject.com/en/stable/topics/tasks/) backend which uses RQ as its underlying queue.

## Installation

```
python -m pip install django-tasks-rq
```

First, add `django_tasks_rq` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "django_tasks_rq",
]
```

Finally, add it to your `TASKS` configuration:

```python
TASKS = {
    "default": {
        "BACKEND": "django_tasks_rq.RQBackend",
        "QUEUES": ["default"]
    }
}
```

## Usage

The RQ-based backend acts as an interface between [Django's tasks interface](https://docs.djangoproject.com/en/stable/topics/tasks/) and `RQ`, allowing tasks to be defined and enqueued using `django.tasks`, but stored in Redis and executed using RQ's workers.

Any queues defined in `QUEUES` must also be defined in `django-rq`'s `RQ_QUEUES` setting.

### Job class

To use `rq` with `django-tasks-rq`, a custom `Job` class must be used. This can be passed to the worker using `--job-class`:

```shell
./manage.py rqworker --job-class django_tasks_rq.Job
```

### Priorities

`rq` has no native concept of priorities - instead relying on workers to define which queues they should pop tasks from in order. Therefore, `task.priority` has little effect on execution priority.

If a task has a priority of `100`, it is enqueued at the top of the queue, and will be the next task executed by a worker. All other priorities will enqueue the task to the back of the queue. The queue value is not stored, and will always be `0`.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for information on how to contribute.

Note: Prior to `0.12.0`, this backend was included in [`django-tasks`](https://github.com/RealOrangeOne/django-tasks/). Whilst the commit history was cleaned up, it's still quite messy. Don't look too closely.
