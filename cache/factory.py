from config import Config
from .redis_cache import RedisCache
from .memcached_cache import MemcachedCache

def get_cache_backend():
    if Config.CACHE_BACKEND == 'redis':
        return RedisCache()
    elif Config.CACHE_BACKEND == 'memcached':
        return MemcachedCache()
    else:
        raise ValueError("Unsupported CACHE_BACKEND specified.")
