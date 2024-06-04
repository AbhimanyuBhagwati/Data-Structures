class CreateNode:
    """
    A class representing a node in a linked list.

    Attributes:
        value (any): The value stored in the node.
        next (CreateNode or None): A reference to the next node in the linked list.
    """
    def __init__(self, value):
        """
        Initializes a new instance of the CreateNode class.

        Args:
            value (any): The value to be stored in the node.
        """
        self.node = value
        self.next = None


class LinkList:
    """
    A class representing a linked list data structure.

    Attributes:
        head (CreateNode or None): A reference to the first node in the linked list.
        tail (CreateNode or None): A reference to the last node in the linked list.
        length (int): The number of nodes in the linked list.
    """
    def __init__(self, value):
        """
        Initializes a new instance of the LinkList class with a single node.

        Args:
            value (any): The value to be stored in the first node of the linked list.
        """
        new_node = CreateNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linklist(self):
        """
        Prints the values of all nodes in the linked list.

        If the linked list is empty, it prints "LinkList is empty".
        """
        temp = self.head
        while temp is not None:
            print(temp.node)
            temp = temp.next
        if self.head is None:
            print("LinkList is empty")

    def append_node(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value (any): The value to be stored in the new node.
        """
        new_node = CreateNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_node(self):
        """
        Removes and returns the last node from the linked list.

        Returns:
            CreateNode or None: The removed node, or None if the linked list is empty.
        """
        if self.length == 0:
            return None
        if self.head is None:
            return False
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head, self.tail = None, None
            return temp

    def pre_append_node(self, value):
        """
        Inserts a new node with the given value at the beginning of the linked list.

        Args:
            value (any): The value to be stored in the new node.
        """
        new_node = CreateNode(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first_node(self):
        """
        Removes and returns the first node from the linked list.

        If the linked list is empty, it prints "LinkList is empty".
        """
        if self.head is None:
            print("LinkList is empty")
        else:
            if self.head.next is not None:
                temp = self.head
                self.head = self.head.next
                temp.next = None
            else:
                self.head, self.tail = None, None
        self.length -= 1

    def get_node_at_index(self, index):
        """
        Retrieves the node at the given index in the linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            CreateNode or None: The node at the specified index, or None if the index is out of range.
        """
        if self.head is None:
            return None
        temp = self.head
        for _ in range(index):
            if temp.next is None:
                return "Index out of range"
            temp = temp.next
        print(temp.node)
        return temp

    def set_value_at_index(self, index, value):
        """
        Sets the value of the node at the given index in the linked list.
        :param index:
        :param value:
        :return:
        """
        temp = self.get_node_at_index(index)
        temp.node = value

    def insert_node_at_index(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the linked list.
        :param index:
        :param value:
        :return:
        """
        if index <0 or index >= self.length:
            return "Index out of range"
        if index == 0:
            self.pre_append_node(value)
        elif index == self.length:
            self.append_node(value)
        else:
            new_node = CreateNode(value)
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def remove_node_at_index(self, index):
        if index < 0 or index >= self.length:
            return "Index out of range"
        elif index ==0:
            self.pop_first_node()
        elif index == self.length:
            self.pop_node()
        else:
            pre = self.get_node_at_index(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -=1





if __name__ == "__main__":
    linklist_obj = LinkList(1)
    linklist_obj.append_node(2)
    linklist_obj.append_node(3)
    linklist_obj.print_linklist()
    print("________POP________")
    linklist_obj.pop_node()
    linklist_obj.print_linklist()
    print("________PRE APPEND________")
    linklist_obj.pre_append_node(0)
    linklist_obj.print_linklist()
    print("________POP FIRST________")
    linklist_obj.pop_first_node()
    linklist_obj.print_linklist()
    print("________GET NODE AT INDEX________")
    linklist_obj.get_node_at_index(1)
    print("________SET VALUE AT INDEX________")
    linklist_obj.print_linklist()
    linklist_obj.set_value_at_index(1, 5)
    linklist_obj.print_linklist()
    print("________INSERT NODE AT INDEX________")
    linklist_obj.insert_node_at_index(1, 2)
    linklist_obj.insert_node_at_index(2, 3)
    linklist_obj.insert_node_at_index(3, 4)
    linklist_obj.print_linklist()
    print("________REMOVE NODE AT INDEX________")
    linklist_obj.remove_node_at_index(2)
    linklist_obj.print_linklist()