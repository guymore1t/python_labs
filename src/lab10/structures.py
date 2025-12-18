from collections import deque

class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Пустой стек")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)

class Queue:
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Пустая очередь")
        return self._data.popleft()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)

if __name__ == "__main__":
    print("Тестирование Stack и Queue\n")
    
    print("1. Тест Stack:")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"  push(10,20,30)")
    print(f"  pop() = {s.pop()}")
    print(f"  peek() = {s.peek()}")
    print(f"  размер = {len(s)}")
    print(f"  пустой? {s.is_empty()}")
    
    print("\n2. Тест Queue:")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"  enqueue(A,B,C)")
    print(f"  dequeue() = {q.dequeue()}")
    print(f"  peek() = {q.peek()}")
    print(f"  размер = {len(q)}")
    print(f"  пустая? {q.is_empty()}")
