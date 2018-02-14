Array=[1,2,3,4,5,6,7,8,9,12,13,14]
length_array=len(Array)
# print(length_array)
highest_value=Array[0]

for i in range(0,length_array):
    if Array[i] > highest_value:
        highest_value=Array[i]
        print(highest_value)

# ===  Output === #

# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 12
# 13
# 14