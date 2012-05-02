import logging

from celery.task import task

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from pod_manager.settings import PROVIDER, PROVIDER_CREDENTIALS
from pod_manager.utils import get_logger

logger = get_logger('pod_manager.tasks.server')

@task
def bootstrap():
    cls = get_driver(PROVIDER)
    driver = cls(*PROVIDER_CREDENTIALS)
    name = 'pod-%s-%s' % (label, id)

    # TODO insert server into servers

    try:
        node = driver.deploy_node(name=name, size=size, image=image)
    except Exception, e:
        logger.log(logging.ERROR, 'Failed to deploy node: %s' % (str(e)))

    logget.log(logging.DEBUG, 'Server successfully booted', extra=node.__dict__)

    # TODO change server status to available
