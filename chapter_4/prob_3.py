
def functionB(num):
    return num-10

def functionA(num):
    localvar=functionB(num*10)
    return localvar
x=12
y=functionA(x)
print("The result from the above function operation is: {}".format(y))

# === Output === #

# The result from the above function operation is: 110
