from os.path import exists


from_file = input("What file do you want to copy?\n")
to_file = input(f"What file would you like to copy {from_file} to?\n")

print(f"Copying form{from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")

print("ready, hit ENTER to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
