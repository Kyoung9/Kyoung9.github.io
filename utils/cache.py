import time

class TTLCache:
    def __init__(self, ttl_seconds = 3600): # 1 hour
        self.ttl = ttl_seconds
        self.store = {}

    def get(self, key):
        item = self.store.get(key)
        if not item:
            return None
        expires_at, value = item
        if expires_at < time.time():
            self.store.pop(key, None)
            return None
        return value

    def set(self, key, value):
        self.store[key] = (time.time() + self.ttl, value)