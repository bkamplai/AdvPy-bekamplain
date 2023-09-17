# Difficult: 2.0

def count_a(s: str) -> int:
    count: int = 0
    while count < len(s) and s[count] == "a":
        count += 1
    return count


def compare_count_a(person1: str, person2: str) -> str:
    jon_count: int = count_a(person1)
    doctor_count: int = count_a(person2)

    if doctor_count > jon_count:
        return "no"
    else:
        return "go"


if __name__ == "__main__":
    jon: str = input()
    doctor: str = input()
    result: str = compare_count_a(jon, doctor)
    print(result)
