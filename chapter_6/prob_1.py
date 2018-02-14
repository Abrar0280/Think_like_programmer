def factorial(n):
    if n == 1:
        return 1
    else:
        return n *factorial(n-1)

num=int(input("Enter a number: "))

print("The factorial of {0} is {1}".format(num,factorial(num)))

# === Output === #

# Enter a number: 5
# The factorial; of 5 is 120