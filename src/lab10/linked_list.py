class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1
    
    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError("Неправильный индекс")
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next
            new_node = Node(value, current.next)
            current.next = new_node
            self._size += 1
    
    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError("Неправильный индекс")
        if idx == 0:
            removed = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next
            removed = current.next
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        self._size -= 1
        return removed.value
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"LinkedList({list(self)})"

if __name__ == "__main__":
    print("Тестирование SinglyLinkedList\n")
    
    print("1. Тест SinglyLinkedList:")
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    lst.prepend(5)
    lst.insert(2, 15)
    print(f"  append(10,20,30), prepend(5), insert(2,15)")
    print(f"  список: {lst}")
    print(f"  размер: {len(lst)}")
    print(f"  удаляем индекс 2: {lst.remove_at(2)}")
    print(f"  список: {lst}")
    
    print("\n2. Итерация по списку:")
    for item in lst:
        print(f"  - {item}")
