length1 = int(input("Enter the Length1\n"))
length2 = int(input("Enter the Length2\n"))
length3 = int(input("Enter the Length3\n"))

if length1 == length2 == length3:
    print("It is a Equilateral Triangle")
elif length1 == length2 or length2 == length3 or length3 == length1:
    print("It is a Isosceles Triangle")
else:
    print("It is a Scalene Triangle")