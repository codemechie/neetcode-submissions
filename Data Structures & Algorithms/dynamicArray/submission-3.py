class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity
    def get(self, i: int) -> int:
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self._size >= self._capacity:
            self.resize()
        self._array[self._size] = n
        self._size += 1 
        
        
    def popback(self) -> int:
        if self._size == 0:
            raise IndexError("Cannot remove from empty array")
        self._size -= 1
        value = self._array[self._size]
        self._array[self._size] = None
        return value

    def resize(self) -> None:
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        
    def getSize(self) -> int:
        return self._size
    def getCapacity(self) -> int:
        return self._capacity
