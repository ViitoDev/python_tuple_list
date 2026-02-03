items = ["bread", "cheese", "coffee"]

user_input = str(input("Enter the item you want to check:\n"))

if user_input in items:
    print(f"The item {user_input} is available on pantry.")
else:
    print(f"The item {user_input} needs to be purchased.")