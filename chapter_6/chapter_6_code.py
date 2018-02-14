

# ===================== Problem 1 ================================== #

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n *factorial(n-1)
#
# num=int(input("Enter a number: "))
#
# print("The factorial of {0} is {1}".format(num,factorial(num)))

# === Output === #

# Enter a number: 5
# The factorial of 5 is 120

# ================================= Problem 2 ======================================= #

# def sum(n):
#     if len(n) == 0:
#         return 0
#     else:
#         return n[0] + sum(n[1:])
#
# num=[1,2,3,4,5]
#
# print("The Sum of elements in the list is: {}".format(sum(num)))

# === Output === #

# The Sum of elements in the list is: 15


# ================================= Problem 3 ======================================= #

# numbers = [1, 2, -3, 3, -7, 5, 4, -1, 4, 5]
# count=0
#
# x=sum(1 for number in numbers if number < 0)
# print("The count of number's less than 0 are: {}".format(x))

# === Output === #

# The count of number's less than 0 are: 3

# ================================= Problem 4 ======================================= #

# class Node:
#
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
#
# def insert(node, data):
#     if node is None:
#         return (Node(data))
#
#     else:
#         if data <= node.data:
#             node.left = insert(node.left, data)
#         else:
#             node.right = insert(node.right, data)
#
#         return node
#
# def minValue(node):
#     current = node
#
#     while (current.left is not None):
#         current = current.left
#
#     return current.data
#
# root = None
# root = insert(root, 4)
# insert(root, 2)
# insert(root, 1)
# insert(root, 3)
# insert(root, 6)
# insert(root, 5)
#
# print("\nMinimum value in BST is %d" % (minValue(root)))

# === Output === #

# Minimum value in BST is 1

# ================================= Problem 5 ======================================= #

# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# def getLeafCount(node):
#     if node is None:
#         return 0
#     if (node.left is None and node.right is None):
#         return 1
#     else:
#         return getLeafCount(node.left) + getLeafCount(node.right)
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print("Leaf count of the tree is %d" % (getLeafCount(root)))


# === Output === #

# Leaf count of the tree is 3

# ============================ Problem 6 ========================================= #

# class Node:
#
#     def __init__(self, data, nextNode=None):
#         self.data = data
#         self.nextNode = nextNode
#
#     def getData(self):
#         return self.data
#
#     def setData(self, val):
#         self.data = val
#
#     def getNextNode(self):
#         return self.nextNode
#
#     def setNextNode(self, val):
#         self.nextNode = val
#
# class LinkedList:
#
#     def __init__(self, head=None):
#         self.head = head
#         self.size = 0
#
#     def getSize(self):
#         return self.size
#
#     def addNode(self, data):
#         newNode = Node(data, self.head)
#         self.head = newNode
#         self.size += 1
#         return True
#
#     def printNode(self):
#         curr = self.head
#         while curr:
#             print(curr.data)
#             curr = curr.getNextNode()
#
#
# myList = LinkedList()
# print("Inserting")
# print(myList.addNode(5))
# print(myList.addNode(15))
# print(myList.addNode(25))
# print("Printing")
# myList.printNode()
# print("Size")
# print(myList.getSize())

# === Output === #

# Inserting
# True
# True
# True
# Printing
# 25
# 15
# 5
# Size
# 3

# ============================ Problem 7 ========================================= #

# def recur_sum(n):
#     if len(n) == 0:
#         return 0
#     else:
#         return n[0] + recur_sum(n[1:])
#
# num_list=[1,2,3,4,-5,-10]
#
# num_list = [item for item in num_list if item >= 0]
# print("The sum of positive numbers excluding negatives: {}".format(recur_sum(num_list)))

# === Output === #

# The sum of positive numbers excluding negatives: 10

# ============================ Problem 8 ========================================= #

# from statistics import mode
# l=[0,1,0,1,1,1,0]
#
# frequent=mode(l)
#
# if frequent == 0:
#     print("The list has even parity.")
# elif frequent == 1:
#     print("The list has odd parity.")


# === Output === #

# The list has odd parity.


