import os

class Config:
    CACHE_BACKEND = os.getenv("CACHE_BACKEND", "redis")  # Options: redis, memcached
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    MEMCACHED_HOST = os.getenv("MEMCACHED_HOST", "localhost")
    MEMCACHED_PORT = int(os.getenv("MEMCACHED_PORT", 11211))
