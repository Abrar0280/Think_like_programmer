numbers = [1, 2, -3, 3, -7, 5, 4, -1, 4, 5]
count=0

x=sum(1 for number in numbers if number < 0)
print("The count of number's less than 0 are: {}".format(x))

# === Output === #

# The count of number's less than 0 are: 3
