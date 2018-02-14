def recur_sum(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + recur_sum(n[1:])

num_list=[1,2,3,4,-5,-10]

num_list = [item for item in num_list if item >= 0]
print("The sum of positive numbers excluding negatives: {}".format(recur_sum(num_list)))

# === Output === #

# The sum of positive numbers excluding negatives: 10
