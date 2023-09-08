# Difficult: 2.0

def count_a(s):
    count = 0
    while count < len(s) and s[count] == "a":
        count += 1
    return count

def compare_count_a(person1, person2):
    jon_count = count_a(person1)
    doctor_count = count_a(person2)

    if doctor_count > jon_count:
        return "no"
    else:
        return "go"
    
if __name__ == "__main__":
    jon = input()
    doctor = input()
    result = compare_count_a(jon, doctor)
    print(result)