#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

class Cache:
    '''
        Cache class.
    '''
    def __init__(self):
        '''
            Initialize the cache.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            Store data in the cache.
        '''
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey
