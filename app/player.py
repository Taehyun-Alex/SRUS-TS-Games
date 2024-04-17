from argon2 import PasswordHasher


class Player:
    def __init__(self, id: str, player_name: str, score: int = None):
        self.id = id
        self.player_name = player_name
        self.ph = PasswordHasher()
        self._hashed_password = None
        self._score = score

    def uid(self):
        return self.id

    def name(self):
        return self.player_name

    def get_score(self):
        return self._score

    def set_score(self, new_score):
        if new_score >= 1 and isinstance(new_score, int):
            self._score = new_score
        else:
            raise ValueError("Score must be a positive integer value.")

    def __str__(self):
        return f"Id:{self.id}  Name:{self.player_name}"

    def __eq__(self, other):
        return self._score == other.get_score()

    def __gt__(self, other):
        return self._score > other.get_score()

    def __lt__(self, other):
        return self._score < other.get_score()

    def add_password(self, password: str):
        self._hashed_password = self.ph.hash(password)

    def verify_password(self, password_to_verify: str):
        if self.ph.verify(self._hashed_password, password_to_verify):
            return True
        return False

    @staticmethod
    def radix_sort_in_descending_order(lst):
        max_num = max(lst)
        max_digits = len(str(max_num))

        for digit_place in range(max_digits):
            buckets = [[] for _ in range(10)]

            for num in lst:
                digit = (num // (10 ** digit_place)) % 10
                buckets[digit].append(num)

            lst = [num for bucket in reversed(buckets) for num in bucket]

        return lst

