# ========================== Problem 1 ================================ #

# variable_1=10
#
# address_of_Variable_1=id(variable_1)
# print("The address of variable {0} is: {1}".format(variable_1,address_of_Variable_1))

# === Output === #

# The address of variable 10 is: 1460196544

# ========================== Problem 2 ================================ #

# def refparameter(number):
#     address=id(number)
#     return address
#
#
# number = 5
# x=refparameter(number)
# print("The number is: {}".format(number))
# print("The address is {}".format(x))

# === Output === #

# The number is: 5
# The address is 1460196464

# ========================== Problem 3 ================================ #

# def functionB(num):
#     return num-10
#
# def functionA(num):
#     localvar=functionB(num*10)
#     return localvar
# x=12
# y=functionA(x)
# print("The result from the above function operation is: {}".format(y))

# === Output === #

# The result from the above function operation is: 110

# ========================== Problem 4 ================================ #

# import sys
# x = sys.getsizeof(int)
# print("The size of int is: {}".format(x))

# === Output === #

# The size of int is: 200

# ========================== Problem 5 ================================ #

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


# node=Node(1)
# print(node.get_next())
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

link=LinkedList()
link_1=LinkedList()

x = link.insert(5)
y = link_1.insert(6)

print(x)
print(y)