# ============================ Problem 9 ========================================= #

# def recursiveCount(lst,key):
#     if lst == []:
#         return 0
#     if lst[0] == key:
#         return 1 + recursiveCount(lst[1:],key)
#     else:
#         return 0 + recursiveCount(lst[1:],key)
#
# print(recursiveCount([1,2,34,4,5,1,1,2,2,5],1))

# 3

# ============================ Problem 10 ========================================= #


# def findMean(A, N):
#
#     if (N == 1):
#         return (float)
#         A[N - 1]
#     else:
#         return ((float)(findMean(A, N - 1) * (N - 1) +
#                     A[N - 1]) / N)
#
# def main():
#
#     Mean = 0
#
#     A = {1, 2, 3, 4, 5}
#
#     N = (A) / (A[0])
#     print("%.2f\n", findMean(A, N))
#     return 0


# ============================ Problem 11 ========================================= #

# l=[20,10,40,5,60]
# l_1=l[::-1]
# print("The Reversed list is: {}".format(l_1))

# === Output === #

# The Reversed list is: [60, 5, 40, 10, 20]


# =========================== Problem 12 ============================================ =#

# class Node(object):
#     def __init__(self, data):
#         self.root = data
#         self.left = None
#         self.right = None
#
# class BST(object):
#     def __init__(self):
#         self.top = None
#
#     def recursBST(self, node, data):
#         if node is None:
#             node = Node(data)
#         elif self.top.root > data:
#             node.left = self.recursBST(node.left, data)
#         elif  self.top.root < data:
#             node.right = self.recursBST(node.right, data)
#
#         return node
#
#     def insert(self, data):
#         self.top = self.recursBST(self.top, data)
#
# conv = BST()
# print(conv.insert(8))
# print(conv.insert(3))
# print(conv.insert(6))
# print(conv.insert(1))
# print(conv.insert(-1))
# print(conv.insert(10))
# print(conv.insert(14))
# print(conv.insert(50))


# ====================================== Problem 13 ======================================= #


data = []
print("This program will make mean, median and mode very easy!")
print("\nFirst, we need to enter some numbers!")

num = input("Type your first number: ")
while num:
    data.append(float(num))  # Converts num into a float so we can do division
    print("\n", data)
    num = input("Add another number, or press enter to move on.")

total = sum(data)
length = len(data)
print("\n\nThe Mean Is:", total / length)

data.sort()
print("\n\nHere's the list in numerical order:\n", data)

oddness = length % 2
half = length // 2
if oddness == 1:
    print("The median is:", data[half])
else:
    low = float(data[half - 1])
    high = float(data[half])
    print("The median is half way between", low, "and", high)
    print("That makes it:", low + (high - low) / 2)

hits = []
for item in data:
    tally = data.count(item)
    values = (tally, item)

    if values not in hits:
        hits.append(values)
hits.sort(reverse=True)
if hits[0][0] > hits[1][0]:
    print("\n\nThe mode is:", hits[0][1], "hit appeared", hits[0][0], "times.")
else:
    print("There is not a mode")


# === Output === #

# This program will make mean, median and mode very easy!
#
# First, we need to enter some numbers!
# Type your first number: 15
#
#  [15.0]
# Add another number, or press enter to move on.14
#
#  [15.0, 14.0]
# Add another number, or press enter to move on.20
#
#  [15.0, 14.0, 20.0]
# Add another number, or press enter to move on.14
#
#  [15.0, 14.0, 20.0, 14.0]
# Add another number, or press enter to move on.45
#
#  [15.0, 14.0, 20.0, 14.0, 45.0]
# Add another number, or press enter to move on.75
#
#  [15.0, 14.0, 20.0, 14.0, 45.0, 75.0]
# Add another number, or press enter to move on.
# 78
#
#
# The Mean Is: 30.5
#
#
# Here's the list in numerical order:
#  [14.0, 14.0, 15.0, 20.0, 45.0, 75.0]
# The median is half way between 15.0 and 20.0
# That makes it: 17.5
#
#
# The mode is: 14.0 hit appeared 2 times.

