class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def insert_at_head(self, new_node):
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._previous = new_node
            self._head = new_node

    def insert_at_tail(self, new_node):
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._previous = self._tail
            self._tail._next = new_node
            self._tail = new_node

    def delete_at_head(self):
        if self.is_empty():
            print("The list is empty.")
            return
        if self._head.get_next() is not None:
            self._head = self._head.get_next()
            self._head._previous = None
        else:
            self._head = None
            self._tail = None

    def delete_at_tail(self):
        if self.is_empty():
            print("The list is empty.")
            return
        if self._tail.get_previous() is not None:
            self._tail = self._tail.get_previous()
            self._tail._next = None
        else:
            self._head = None
            self._tail = None

    def delete_with_key(self, key):
        if self.is_empty():
            print("The list is empty.")
            return

        current = self._head  # sets a temporary reference
        while current is not None:
            if current.get_player() == key:
                if current == self._head:  # if the key is at the front
                    self._head = current.get_next()
                    if self._head is not None:
                        self._head.set_previous(None)
                    else:
                        self._tail = None
                elif current == self._tail:  # if the key is at the end
                    self._tail = current.get_previous()
                    if self._tail is not None:
                        self._tail.set_next(None)
                    else:
                        self._head = None
                else:  # if the key is in the middle of the list
                    previous_node = current.get_previous()
                    next_node = current.get_next()
                    previous_node.set_next(next_node)
                    next_node.set_previous(previous_node)
                return
            current = current.get_next()
        print(
            f"The list does not contain a node with key {key}.")  # This line only executes if the while loop did not
        # find the node with the passed key

    def display(self, forward=True):
        if self.is_empty():
            print("The list is empty.")
            return

        # Traverse the linked list again to display the values
        if forward:
            current = self._head
            print("Printing values from left to right")
            while current is not None:
                print(current.get_player())
                current = current.get_next()
        else:
            current = self._tail
            print("Printing values from right to left")
            while current is not None:
                print(current.get_player())
                current = current.get_previous()

