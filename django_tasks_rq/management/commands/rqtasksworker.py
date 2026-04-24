from typing import Any

from django_rq.management.commands.rqworker import Command as RQWorkerCommand


class Command(RQWorkerCommand):
    help = (
        "Runs an RQ worker configured for django-tasks-rq. "
        "A thin wrapper around `rqworker` that defaults `--job-class` to "
        "`django_tasks_rq.Job`."
    )

    def handle(self, *args: Any, **options: Any) -> None:
        if not options.get("job_class"):
            options["job_class"] = "django_tasks_rq.Job"
        super().handle(*args, **options)  # type: ignore[no-untyped-call]
