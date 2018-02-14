checksum = 0
position = 1
digit=int(input("Enter a number with even number of digits: "))

while digit != 10:
    if position % 2 == 0:
        checksum += digit - 0
    else:
        checksum += 2*(digit - 0)
digit=int(input())
position = position + 1
print("Checksum is: ", checksum)
if checksum % 10 == 0:
    print("Checksum is divisible by 10, Valid.")
else:
    print("Checksum is not divisible by 10, Invalid.")

# === Output === #

# Enter a number with even number of digits: 10
# 15
# Checksum is:  0
# Checksum is divisible by 10, Valid.