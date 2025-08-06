import redis
from .base import BaseCache
from config import Config

class RedisCache(BaseCache):
    def __init__(self):
        self.client = redis.Redis.from_url(Config.REDIS_URL)

    def set(self, key, value, expire=3600):
        self.client.set(name=key, value=value, ex=expire)

    def get(self, key):
        return self.client.get(key)

    def delete(self, key):
        self.client.delete(key)

    def clear(self):
        self.client.flushdb()
