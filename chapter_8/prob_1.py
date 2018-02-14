
Array=[1,2,3,4,5]
length=len(Array)
total=0
positive_count=0

for i in range(0,length):
    if Array[i] > 0:
        total += Array[i]
        positive_count += 1
# print(positive_count)
average=total/positive_count
print("Average of positive count is: {}".format(average))

# === Output === #

# Average of positive count is: 3.0
