answer = []

a = 10#float(input("Enter your first number.\n"))
b = 2#float(input("Enter your second number.\n"))
n = 10#int(input("Enter the number digits in the answer.\n"))

for i in range(n):
    a = a // b
    b = a % b
    answer.append(str(a))

    print("".join(answer))
