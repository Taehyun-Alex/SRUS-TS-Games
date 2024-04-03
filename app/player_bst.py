class PlayerBST:
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    def insert(self, player):
        if self._root is None:
            self._root = player.player_name
        else:
            if self._root > player.player_name:
                if self._root.left is None:
                    self._root.left = player.player_name
                else:
                    # Resursive
            elif self._root < player.player_name:
                if self._root.right is None:
                    self._root.right = player.player_name
                else:
                    # Recursive
            else:
                # same name, so update the value
