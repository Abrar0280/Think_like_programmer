def recursiveCount(lst,key):
    if lst == []:
        return 0
    if lst[0] == key:
        return 1 + recursiveCount(lst[1:],key)
    else:
        return 0 + recursiveCount(lst[1:],key)

print(recursiveCount([1,2,34,4,5,1,1,2,2,5],1))


# === Output === #

# 3
