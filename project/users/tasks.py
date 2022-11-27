"""Shared Tasks"""

from celery import shared_task


@shared_task
def celery_commit_all(tsg_id: str, client_id: str, client_secret: str, verify: bool = True):
    from project.sase_commit import commit_all
    response = commit_all(tsg_id=tsg_id, client_id=client_id,
                          client_secret=client_secret, verify=verify)
    return response
