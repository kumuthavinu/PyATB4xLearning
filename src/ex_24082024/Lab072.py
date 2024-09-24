def print_arguments(*args):
    #print(args[0])
    for i in args:
        print(i)

print_arguments("Kumutha", "Vinu", "Krithvi")
print_arguments("Vinu", "Krithvi")
print_arguments("Krithvi", 10)
print_arguments(10,True)
print_arguments("Mani", 10, True, False)


print("Kumutha")
print("Vinu", "Krithvi")
print("Mani", "Priya", "Sathvika")
print("Jaya", "Seetha", True)
print("Malliga", "Ceaser", False)