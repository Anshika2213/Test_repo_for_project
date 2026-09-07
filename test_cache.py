import time
from cache import TTLCache

def test_cache_normal_retrieval():
    cache = TTLCache(ttl_seconds=1.0)
    cache.set("a", 100)
    assert cache.get("a") == 100

def test_cache_expiration():
    cache = TTLCache(ttl_seconds=0.1)
    cache.set("temp", "data")
    time.sleep(0.15)
    assert cache.get("temp") is None, "Expired key should return None"

def test_cleanup_expired_safely():
    cache = TTLCache(ttl_seconds=0.05)
    cache.set("k1", 1)
    cache.set("k2", 2)
    time.sleep(0.08)
    # Should not throw RuntimeError: dictionary changed size during iteration
    removed = cache.cleanup_expired()
    assert removed == 2
    assert len(cache.store) == 0