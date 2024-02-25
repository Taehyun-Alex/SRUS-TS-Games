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

