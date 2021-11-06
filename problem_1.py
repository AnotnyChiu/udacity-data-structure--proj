# problem 1: Least Recently Used Cache

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.access_order = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        # alert if None or null passed
        if key is None:
            print('Null value is not acceptable')
            return

        # if cache hit
        if key in self.dict:
            self.access_order.remove(key)
            self.access_order.append(key)
            print(self.access_order)
            return self.dict[key]
        # if cache miss
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # if the key aleady exist
        if key in self.dict:
            print(f'key {key} already exist')
            return
        
        # else, add new element to cache (and access order)
        self.access_order.append(key)
        self.size += 1

        # if over capacity, refresh cache
        if self.size > self.capacity:
            print(self.access_order)
            del self.dict[self.access_order[0]]
            self.access_order.pop(0)
            print(self.access_order)
            self.size -= 1

        # add the value after refresh
        self.dict[key] = value
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 'antony')

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))       # returns -1 because 9 is not present in the cache
print(our_cache.get(4))

our_cache.set(5, 5)           # aleert key already exist
our_cache.set(6, 6)
our_cache.set(8, 8)

print(our_cache.get(3))    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(5))    # returns -1 because the cache reached it's capacity and 5 was also removed
