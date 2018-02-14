gradeArray=[82,45,12,78,95,64,13,65,52,44]
length=len(gradeArray)
sum=0
for i in range(0,length):
    sum += gradeArray[i]
average= sum/length
print("The average of elements in the list {0}".format(average))

# === Output === #

# The average of elements in the list 55.0