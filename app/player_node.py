from typing import Optional

from player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._next: Optional["PlayerNode"] = None
        self._previous: Optional["PlayerNode"]= None

    # player getter
    def get_player(self) -> Player:
        return self._player

    # next_node setter
    def next_node(self, node) -> None:
        self._next = node

    # next_node getter
    def get_next(self) -> Player:
        return self._next

    # previous_node setter
    def previous_node(self, node) -> None:
        self._previous = node

    # previous_node getter
    def get_previous(self) -> Player:
        return self._previous

    # returns uid property of the player instance
    def key(self) -> str:
        return self._player.uid()

    def __str__(self) -> str:
        return str(self._player)
