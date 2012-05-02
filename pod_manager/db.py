import redis

from pod_manager.settings import REDIS_HOST, REDIS_PORT, REDIS_DB

def get_client():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    return client
