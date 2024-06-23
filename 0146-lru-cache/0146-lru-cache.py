class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache ={}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def add_node(self, node:Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_node(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            del self.cache[key]
            
        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            self.remove_node(lru_node)
            del self.cache[lru_node.key]
            
        new_node = Node(key,value)
        self.add_node(new_node)
        self.cache[key] = new_node
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)