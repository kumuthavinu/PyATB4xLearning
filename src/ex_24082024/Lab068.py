num1 = int(input("Enter Number1:\n"))
num2 = int(input("Enter Number2:\n"))
num3 = int(input("Enter Number3:\n"))


def sum_of_three_numbers(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_numbers(num1, num2, num3)
print("The result is:", result)
result = sum_of_three_numbers(n1=num1, n2=num2, n3=num3)
