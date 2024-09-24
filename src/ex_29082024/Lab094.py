# List
# List - Collection of Items(Duplicates Allowed)

my_list = [1, 2, 3]
# my_list2 = [1, True, "Kumutha", 13.14]

print(my_list)
print(len(my_list))

print(my_list[0])
print(my_list[1])
# print(my_list[10])

my_list[0] = "Kumutha"
my_list[1] = "Vinu"
my_list[2] = "Vinu"

# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

print(my_list)
for element in my_list:
    print(element)

for i in range(1, 10, 1):
    print(i)

print("--------------------------------------------")
my_list = [1, 2, 3]

#append
my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list)

# extend
my_list.extend([7, 8, 9])
my_list.extend([10])
my_list.extend(["Kumutha"])
print(my_list)
print(len(my_list))

# insert
my_list.insert(1,"Vinu")
print(my_list)
print(len(my_list))

my_list[1] = "Kumutha"
print(my_list)

my_list.insert(0, 0)
my_list.insert(-1,"Krithvi")
print(my_list)


# remove
my_list.remove("Kumutha")
print(my_list)

print("--------------------------------------------")
print("--------------------------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Krithvi")
my_copy_list.remove("Kumutha")
my_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)