filename = input("Filename: ")

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

New = input()

print("I'm going to write these to the file.")

target.write(New)

print("I'll save those changes thank you!")
target.close()
