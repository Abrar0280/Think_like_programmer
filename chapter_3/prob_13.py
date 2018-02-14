
def arraySortedOrNot(arr):
    n = len(arr)

    if n == 1 or n == 0:
        return True

    return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])


arr = [100, 20, 23, 23, 45, 78]


if arraySortedOrNot(arr):
    print("Yes, The array is sorted")
else:
    print("No, Array is not sorted!")

# === Output === #

# arr = [20, 23, 23, 45, 78, 88]
# Yes, The array is sorted

# arr = [100, 20, 23, 23, 45, 78]
# No, Array is not sorted!
