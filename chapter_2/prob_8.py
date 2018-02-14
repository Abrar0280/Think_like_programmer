checksum = 0
for i in range(1,7):
    digit=int(input("Enter a six digit number: "))
    checksum += digit - 0
print("The Checksum is: ",checksum)

if checksum % 10 == 0:
    print("Checksum is divisible by 10, Valid.")
else:
    print("Checksum is not divisible by 10, Invalid.")

# === Output === #

# Enter a six digit number: 4
# Enter a six digit number: 1
# Enter a six digit number: 1
# Enter a six digit number: 5
# Enter a six digit number: 7
# Enter a six digit number: 8
# The Checksum is:  26
# Checksum is not divisible by 10, Invalid.