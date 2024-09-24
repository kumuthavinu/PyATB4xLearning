# Functions within the Functions
"""def outer_function():
    var = 30  # local int variable

    def inner_function1():
        print(var)

    def inner_function2():
        print(var)

    inner_function1()
    inner_function2()


outer_function()"""

# Passing List in the Function

my_shopping_list = ["Bread", "Butter", "Milk"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_shopping_list):
    # more_item = input("Enter the item to add") # Get the item from the user
    # my_shopping_list.append(more_item)
    # my_shopping_list.remove(more_item) # Remove the item
    my_shopping_list.append("Cheese") #Adding the new item in the list
    return my_shopping_list

l = bring_more_food(my_shopping_list)
print(l)
