import logging

from libcloud.compute.providers import Provider

# General
SSH_KEY_PATH = ''

# After how many seconds server is considered stuck if it's still in the
# 'bootstrapping' or 'provisioning' state and should be deleted.
STUCK_SERVER_THRESHOLD = ''

# Redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

# Provider settings
PROVIDER = Provider.RACKSPACE
PROVIDER_CREDENTIALS = ('username', 'password')
PROVIDER_KWARGS = {}

# Logging
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s %(levelname)s - %(message)s'

try:
    from local_settings import *
except:
    print 'ERROR: Failed to import local settings!'
    import traceback
    import sys
    traceback.print_stack()
    sys.exit(1)
