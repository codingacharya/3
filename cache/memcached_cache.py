from pymemcache.client import base
from .base import BaseCache
from config import Config

class MemcachedCache(BaseCache):
    def __init__(self):
        self.client = base.Client((Config.MEMCACHED_HOST, Config.MEMCACHED_PORT))

    def set(self, key, value, expire=3600):
        self.client.set(key, value, expire)

    def get(self, key):
        return self.client.get(key)

    def delete(self, key):
        self.client.delete(key)

    def clear(self):
        self.client.flush_all()
