# Difficulty: 2.9

def find_absolute_value(num: int) -> int:
    return abs(num)


def find_difference(num1: int, num2: int) -> int:
    return num1 - num2


if __name__ == "__main__":
    while True:
        try:
            integers = input().split()
        except EOFError:
            break
        int1: int = int(integers[0])
        int2: int = int(integers[1])
        result: int = find_absolute_value(find_difference(int1, int2))
        print(result)
