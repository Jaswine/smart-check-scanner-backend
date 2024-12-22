from typing import Any
from django.core.cache import cache


def get_cache(cache_key: str) -> Any | None:
    """
        Get a cache
        :param cache_key: str - Key of the cache
        :return: Any - Data from the cache
    """
    return cache.get(cache_key)

def set_cache(cache_key: str, data: Any, /, *, timeout: int = 600) -> None:
    """
    Set a cache
        :param cache_key: str - Key of the cache
        :param data: Any - Data to be stored in the cache
        :param timeout: int - Timeout for the cache in seconds (default 600 seconds)
        :return: None
    """
    cache.set(cache_key, data, timeout=timeout)

def delete_cache_by_key(cache_key: str) -> None:
    """
        Delete a cache by key.
        :param cache_key: str - Key of the cache to delete.
        :return: None
    """
    cache.delete(cache_key)


def delete_cache_by_pattern(pattern: str) -> None:
    """
        Delete all keys from cache that match the given pattern.
       :param pattern: str - Pattern to match cache keys.
       :return: None
    """
    pattern = f'{pattern}*'
    cache.delete_pattern(pattern)
