class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._previous = None

    # player getter
    def get_player(self):
        return self._player

    # next_node setter
    def next_node(self, node):
        self._next = node

    # next_node getter
    def get_next(self):
        return self._next

    # previous_node setter
    def previous_node(self, node):
        self._previous = node

    # previous_node getter
    def get_previous(self):
        return self._previous

    # returns uid property of the player instance
    def key(self):
        return self._player.uid

    def __str__(self):
        return str(self._player)
