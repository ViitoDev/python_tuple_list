data = input("Enter the student dada on format: name, age, note")

for i in range(0, len(data), 3):
    name, age, note = data[i], int(data[i + 1]), float (data[i + 2])
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Note: {note}\n")