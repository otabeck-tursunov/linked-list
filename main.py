class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert(self, data, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        obj = self.head
        while obj.data != data and obj.next is not None:
            obj = obj.next
        if obj.data == data:
            new_node.next = obj.next
            obj.next = new_node
            return
        else:
            return f"{data} not in LinkedList"

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        obj = self.head
        while obj.next is not None:
            obj = obj.next
        obj.next = new_node
        return

    def delete(self, data):
        if self.head is None:
            return "LinkedList is empty"
        obj = self.head
        while obj.data != data and obj.next is not None:
            obj = obj.next
        if obj.data == data:
            new_obj = self.head
            while new_obj.next.data != obj.data:
                new_obj = new_obj.next
            new_obj.next = new_obj.next.next
            return
        else:
            return f"{data} not in LinkedList"

    def get_list(self):
        if self.head is None:
            return []
        obj = self.head
        l = [obj.data]
        while obj.next is not None:
            obj = obj.next
            l.append(obj.data)
        return l

    def length(self):
        return len(self.get_list())


monday = Node("Monday")
tuesday = Node("Tuesday")

monday.next = tuesday
linked_list = LinkedList(monday)

linked_list.push('Sunday')
linked_list.insert('Tuesday', 'Wednesday')
linked_list.append('Thursday')
linked_list.delete('Thursday')
print(linked_list.head.next.next.next.data)
print(linked_list.get_list())
print(linked_list.length())
