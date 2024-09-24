# 1. No Return type with no arguments

def greet():
    print("Hello, Everyone!!")


result = greet()
print(result)


# 2. No Return type with argument

def greet_by_name(name):
    print("Hello", name)


greet_by_name("Vinu")


# 3. No Return type with Default Argument

def say_hello_default_argument(name="Vinu"):
    print("Hello", name)


say_hello_default_argument("Kumutha")
say_hello_default_argument()
say_hello_default_argument(name="Krithvi")


# Multiple Arguments

def multiple_arguments(name1="Kumutha", name2="Vinu", name3="Krithvi"):
    print("Mutiple Argumants", name1, name2, name3)


multiple_arguments()
multiple_arguments(name1="Mani", name2="Priya", name3="Sathvika")
multiple_arguments(name1="Jaya")


# 4. return Type with Argument

def sum_of_two_number(num1, num2):
    return num1 + num2


result = sum_of_two_number(10, 20)
print(result)
