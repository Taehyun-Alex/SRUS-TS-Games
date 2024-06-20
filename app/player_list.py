class PlayerList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def is_empty(self) -> bool:
        return self._head is None

    def insert_at_head(self, new_node) -> None:
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head.previous_node = new_node
            self._head = new_node

    def insert_at_tail(self, new_node) -> None:
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.previous_node = self._tail
            self._tail.next_node = new_node
            self._tail = new_node

    def delete_at_head(self) -> None:
        if self.is_empty():
            raise Exception("Cannot delete from an empty list")
        if self._head.next_node is not None:
            self._head = self._head.next_node
            self._head.previous_node = None
        else:
            self._head = None
            self._tail = None

    def delete_at_tail(self) -> None:
        if self.is_empty():
            raise Exception("Cannot delete from an empty list")
        if self._tail.previous_node is not None:
            self._tail = self._tail.previous_node
            self._tail.next_node = None
        else:
            self._head = None
            self._tail = None

    def delete_with_key(self, key: str) -> None:
        if self.is_empty():
            raise Exception("Cannot delete from an empty list")

        current = self._head
        while current is not None:
            if current.key == key:
                if current == self._head:
                    self._head = current.next_node
                    if self._head is not None:
                        self._head.previous_node = None
                    else:
                        self._tail = None
                elif current == self._tail:
                    self._tail = current.previous_node
                    if self._tail is not None:
                        self._tail.next_node = None
                    else:
                        self._head = None
                else:  # if the key is in the middle of the list
                    previous_node = current.previous_node
                    next_node = current.next_node
                    previous_node.next_node = next_node
                    next_node.previous_node= previous_node
                return
            current = current.next_node
        raise Exception(f"The list does not contain a node with key {key}")

    def display(self, forward=True) -> None:
        if self.is_empty():
            print("The list is empty.")
            return

        # Traverse the linked list again to display the values
        if forward:
            current = self._head
            print("Printing values from left to right")
            while current is not None:
                print(current.player)
                current = current.next_node
        else:
            current = self._tail
            print("Printing values from right to left")
            while current is not None:
                print(current.player)
                current = current.previous_node
