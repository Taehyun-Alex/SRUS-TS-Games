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
        if self._head.get_next() is not None:
            self._head = self._head.get_next()
            self._head._previous = None
        else:
            self._head = None
            self._tail = None

    def delete_at_tail(self):
        if self.is_empty():
            print("The list is empty.")
        if self._tail.get_previous() is not None:
            self._tail = self._tail.get_previous()
            self._tail._next = None
        else:
            self._head = None
            self._tail = None


