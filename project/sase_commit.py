"""SASE Commit process"""
from prismasase.configs import Auth
from prismasase.config_mgmt import configuration


def commit_all(tsg_id: str, client_id: str, client_secret: str, verify: bool = True):
    auth = Auth(tsg_id=tsg_id,
                client_id=client_id,
                client_secret=client_secret,
                verify=verify)
    response = configuration.config_commit(
        folders=['Remote Networks', 'Service Connections'],
        description='automation test with celery', auth=auth)
    return response
