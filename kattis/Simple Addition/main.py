# Difficulty: 2.0

def is_positive(num1, num2):
    if num1 > 0 and num2 > 0:
        return True
    else:
        return False

def fits_domain(num1, num2):
    if num1 < 10**10_000 and num2 < 10 ** 10_000:
        return True
    else:
        return False

def is_digit(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return True
    else:
        return False
    
def sum(num1, num2):
    if is_positive(int(num1), int(num2)) and fits_domain(int(num1), int(num2))and is_digit(num1, num2):
        return eval(num1) + eval(num2)
    else:
        return None

if __name__ == "__main__":
    x = input()
    y = input()

    result = sum(x, y)
    print(result)
    