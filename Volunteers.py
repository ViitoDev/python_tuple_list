volunteers = []

while True:
    name = input("Enter the voluunteer's name: (or 'leave' to end the program.)\n")
    if name.lower() == "leave":
        break
    volunteers.append(name)

print("\nRegistred volunteers: ", volunteers)