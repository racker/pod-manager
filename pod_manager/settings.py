from libcloud.compute.providers import Provider

# Redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

# Provider settings
PROVIDER = Provider.RACKSPACE
PROVIDER_CREDENTIALS = ('username', 'password')

# Logging
LOG_FORMAT = '%(asctime)s %(levelname)s (%(ip)s - %(session_id)s) - %(message)s'

try:
    from local_settings import *
except:
    print 'ERROR: Failed to import local settings!'
    import traceback
    import sys
    traceback.print_stack()
    sys.exit(1)
