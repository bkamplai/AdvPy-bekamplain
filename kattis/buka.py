# Difficulty: 2.0

def is_power_of_ten(num):
    while num > 1:
        if num % 10 != 0:
            return False
        num //= 10
    return True

def calculate(A, operand, B):
    if len(A) > 100 or len(B) > 100:
        return None
    elif not A.isdigit() or not B.isdigit():
        return None
    elif operand != "*" and operand != "+":
        return None
    else:
        int_A = int(A)
        int_B = int(B)

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
    A = input()
    operand= input()
    B = input()

    result = calculate(A, operand, B)
    print(result)