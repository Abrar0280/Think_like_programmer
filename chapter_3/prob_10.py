def arrayAverage(Array,length):
    sum=0
    for i in range(0,length):
        sum += Array[i]
    average=(sum + 0.5) / length
    return average

Array=[1,2,3,4,5]
length=len(Array)

print("The Average of the terms in the list is: {}".format(arrayAverage(Array,length)))

# === Output === #

# The Average of the terms in the list is: 3.1
