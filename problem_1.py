# problem 1: Least Recently Used Cache

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = {}
        self.access_order = [i for i in range(capacity)]

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # if cache hit
        if key in self.dict:
            return dict[key]
        # if cache miss
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # if the key aleady exist
        if key in self.dict:
            print(f'key {key} already exist')
            return
        # if over capacity, refresh cache
        self.dict[key] = value
    
    def refresh_cache(self):
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
