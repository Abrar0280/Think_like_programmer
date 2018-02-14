def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result

print(base_convert(25,9))

# === Output === #

# [2, 7]