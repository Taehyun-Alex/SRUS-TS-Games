from argon2 import PasswordHasher

class Player:
    def __init__(self, id: str, player_name: str):
        self.id = id
        self.player_name = player_name
        self.ph = PasswordHasher()
        self._hashed_password = None

    def uid(self):
        return self.id

    def name(self):
        return self.player_name

    def __str__(self):
        return f"Id:{self.id}  Name:{self.player_name}"

    def add_password(self, password: str):
        self._hashed_password = self.ph.hash(password)

    def verify_password(self, password_to_verify: str):
        if self.ph.verify(self._hashed_password, password_to_verify):
            return True
        return False


player_1 = Player("100", "John")
player_2 = Player("101", "David")

player_1.add_password("hello")
print(player_1.verify_password("hello"))