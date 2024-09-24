user_type = input("Enter the user type Admin,Manager,Guest\n")
match user_type:
    case "Admin" | "Manager":
        print("Hello! Admin")
    case "Guest":
        print("Hello! Guest")
    case _:
        print("Hello There")