import pickle
import redis

from pod_manager.settings import REDIS_HOST, REDIS_PORT, REDIS_DB

__all__ = [
    'get_client',
    'cache_object',
    'get_object'
]

def get_client():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    return client

def cache_object(client, key, obj, ttl=60):
    pipe = client.pipeline()
    data = pickle.dumps(obj)
    pipe.set(key, data)

    if ttl:
        pipe.expire(key, ttl)

    pipe.execute()

def get_object(client, key):
    data = client.get(key)

    if not data:
        return None

    obj = pickle.loads(data)
    return obj
