from typing import Union, List, Optional

from argon2 import PasswordHasher


class Player:
    def __init__(self, id: str, player_name: str, score: int = None) -> None:
        self.id = id
        self.player_name = player_name
        self.ph = PasswordHasher()
        self._hashed_password = None
        self._score = score

    def uid(self) -> str:
        return self.id

    def name(self) -> str:
        return self.player_name

    @property
    def score(self) -> Optional[int]:
        return self._score

    @score.setter
    def score(self, new_score: Optional[int]) -> None:
        if new_score is not None and new_score >= 1 and isinstance(new_score, int):
            self._score = new_score
        else:
            raise ValueError("Score must be a positive integer value.")

    def __str__(self) -> str:
        return f"Id:{self.id}  Name:{self.player_name}"

    def __eq__(self, other) -> bool:
        return self.score == other.score

    def __gt__(self, other) -> bool:
        return self.score > other.score

    def __lt__(self, other) -> bool:
        return self.score < other.score

    @property
    def password(self) -> Optional[str]:
        return self._hashed_password

    @password.setter
    def password(self, password: Optional[str]) -> None:
        if password is not None:
            self.password = self.ph.hash(password)
        else:
            raise ValueError("Password cannot be None.")

    def verify_password(self, password_to_verify: str) -> bool:
        if self.ph.verify(self.password, password_to_verify):
            return True
        return False

    @staticmethod
    def radix_sort_in_descending_order(lst: List[int]) -> List[int]:
        max_num = max(lst) if lst else 0
        max_digits = len(str(max_num))

        for digit_place in range(max_digits):
            buckets = [[] for _ in range(10)]

            for num in lst:
                digit = (num // (10 ** digit_place)) % 10
                buckets[digit].append(num)

            lst = [num for bucket in reversed(buckets) for num in bucket]

        return lst
