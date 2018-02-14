data = []
print("This program will make mean, median and mode very easy!")
print("\nFirst, we need to enter some numbers!")

num = input("Type your first number: ")
while num:
    data.append(float(num))  # Converts num into a float so we can do division
    print("\n", data)
    num = input("Add another number, or press enter to move on.")

total = sum(data)
length = len(data)
print("\n\nThe Mean Is:", total / length)

data.sort()
print("\n\nHere's the list in numerical order:\n", data)

oddness = length % 2
half = length // 2
if oddness == 1:
    print("The median is:", data[half])
else:
    low = float(data[half - 1])
    high = float(data[half])
    print("The median is half way between", low, "and", high)
    print("That makes it:", low + (high - low) / 2)

hits = []
for item in data:
    tally = data.count(item)
    values = (tally, item)

    if values not in hits:
        hits.append(values)
hits.sort(reverse=True)
if hits[0][0] > hits[1][0]:
    print("\n\nThe mode is:", hits[0][1], "hit appeared", hits[0][0], "times.")
else:
    print("There is not a mode")


# === Output === #

# This program will make mean, median and mode very easy!
#
# First, we need to enter some numbers!
# Type your first number: 15
#
#  [15.0]
# Add another number, or press enter to move on.14
#
#  [15.0, 14.0]
# Add another number, or press enter to move on.20
#
#  [15.0, 14.0, 20.0]
# Add another number, or press enter to move on.14
#
#  [15.0, 14.0, 20.0, 14.0]
# Add another number, or press enter to move on.45
#
#  [15.0, 14.0, 20.0, 14.0, 45.0]
# Add another number, or press enter to move on.75
#
#  [15.0, 14.0, 20.0, 14.0, 45.0, 75.0]
# Add another number, or press enter to move on.
# 78
#
#
# The Mean Is: 30.5
#
#
# Here's the list in numerical order:
#  [14.0, 14.0, 15.0, 20.0, 45.0, 75.0]
# The median is half way between 15.0 and 20.0
# That makes it: 17.5
#
#
# The mode is: 14.0 hit appeared 2 times.

