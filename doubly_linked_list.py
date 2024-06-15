class CraateNone:
    def __init__(self, value):
        self.node = value
        self.pre = None
        self.next = None


class DoublyLinkList:
    def __init__(self, value):
        new_node = CraateNone(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linklist(self):
        temp = self.head
        while temp is not None:
            print(temp.node)
            temp = temp.next
        if self.head is None:
            print("LinkList is empty")

    def append(self, value):
        new_node = CraateNone(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("LinkList is empty")
            return
        if self.head is None:
            print("LinkList is empty")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        else:
            temp = self.tail
            self.tail = temp.pre
            self.tail.next = None
            temp.pre = None
            print(f"Poped value is: {temp.node}")
        self.length -= 1

    def pre_pend_node(self, value):
        new_node = CraateNone(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.length +=1

    def pop_first_node(self):
        temp = self.head
        if self.length == 0:
            print("LinkList is empty")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        else:
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
            self.length -= 1
            print(f"Poped value is: {temp.node}")

    def get_node_at_index(self, index):
        len_of_linklist_obj = len(range(self.length))
        if index < 0 or index >= len_of_linklist_obj:
            print("Index out of range")
            return
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.pre
        print(f"Node at index {index} is: {temp.node}")
        return temp

    def set_index(self, index, value):
        print("Indexing starts from 0 so where are Replacing with respect to that.")
        temp = self.get_node_at_index(index)
        if temp:
            temp.node = value

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return
        if index == 0:
            self.pre_pend_node(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = CraateNone(value)
            before = self.get_node_at_index(index-1)
            after = before.next
            before.next = new_node
            new_node.pre = before
            new_node.next = after
            after.pre = new_node
            self.length += 1

    def remove_node_at_index(self, index):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return
        if index == 0:
            self.pop_first_node()
        elif index == self.length:
            self.pop()
        else:
            current = self.get_node_at_index(index)
            before = current.pre
            after = current.next
            before.next = after
            after.pre = before
            current.next = None
            current.pre = None
            self.length -= 1



if __name__ == '__main__':
    linklist_obj = DoublyLinkList(1)
    linklist_obj.print_linklist()
    print("________APPEND________")
    linklist_obj.append(2)
    linklist_obj.append(3)
    linklist_obj.append(4)
    linklist_obj.append(5)
    linklist_obj.print_linklist()
    print("________POP________")
    linklist_obj.pop()
    linklist_obj.print_linklist()
    print("________PRE APPEND________")
    linklist_obj.pre_pend_node(0)
    linklist_obj.pre_pend_node(-1)
    linklist_obj.print_linklist()
    print("________POP FIRST________")
    linklist_obj.pop_first_node()
    linklist_obj.print_linklist()
    print("________GET NODE AT INDEX________")
    linklist_obj.get_node_at_index(4)
    print("________SET VALUE AT INDEX________")
    print("________Original Linklist________")
    linklist_obj.print_linklist()
    print("________After setting value at index________")
    linklist_obj.set_index(2, 10)
    linklist_obj.print_linklist()
    print("________INSERT NODE AT INDEX________")
    linklist_obj.insert(2, 3)
    linklist_obj.print_linklist()
    print("________REMOVE NODE AT INDEX________")
    linklist_obj.remove_node_at_index(2)
    linklist_obj.print_linklist()