import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IN_TEST = "IN_TEST" in os.environ or (len(sys.argv) > 1 and sys.argv[1] == "test")

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django_tasks_rq",
    "django_rq",
    "tests",
]

SECRET_KEY = "abcde12345"

USE_TZ = True

if not IN_TEST:
    DEBUG = True

TASKS = {
    "default": {
        "BACKEND": "django_tasks_rq.RQBackend",
        "QUEUES": ["default", "queue-1"],
    }
}

RQ_QUEUES = {
    "default": {
        "HOST": "localhost",
        "PORT": 6379,
    },
    "queue-1": {
        "HOST": "localhost",
        "PORT": 6379,
    },
}
