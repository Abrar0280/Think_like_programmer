Array=[1,2,3,4,5,6,7,8,9,12,13,14]
print(Array)
for i in range(0,12):
    Array[i]=-1
print(Array)

# === Output === #

# Before = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14]
# After = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]