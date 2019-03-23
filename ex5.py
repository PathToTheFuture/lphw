my_name = 'Christian J. Johnson'
my_age = 23 # Not a lie
my_height = 74 # inches
my_weight = 310 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
my_kgs = round(my_weight * 0.453359237, 2) # weight in kilograms
my_cm = my_height * 2.54# height in centimeters

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"If we used the metric system I'd be {my_cm}cm tall and {my_kgs}kgs heavy")
print("Actually that's is a little too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is supposed to be tricky acording to the book... Not for meself.
total = my_age + my_height + my_weight
print(f"If I add my age {my_age}, my height {my_height}, and weight {my_weight} I get {total} total.")
