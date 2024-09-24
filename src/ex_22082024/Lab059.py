#Write a program
browser_name = input("Enter the browser name\n")
browser_name = browser_name.lower()
match browser_name:
    case "chrome":
        print("Execute the code in chrome browser")
    case "firefox":
        print("Execute the code in firefox browser")
    case "edge":
        print("Execute the code in edge browser")
    case "safari":
        print("Execute the code in safari browser")
    case _:
        print("Browser not found")

