from typing import Optional

from app.player import Player


class PlayerNode:
    def __init__(self, player) -> None:
        self._player = player
        self._next: Optional["PlayerNode"] = None
        self._previous: Optional["PlayerNode"] = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def next_node(self) -> Optional["PlayerNode"]:
        return self._next

    @next_node.setter
    def next_node(self, node) -> None:
        self._next = node

    @property
    def previous_node(self) -> Optional["PlayerNode"]:
        return self._previous

    @previous_node.setter
    def previous_node(self, node) -> None:
        self._previous = node

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        return str(self._player)
