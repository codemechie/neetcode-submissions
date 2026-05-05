class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1 # or raise an exception
        current = self.head
        for i in range(index): # Changed from index-1
            current = current.next
        return current.data
    
    def insertHead(self, val: int) -> None:
        new_node = Node(val) # Create a Node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        if index == 0: # Handle head removal
            self.head = self.head.next
        else:
            prev = None
            current = self.head
            for i in range(index):
                prev = current
                current = current.next
            prev.next = current.next
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        current = self.head
        while current:
            result.append(current.data) # Append the data, not the node
            current = current.next
        return result   