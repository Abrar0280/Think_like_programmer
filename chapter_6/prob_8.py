from statistics import mode
l=[0,1,0,1,1,1,0]

frequent=mode(l)

if frequent == 0:
    print("The list has even parity.")
elif frequent == 1:
    print("The list has odd parity.")


# === Output === #

# The list has odd parity.

