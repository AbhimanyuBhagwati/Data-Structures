class CreateNode:
    def __init__(self, value):
        self.node = value
        self.next = None


class LinkList:
    def __init__(self, value):
        new_node = CreateNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_linklist(self):
        temp = self.head
        while temp is not None:
            print(temp.node)
            temp = temp.next


    def append_node(self, value):
        new_node = CreateNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length+=1

    def pop_node(self):
        if self.length == 0:
            return None
        if self.head is None:
            return False
        else:
            pre = None
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -=1
            if self.length == 0:
                self.head, self.tail = None, None
            return temp


if __name__ == "__main__":
    linklist_obj = LinkList(1)
    linklist_obj.append_node(2)
    linklist_obj.append_node(3)

    linklist_obj.print_linklist()
    linklist_obj.pop_node()
    linklist_obj.print_linklist()

