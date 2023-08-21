class Node:
    def __init__(self, member_no, member_name, age):
        self.member_no = member_no
        self.member_name = member_name
        self.age = age
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, member_no, member_name, age):
        new_node = Node(member_no, member_name, age)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_node

def main():
    queue = Queue()
    queue.enqueue(1001, "John Doe", 30)
    queue.enqueue(1002, "Jane Doe", 25)
    print("Dequeued member:", queue.dequeue())
    print("Dequeued member:", queue.dequeue())

if __name__ == "__main__":
    main()
