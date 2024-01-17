answer = []

a = 20#float(input("Enter your first number.\n"))
b = 10#float(input("Enter your second number.\n"))
n = 10#int(input("Enter the number digits in the answer.\n"))

for i in range(n):
    whole_division_result = a // b
    remainder_from_division = a % b
    answer.append(whole_division_result)
    str_answer = "".join(answer)
    print(str_answer)
