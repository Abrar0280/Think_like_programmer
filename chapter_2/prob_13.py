
digitChar=int(input("Enter a three-digit or four-digit number: "))
threeDigit=(digitChar - 0) * 100
fourDigit=(digitChar - 0) * 1000

digitChar=int(input("Enter a three-digit or four-digit number: "))
threeDigit += (digitChar - 0) * 10
fourDigit += (digitChar - 0) * 100

digitChar=int(input("Enter a three-digit or four-digit number: "))
threeDigit += (digitChar - 0)
fourDigit += (digitChar - 0) * 10

if digitChar == 10:
    print("Number Entered is: ",threeDigit)
else:
    fourDigit += (digitChar - 0)
    print("Number Entered is: ", fourDigit)

# === Output === #

# Enter a three-digit or four-digit number: 120
# Enter a three-digit or four-digit number: 1200
# Enter a three-digit or four-digit number: 450
# Number Entered is:  24495