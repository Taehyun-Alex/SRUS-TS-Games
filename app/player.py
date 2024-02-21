class Player:
    def __init__(self, id: str, player_name: str):
        self.id = id
        self.player_name = player_name

    def uid(self):
        return self.id

    def name(self):
        return self.player_name

    def __str__(self):
        return f"Id:{self.id}  Name:{self.player_name}"


player_1 = Player("100", "John")
player_2 = Player("101", "David")
