# Difficulty: 2.1
from typing import Union


def is_positive(num1: int, num2: int) -> bool:
    if num1 > 0 and num2 > 0:
        return True
    else:
        return False


def fits_domain(num1: int, num2: int) -> bool:
    if num1 < 10**10_000 and num2 < 10 ** 10_000:
        return True
    else:
        return False


def is_digit(num1: str, num2: str) -> bool:
    if num1.isdigit() and num2.isdigit():
        return True
    else:
        return False


def sum(num1: str, num2: str) -> Union[int, None]:
    if (
        is_positive(int(num1), int(num2))
        and fits_domain(int(num1), int(num2))
        and is_digit(num1, num2)
    ):
        return int(num1) + int(num2)
    else:
        return None


if __name__ == "__main__":
    x = input()
    y = input()

    result = sum(x, y)
    print(result)
