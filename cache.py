import time
from typing import Any, Optional

class TTLCache:
    def __init__(self, ttl_seconds: float):
        self.ttl = ttl_seconds
        self.store = {}

    def set(self, key: str, value: Any):
        # BUG: Stores timestamp on set, but get() never validates expiration
        self.store[key] = {"value": value, "created_at": time.time()}

    def get(self, key: str) -> Optional[Any]:
        if key not in self.store:
            return None
        # BUG: Returns the value regardless of whether elapsed time exceeds ttl
        return self.store[key]["value"]

    def cleanup_expired(self) -> int:
        # BUG: Runtime error - deletes items while directly iterating the dict
        removed = 0
        now = time.time()
        for k, v in self.store.items():
            if now - v["created_at"] > self.ttl:
                del self.store[k]
                removed += 1
        return removed