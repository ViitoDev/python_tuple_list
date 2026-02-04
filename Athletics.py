names = ["John", "Mia", "Jonathan"]
print(f"Current list: {names}")
wrong_name = input("Enter the wrong name:\n")

if wrong_name in names:
    correct_name = input("Enter the correct name:\n")
    position = wrong_name.index(wrong_name)
    names.remove(wrong_name)
    names.insert(position, correct_name)
    print(f"The name {wrong_name} has been replaced with {correct_name}")
    print(f"Updated list: {names}")
else:
    print("Error: Name not found.")