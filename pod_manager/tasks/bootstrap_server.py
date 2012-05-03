import logging

from celery.task import task
from libcloud.compute.base import NodeImage, NodeSize
from libcloud.compute.deployment import SSHKeyDeployment

from pod_manager.settings import PROVIDER
from pod_manager.utils import get_logger, get_driver, get_random_string
from pod_manager.db import get_client, cache_object, get_object
from pod_manager.settings import SSH_KEY_PATH
from pod_manager.models import server

logger = get_logger('pod_manager.tasks.server')

@task(ignore_result=True, time_limit=500)
def bootstrap(label, pod, pod_member, service_type):
    client = get_client()
    driver = get_driver()

    name = 'pod-%s-member-%s' % (pod['label'], pod_member['id'])
    metadata = {'pod_id': pod['id'], 'pod_member_id': pod_member['id']}

    image_id = service_type['server_image_id']
    size_id = service_type['server_size_id']

    image_ids = get_object(client, 'cache:image_ids')
    size_ids = get_object(client, 'cache:size_ids')

    if not image_ids:
        images = driver.list_images()
        image_ids = [i.id for i in images]
        cache_object(client, 'cache:image_ids', image_ids, 500)

    if not size_ids:
        sizes = driver.list_sizes()
        size_ids = [s.id for s in sizes]
        cache_object(client, 'cache:size_ids', size_ids, 500)

    if not image_id in image_ids:
        logger.log(logging.ERROR, 'Image with id %s doesn\'t exist' % (image_id))
        return

    if not size_id in size_ids:
        logger.log(logging.ERROR, 'Size with id %s doesn\'t exist' % (size_id))
        return

    image = NodeImage(image_id, None, None)
    size = NodeSize(size_id, None, None, None, None, None, None)

    with open(SSH_KEY_PATH, 'r') as fp:
        content = fp.read()

    sd = SSHKeyDeployment(content)

    server_id = get_random_string()

    server.update_server(server_id, {'name': name, 'provider': PROVIDER,
                                     'state': server.ServerState.BOOTSTRAPPING})

    logger.log(logging.DEBUG, 'Bootstrapping node (server_id=%s)...' %
               (server_id))

    try:
        node = driver.deploy_node(name=name, size=size, image=image, deploy=sd,
                                  ex_metadata=metadata)
    except Exception, e:
        logger.log(logging.ERROR, 'Failed to deploy node: %s' % (str(e)))
        return

    server.update_server(server_id, {'provider_id': node.id,
                                     'state': server.ServerState.BOOTSTRAPPED})
    logger.log(logging.DEBUG, 'Server successfully booted')
