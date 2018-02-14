positiveCount = 0
negativeCount = 0

for i in range(0,10):
    number = int(input("Enter {0} Numbers: ".format(i)))
    if number > 0:
        positiveCount=positiveCount + 1
    if number < 0:
        negativeCount=negativeCount + 1
print("Do you want the (p)ositive or (n)egative count? ")
response=str(input())

if response == 'p':
    print("Positive count is {0}".format(positiveCount))
if response == 'n':
    print("Negative count is {0}".format(negativeCount))

# === Output === #

# Enter 0 Numbers: -5
# Enter 1 Numbers: -5
# Enter 2 Numbers: -4
# Enter 3 Numbers: -10
# Enter 4 Numbers: 1
# Enter 5 Numbers: 2
# Enter 6 Numbers: 5
# Enter 7 Numbers: 4
# Enter 8 Numbers: 45
# Enter 9 Numbers: 4
# Do you want the (p)ositive or (n)egative count?
# p
# Positive count is 6