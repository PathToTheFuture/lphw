def stupid_name(stupid_count, fucks_given):
    print(f"You have {stupid_count} of stupid!")
    print(f"You have {fucks_given} number of stupid exercises!")
    print("Man that's enough for a dumbfuck!")
    print("Get a Slap.\n")

print("We can just give the function numbers directly:")
stupid_name(53, 19)

print("Or, we can use variablesfrom our script:")
amount_of_stupid = 40
amount_of_fucks = 2

stupid_name(amount_of_stupid, amount_of_fucks)

print("We can even do math inside too: (duh already knew that)")

stupid_name(40+53, 2-19.0)

print("And we can compine the two, variables and math:")
stupid_name(amount_of_stupid-15, amount_of_fucks+20)
