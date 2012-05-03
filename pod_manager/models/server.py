from pod_manager.db import get_client

class ServerState(object):
    BOOTSTRAPPING = 0
    BOOTSTRAPPED = 1
    PROVISIONING = 2
    AVAILABLE = 3
    DELETING = 4
    DELETED = 5

def update_server(server_id, attributes):
    hash_key = 'servers:%s' % (server_id)

    client = get_client()
    pipe = client.pipeline()

    for key, value in attributes.iteritems():
        pipe.hset(hash_key, key, value)

    pipe.execute()
