
# ============================== Problem 1 ======================================== #

# Array=[1,2,3,4,5,6,7,8,9,12,13,14]
# print(Array)
# for i in range(0,12):
#     Array[i]=-1
# print(Array)

# === Output === #

# Before = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14]
# After = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# ============================== Problem 2 ======================================== #

# copying and list to other
# import copy
# Array=[1,2,3,4,5,6,7,8,9,12,13,14]
# copy_Array=copy.copy(Array)
# print(copy_Array)

# === Output === #

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14]

# ============================== Problem 2 ======================================== #

# x=3 in [1, 2, 3]
# # print(x)
#
# getting_position = [i for i,x in enumerate([1,2,3,4,5,6,7,8,9,12,13,14]) if x==13]
# print(getting_position)

# ============================== Problem 3 ======================================== #

# Array=[1,2,3,4,5,6,7,8,9,12,13,14]
# length_array=len(Array)
# # print(length_array)
# highest_value=Array[0]
#
# for i in range(0,length_array):
#     if Array[i] > highest_value:
#         highest_value=Array[i]
#         print(highest_value)

# ===  Output === #

# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 12
# 13
# 14

# ============================== Problem 4 ======================================== #

# def partition(arr, low, high):
#     i = (low - 1)
#     pivot = arr[high]
#
#     for j in range(low, high):
#
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i])
#

# === Output === #

# Sorted array is:
# 1
# 5
# 7
# 8
# 9
# 10

# ============================== Problem 5 ======================================== #

# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i])

# === Output +++ #

# Sorted array is:
# 5
# 6
# 11
# 12
# 13

# ============================== Problem 6 ======================================== #

# gradeArray=[82,45,12,78,95,64,13,65,52,44]
# length=len(gradeArray)
# sum=0
# for i in range(0,length):
#     sum += gradeArray[i]
# average= sum/length
# print("The average of elements in the list {0}".format(average))

# === Output === #

# The average of elements in the list 55.0

# ============================== Problem 7 ======================================== #

# from statistics import mode
# repeated_values=mode([1, 1, 2, 3, 3, 3, 3, 4])
# print("The Mode of the list is: {0}".format(repeated_values))

# === Output === #

# The Mode of the list is: 3

# ============================== Problem 8 ======================================== #

# class Student:
#
#     def __init__(self,roll_no,name,grade):
#         self.Roll_no=roll_no
#         self.Name=name
#         self.Grade = grade
#
#     def details(self):
#         return "The roll_no: {0}, Name: {1}, Grade: {}".format(self.Roll_no,self.Name,self.Grade)
#
# class Average(Student):
#     def __init__(self,roll_no,grade,name):
#         super().__init__(roll_no,grade,name)
#
#     def average(self):
#         Average = len(str(self.Grade))
#         return Average
#
# l=[[1000,"Abrar",100000],[10001,"Rahman",90000000],[10002,"Basith",1010102]]
# x=Average(1000,"Abrar",90)
# print("The length of grade value is: {0}".format(x.average()))

# === Output === #

# The length of grade value is: 2

# ============================== Problem 9 ======================================== #

# def arrayAverage(Array,length):
#     sum=0
#     for i in range(0,length):
#         sum += Array[i]
#     average=(sum + 0.5) / length
#     return average
#
# Array=[1,2,3,4,5]
# length=len(Array)
#
# print("The Average of the terms in the list is: {}".format(arrayAverage(Array,length)))

# === Output === #

# The Average of the terms in the list is: 3.1

# ============================== Problem 10 ======================================== #

# class Student():
#     def __init__(self,lis):
#         self.Mul_lis=lis
#     def sort(self):
#         return sorted(self.Mul_lis, key=lambda x: x[2])
#
# l=[[1000,"John",2],[1001,"Jim",9],[1002,"Jason",1]]
# stud=Student(l)
# print("The sorted list based on grades: {}".format(stud.sort()))

# === Output === #

# The sorted list based on grades: [[1002, 'Jason', 1], [1000, 'John', 2], [1001, 'Jim', 9]]

# ============================== Problem 11 ======================================== #

# sales=[[1856,498,30924,328,2653,387,3754,387587,2873,276,32],
#        [5665,5456,3983,6464,9957,4785,3875,3838,4959,1122,7766,2534],
#        [23,55,67,99,264,376,232,223,4546,564,4544,3434]]

# highest=sales[0][0]
# # print(highest)
# for agent in range(0,3):
#     for months in range(0,11):
#         if sales[agent][months] > highest:
#             highest=sales[agent][months]
#             print("The highest value is: {0}".format(highest))

# def arrayAverage(Array,length):
#     sum=0
#     for i in range(0,length):
#         sum += Array[i]
#     average=(sum + 0.5) / length
#     return average
#
# highest_average=arrayAverage(sales[0],11)
# for agent in range (0,3):
#     agent_average=arrayAverage(sales[agent],11)
#     if agent_average > highest_average:
#         highest_average=agent_average
# print("The highest averaqge is: {0}".format(highest_average))


# # === Output === #
#
# # The highest value is: 30924
# # The highest value is: 387587
#
# # The highest averaqge is: 39197.13636363636


# ============================== Problem 12 ======================================== #

# def arraySortedOrNot(arr):
#     n = len(arr)
#
#     if n == 1 or n == 0:
#         return True
#
#     return arr[0] <= arr[1] and arraySortedOrNot(arr[1:])
#
#
# arr = [100, 20, 23, 23, 45, 78]
#
#
# if arraySortedOrNot(arr):
#     print("Yes, The array is sorted")
# else:
#     print("No, Array is not sorted!")

# === Output === #

# arr = [20, 23, 23, 45, 78, 88]
# Yes, The array is sorted

# arr = [100, 20, 23, 23, 45, 78]
# No, Array is not sorted!

# ============================== Problem 13 ======================================== #

# === Substitution Cipher === #

# import random
#
# alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
# key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
# plaintext = "Hey, this is really fun!"
#
# def makeKey(alphabet):
#    alphabet = list(alphabet)
#    random.shuffle(alphabet)
#    return ''.join(alphabet)
#
# def encrypt(plaintext, key, alphabet):
#     keyIndices = [alphabet.index(k.lower()) for k in plaintext]
#     return ''.join(key[keyIndex] for keyIndex in keyIndices)
#
# def decrypt(cipher, key, alphabet):
#     keyIndices = [key.index(k) for k in cipher]
#     return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)
#
# cipher = encrypt(plaintext, key, alphabet)
#
# print(plaintext)
# print(cipher)
# print(decrypt(cipher, key, alphabet))

# === Output === #

# Hey, this is really fun!
# v! zmhvxdmxdmo!nll mikbg
# hey, this is really fun!


# ============================== Problem 14 ======================================== #

# from statistics import mode
# frequent_occuring=mode([1, 1, 2, 3, 3, 3, 3, 4])
# print("The frequently occuring term ihe list is: {0}".format(frequent_occuring))

# === Output === #

# The frequently occuring term ihe list is: 3
