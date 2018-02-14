def dec_to_bin(x):
    return int(bin(x)[2:])

x=20
decimal = 0

binary_value= dec_to_bin(x)

# print("Decimal Number {0}, when converted to binary leads a value {1}".format(x,binary_value))
for digit in str(binary_value):
    decimal = decimal *2 + int(digit)
print("The Binary value {0}, when converted to deci,al leads to {1} ".format(str(binary_value),decimal))


# === Output === #

# Decimal Number 20, when converted to binary leads a value 10100
# The Binary value 10100, when converted to deci,al leads to 20
