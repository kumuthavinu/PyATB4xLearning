year = int(input("Please Enter the Year\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"This {year} is Leap year")
else:
    print(f"This {year} is not a Leap year")
