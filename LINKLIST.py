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
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        """
        pass


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