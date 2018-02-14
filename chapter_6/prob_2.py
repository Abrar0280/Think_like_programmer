def sum(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum(n[1:])

num=[1,2,3,4,5]

print("The Sum of elements in the list is: {}".format(sum(num)))

# === Output === #

# The Sum of elements in the list is: 15
