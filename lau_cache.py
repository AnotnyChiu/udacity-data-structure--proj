# implement use doubly linked list and a hashmap

# doubly linked list node
class Node:
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value
        self.next = None
        self.pre = None

class LRU_Cache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {} # map key to nodes

        # dummy nodes for head and tail,
        # to tell the least and most recent visited node
        # left = LAU , right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.pre = self.right, self.left
    
    # helper functions: remove and add node to linked list (pointer function)
    def _remove(self, node: Node):
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

    def _add_to_right(self, node: Node):
        tail = self.right.pre
        self.right.pre = node
        tail.next = node
        node.pre = tail
        node.next = self.right

    def get(self, key):
        # cache hit
        if key in self.cache:
            # update linked list
            self._remove(self.cache[key])
            self._add_to_right(self.cache[key])
            return self.cache[key].value
        # cache miss
        return -1
    
    def set(self, key, value):
        # if key exist, update the value and set visited
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._add_to_right(self.cache[key])

        # check if over capacity
        if len(self.cache) > self.capacity:
            # remove LAU node from linked list
            lau = self.left.next
            self._remove(lau)
            del self.cache[lau.key]

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))       # returns -1 because 9 is not present in the cache
print(our_cache.get(4))

our_cache.set(5, 5)    
our_cache.set(6, 6)
our_cache.set(8, 8)

print(our_cache.get(3))    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

