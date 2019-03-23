formatter = "\n{}\n{}\n{}\n{}"
audience = "[snap snap snap snap]"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))


print("Happy Endings?")
print(formatter.format(
"There are no happy endings.",
"Endings are the saddest part.",
"So just give me a happy middle.",
"And a very happy start."
))
print("By Shel Silverstein " + audience)
