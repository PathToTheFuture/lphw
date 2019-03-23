happy = "Love"

def print_two(*args):
    arg1, arg2 = args
    print(f"Arg1: {arg1}, Arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"Arg1: {arg1}, Arg2 {arg2}")


def print_one(arg1):
    print(f"Arg1: {arg1}")


def print_none():
    print("I got nothin'.")



print_two('Christian', 'Johnson')
print_two_again(1>4, happy)
print_one("first!")
print_none()
