def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        return quick_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            quick_sort([e for e in l[1:] if e > l[0]])

print(quick_sort([3, 1, 2, 4, 7, 5, 6, 9, 8]))


# === Output === #

# [1, 2, 3, 4, 5, 6, 7, 8, 9]