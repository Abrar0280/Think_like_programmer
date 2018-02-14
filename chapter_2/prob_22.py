
no = int (input("Enter a number: "))
space_no = no - 2
print_line = "   *"*no
for i in range(1,no+1):
    if space_no>0:
        print_line_n = "*"*i+" "*space_no+"*"*i
        space_no -=2
        print(print_line_n)

# === Output === #

# *       *
# **     **
# ***   ***
# **** ****