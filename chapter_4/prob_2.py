
def refparameter(number):
    address=id(number)
    return address


number = 5
x=refparameter(number)
print("The number is: {}".format(number))
print("The address is {}".format(x))

# === Output === #

# The number is: 5
# The address is 1460196464
