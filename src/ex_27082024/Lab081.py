def add_before_ui_after_ui(func):
    def wrapper():
        print("Before the running UI TC")
        print("Start the browser")
        func()
        print("After the running UI TC")
        print("Quit the Browser")
    return wrapper()
@add_before_ui_after_ui
def test_ui():
    print("I will Test the UI")


