
sales=[[1856,498,30924,328,2653,387,3754,387587,2873,276,32],
       [5665,5456,3983,6464,9957,4785,3875,3838,4959,1122,7766,2534],
       [23,55,67,99,264,376,232,223,4546,564,4544,3434]]

highest=sales[0][0]
# print(highest)
for agent in range(0,3):
    for months in range(0,11):
        if sales[agent][months] > highest:
            highest=sales[agent][months]
            print("The highest value is: {0}".format(highest))

def arrayAverage(Array,length):
    sum=0
    for i in range(0,length):
        sum += Array[i]
    average=(sum + 0.5) / length
    return average

highest_average=arrayAverage(sales[0],11)
for agent in range (0,3):
    agent_average=arrayAverage(sales[agent],11)
    if agent_average > highest_average:
        highest_average=agent_average
print("The highest averaqge is: {0}".format(highest_average))


# # === Output === #
#
# # The highest value is: 30924
# # The highest value is: 387587
# # The highest averaqge is: 39197.13636363636
