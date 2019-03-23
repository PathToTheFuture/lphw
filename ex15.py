from sys import argv

script, filename = argv # pass in the filename of user choice

txt = open(filename) # take the specified file open and save to txt varible

print(f"Here's you file {filename}:")
print(txt.read()) # prints the file that was saved in the txt varible

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
