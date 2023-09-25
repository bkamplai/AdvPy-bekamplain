# Difficulty: 2.1
from typing import Union


def is_power_of_ten(num: int) -> bool:
    while num > 1:
        if num % 10 != 0:
            return False
        num //= 10
    return True


def calculate(A: str, operand: str, B: str) -> Union[int, None]:
    if len(A) > 100 or len(B) > 100:
        return None
    elif not A.isdigit() or not B.isdigit():
        return None
    elif operand != "*" and operand != "+":
        return None
    else:
        int_A: int = int(A)
        int_B: int = int(B)
        if int_A <= 0 or int_B <= 0:
            return None
        if is_power_of_ten(int_A) and is_power_of_ten(int_B):
            if operand == "*":
                return int_A * int_B
            else:
                return int_A + int_B
        else:
            return None


if __name__ == "__main__":
    A: str = input()
    operand: str = input()
    B: str = input()
    result = calculate(A, operand, B)
    print(result)
