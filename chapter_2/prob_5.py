number=int(input("Enter a number between 0-9: "))
doubleDigit=number*2
if doubleDigit >= 10:
    sum = 1 + doubleDigit % 10
else:
    sum=doubleDigit
print("Sum of digits in double number: ",sum)

# === Output === #

# Enter a number between 0-9: 2
# Sum of digits in double number:  4