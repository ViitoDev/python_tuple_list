current_list = ["Jonh", "Mia", "Sophia"]
print(f"The current list is: {current_list}")
new_guest = input("Enter the new guest: \n")
guest_position = int(input("Enter the guest position: \n"))
current_list.insert(guest_position - 1, new_guest)
print(f"The updated list is: {current_list}")