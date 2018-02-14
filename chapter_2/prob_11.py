def doubleDigitValue(digit):
    doubleDigit=digit
    if doubleDigit > 10:
        sum = 1 + doubleDigit % 10
    else:
        sum = doubleDigit
    return sum

oddLengthCheckSum = 0
evenLengthChecksum = 0
position = 1
digit=int(input("Enter a Number: "))

while digit != 10:
    if position % 2 == 0:
        oddLengthCheckSum += doubleDigitValue(digit - 0)
        evenLengthChecksum += digit - 0
    else:
        oddLengthCheckSum += digit - 0
        evenLengthChecksum += doubleDigitValue(digit - 0)
    digit=int(input())
    position += 1
if ((position - 1) % 2 == 0):
   Checksum=evenLengthChecksum
else:
    Checksum=oddLengthCheckSum
print("CheckSum is: ",Checksum)

if Checksum % 10 == 0:
    print("Checksum is divisible by 10, valid")
else:
    print("CheckSum is not divisible by 10, Invalid")

# === Output === #

# === CASE 1 === #

# Enter a Number: 12
# 10
# CheckSum is:  12
# CheckSum is not divisible by 10, Invalid

# === CASE 2 === #

# Enter a Number: 30
# 10
# CheckSum is:  30
# Checksum is divisible by 10, valid
