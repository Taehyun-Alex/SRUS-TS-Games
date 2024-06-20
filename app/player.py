class Player:
    def __init__(self, id: str, player_name: str) -> None:
        self._id = id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._player_name

    def __str__(self) -> str:
        return f"Id:{self._id}  Name:{self._player_name}"


player_1 = Player("100", "John")
player_2 = Player("101", "David")
