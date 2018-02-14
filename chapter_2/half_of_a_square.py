# ================================== CHAPTER 2 Problems ============================================ #

# ======================== Problem 1 ===================================== #

# for e in range (5,0,-1):
#     print('' + e * '#')

# === Output === #

#####
####
###
##
#

# ======================== Problem 2 ====================================== #

# for i in range (0,5):
#     for j in range(0,5):
#         print('#',end="")
#     print('\r')

# === Output  ==== #

#####
#####
#####
#####
#####

# ======================== Problem 3 ====================================== #

# for i in range(0,5):
#     print(5-i)
# print("\r")

# === Output === #

# 5
# 4
# 3
# 2
# 1

# ======================== Problem 4 ====================================== #

# for i in range(0,3):
#     for j in range(0,i+1):
#         print("*", end="")
#     print("\r")
#
# for e in range (4,0,-1):
#     print((11) * '' + e * '*')

# === Output === #

# *
# **
# ***
# ****
# ***
# **
# *

# ======================== Problem 5 ====================================== #

# number=int(input("Enter a number between 0-9: "))
# doubleDigit=number*2
# if doubleDigit >= 10:
#     sum = 1 + doubleDigit % 10
# else:
#     sum=doubleDigit
# print("Sum of digits in double number: ",sum)

# === Output === #

# Enter a number between 0-9: 2
# Sum of digits in double number:  4

# ======================== Problem 6 ====================================== #

# digit=int(input("Enter a One digit Number: "))
# sum = digit - 0
# print("Is the sum of digits {0} ? ".format(sum))

# === Output === #

# Enter a One digit Number: 15
# Is the sum of digits 15 ?.
# ======================== Problem 7 ============
========================== #

# def luhn(n):
#     r = [int(ch) for ch in str(n)][::-1]
#     return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0
#
# l=[49927398716, 499273, 123456, 123578]
# for n in (l):
#     print(n, luhn(n))

# === Output === #

# 49927398716 True
# 499273 False
# 123456 False
# 123578 False

# ======================== Problem 8 ====================================== #

# checksum = 0
# for i in range(1,7):
#     digit=int(input("Enter a six digit number: "))
#     checksum += digit - 0
# print("The Checksum is: ",checksum)
#
# if checksum % 10 == 0:
#     print("Checksum is divisible by 10, Valid.")
# else:
#     print("Checksum is not divisible by 10, Invalid.")

# === Output === #

# Enter a six digit number: 4
# Enter a six digit number: 1
# Enter a six digit number: 1
# Enter a six digit number: 5
# Enter a six digit number: 7
# Enter a six digit number: 8
# The Checksum is:  26
# Checksum is not divisible by 10, Invalid.


# ======================== Problem 9 ====================================== #

# checksum = 0
# position = 1
# digit=int(input("Enter a number with even number of digits: "))
#
# while digit != 10:
#     if position % 2 == 0:
#         checksum += digit - 0
#     else:
#         checksum += 2*(digit - 0)
# digit=int(input())
# position = position + 1
# print("Checksum is: ", checksum)
# if checksum % 10 == 0:
#     print("Checksum is divisible by 10, Valid.")
# else:
#     print("Checksum is not divisible by 10, Invalid.")

# === Output === #

# Enter a number with even number of digits: 10
# 15
# Checksum is:  0
# Checksum is divisible by 10, Valid.


# ======================== Problem 10 ====================================== #

# positiveCount = 0
# negativeCount = 0
#
# for i in range(0,10):
#     number = int(input("Enter {0} Numbers: ".format(i)))
#     if number > 0:
#         positiveCount=positiveCount + 1
#     if number < 0:
#         negativeCount=negativeCount + 1
# print("Do you want the (p)ositive or (n)egative count? ")
# response=str(input())
#
# if response == 'p':
#     print("Positive count is {0}".format(positiveCount))
# if response == 'n':
#     print("Negative count is {0}".format(negativeCount))

# === Output === #

# Enter 0 Numbers: -5
# Enter 1 Numbers: -5
# Enter 2 Numbers: -4
# Enter 3 Numbers: -10
# Enter 4 Numbers: 1
# Enter 5 Numbers: 2
# Enter 6 Numbers: 5
# Enter 7 Numbers: 4
# Enter 8 Numbers: 45
# Enter 9 Numbers: 4
# Do you want the (p)ositive or (n)egative count?
# p
# Positive count is 6

# ======================== Problem 11 ====================================== #

# def doubleDigitValue(digit):
#     doubleDigit=digit
#     if doubleDigit > 10:
#         sum = 1 + doubleDigit % 10
#     else:
#         sum = doubleDigit
#     return sum
#
# oddLengthCheckSum = 0
# evenLengthChecksum = 0
# position = 1
# digit=int(input("Enter a Number: "))
#
# while digit != 10:
#     if position % 2 == 0:
#         oddLengthCheckSum += doubleDigitValue(digit - 0)
#         evenLengthChecksum += digit - 0
#     else:
#         oddLengthCheckSum += digit - 0
#         evenLengthChecksum += doubleDigitValue(digit - 0)
#     digit=int(input())
#     position += 1
# if ((position - 1) % 2 == 0):
#    Checksum=evenLengthChecksum
# else:
#     Checksum=oddLengthCheckSum
# print("CheckSum is: ",Checksum)
#
# if Checksum % 10 == 0:
#     print("Checksum is divisible by 10, valid")
# else:
#     print("CheckSum is not divisible by 10, Invalid")

# === Output === #

# === CASE 1 === #

# Enter a Number: 12
# 10
# CheckSum is:  12
# CheckSum is not divisible by 10, Invalid

# === CASE 2 === #

# Enter a Number: 30
# 10
# CheckSum is:  30
# Checksum is divisible by 10, valid


# ======================== Problem 12 ====================================== #

# from random import seed, shuffle
# #Encoder Function
# def Encoder(user_input,SEED):
#     user_input = user_input.lower()
#     letter = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     Letter_code = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
#     code = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
#     n = []
#     seed(SEED)
#     shuffle(code)
#     for letter in user_input:
#         for let in letter:
#             if letter != " ":
#                 if letter == let:
#                     first = Letter_code[let]
#                     n.append(code[first])
#             else:
#                 n.append("~")
#     return ''.join(n)
#
#Decoder Function
# def Decoder(user_input,SEED):
#     user_input = user_input.lower
#     key_list = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     final = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     seed(SEED)
#     shuffle(key_list)
#     key_code = {}
#     z = 0
#     n = []
#     for key in key_list:
#         key_code[key] = z
#         z += 1
#     for let in user_input:
#         if let != "~":
#             for Ke in key_list:
#                 if let == Ke:
#                     a = key_code[Ke]
#                     n.append(final[a])
#         else:
#             n.append(" ")
#     return ''.join(n)
#
#Prompt
# encode_decode = str(input("Would you like to encode or decode a message?(encode/decode): "))
# encode_decode = encode_decode.lower()
# if encode_decode == "encode":
#     message =input("Message to encode (no puncuation):")
#     SEED = input("Key:")
#     print (Encoder(message,SEED))
# elif encode_decode == "decode":
#     message = input("Message to decode:")
#     SEED = input("Key:")
#     print(Decoder(message,SEED))
# else:
#     print("!!!INVALID RESPONSE!!!")

# === Output === #

# Would you like to encode or decode a message?(encode/decode): encode
# Message to encode (no puncuation):Hello Abrar
# Key:a
# gbjjo~xkdxd

# ======================== Problem 13 ====================================== #

# digitChar=int(input("Enter a three-digit or four-digit number: "))
# threeDigit=(digitChar - 0) * 100
# fourDigit=(digitChar - 0) * 1000
#
# digitChar=int(input("Enter a three-digit or four-digit number: "))
# threeDigit += (digitChar - 0) * 10
# fourDigit += (digitChar - 0) * 100
#
# digitChar=int(input("Enter a three-digit or four-digit number: "))
# threeDigit += (digitChar - 0)
# fourDigit += (digitChar - 0) * 10
#
# if digitChar == 10:
#     print("Number Entered is: ",threeDigit)
# else:
#     fourDigit += (digitChar - 0)
#     print("Number Entered is: ", fourDigit)

# === Output === #

# Enter a three-digit or four-digit number: 120
# Enter a three-digit or four-digit number: 1200
# Enter a three-digit or four-digit number: 450
# Number Entered is:  24495

# ======================== Problem 14 ====================================== #

# number=int(input("Enter a Number from 1-8: "))
#
# if number == 1:
#     outputChar = '!'
#
# elif number == 2:
#     outputChar = '?'
#
# elif number == 3:
#     outputChar = ','
#
# elif number == 4:
#     outputChar = '.'
#
# elif number == 5:
#     outputChar = ' '
#
# elif number == 6:
#     outputChar = ';'
#
# elif number == 7:
#     outputChar = '"'
#
# elif number == 8:
#     outputChar = '/'
#
# print("Equivalent symbol: {}".format(outputChar))

# === Output === #

# Enter a Number from 1-8: 8
# Equivalent symbol: /

# ======================== Problem 15 ====================================== #

# for e in range (8,1,-2):
#     print((8-e) * ' ' + e * '# ')

# === Output === #

# # # # # # # #
  # # # # # #
    # # # #
      # #

# ======================== Problem 16 ====================================== #

# side = int(input("Please input side length of diamond: "))
#
# for x in list(range(side)) + list(reversed(range(side-1))):
#     print('{: <{w1}}{:#<{w2}}'.format('', '', w1=side-x-1, w2=x*2+2))

# === Output === #

# Please input side length of diamond: 5
#     ##
#    ####
#   ######
#  ########
# ##########
#  ########
#   ######
#    ####
#     ##

# ======================== Problem 17 ====================================== #

# result_str=""
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str=result_str+"#"
#         else:
#             result_str=result_str+" "
#     result_str=result_str+"\n"
# print(result_str)

# === Output === #

     ###
    #   #
    #   #
    #####
    #   #
    #   #
    #   #

# ======================== Problem 18 ====================================== #

# def dec_to_bin(x):
#     return int(bin(x)[2:])
#
# x=20
# decimal = 0
#
# binary_value= dec_to_bin(x)
#
# # print("Decimal Number {0}, when converted to binary leads a value {1}".format(x,binary_value))
# for digit in str(binary_value):
#     decimal = decimal *2 + int(digit)
# print("The Binary value {0}, when converted to deci,al leads to {1} ".format(str(binary_value),decimal))


# === Output === #

# Decimal Number 20, when converted to binary leads a value 10100
# The Binary value 10100, when converted to deci,al leads to 20

# ======================== Problem 19 ====================================== #

# def ChangeHex(n):
#     if (n < 0):
#         print(0)
#     elif (n<=1):
#         print(n)
#     else:
#         ChangeHex(n / 16)
#         x =(n%16)
#         if (x < 10):
#             print(x),
#         if (x == 10):
#             print("A"),
#         if (x == 11):
#             print("B"),
#         if (x == 12):
#             print("C"),
#         if (x == 13):
#             print("D"),
#         if (x == 14):
#             print("E"),
#         if (x == 15):
#             print("F")
#
# n= int(input("Enter number: "))
# ChangeHex(n)

# === Output === #

# Enter number: 30
# 0.1171875
# 1.875
# E

# ======================== Problem 20 ====================================== #

# def base_convert(i, b):
#     result = []
#     while i > 0:
#             result.insert(0, i % b)
#             i = i // b
#     return result
#
# print(base_convert(25,9))

# === Output === #

# [2, 7]

# ======================== Problem 21 ====================================== #

# string= "This is a string and the task is to count number of words and finding the length of the longest words and greatest number of vowels."
# word_length_each=[len(x) for x in string.split()]
# # print("The word length of each in the string is {0}".format(word_length_each))
# current_max = 0
# for v in word_length_each:
#     if v>current_max:
#         current_max = v
# # print("The max word length i the list is {}".format(current_max))
#
# # ===== Vowels Code ===== #
#
# words = string.split()
# for word in words:
#     vow = sum(letter in 'aeiou' for letter in word.lower())
    # print("The number of vowels in", word, "are", vow)

# === Output === #

# The word length of each in the string is [4, 2, 1, 6, 3, 3, 4, 2, 2, 5, 6, 2, 5, 3, 7, 3, 6, 2, 3, 7, 5, 3, 8, 6, 2, 7]

# The max word length i the list is 8

# The number of vowels in This are 1
# The number of vowels in is are 1
# The number of vowels in a are 1
# The number of vowels in string are 1
# The number of vowels in and are 1
# The number of vowels in the are 1
# The number of vowels in task are 1
# The number of vowels in is are 1
# The number of vowels in to are 1
# The number of vowels in count are 2
# The number of vowels in number are 2
# The number of vowels in of are 1
# The number of vowels in words are 1
# The number of vowels in and are 1
# The number of vowels in finding are 2
# The number of vowels in the are 1
# The number of vowels in length are 1
# The number of vowels in of are 1
# The number of vowels in the are 1
# The number of vowels in longest are 2
# The number of vowels in words are 1
# The number of vowels in and are 1
# The number of vowels in greatest are 3
# The number of vowels in number are 2
# The number of vowels in of are 1
# The number of vowels in vowels. are 2


# ======================================= Problem 22 ==================================== #

# no = int (input("Enter a number: "))
# space_no = no - 2
# print_line = "   *"*no
# for i in range(1,no+1):
#     if space_no>0:
#         print_line_n = "*"*i+" "*space_no+"*"*i
#         space_no -=2
#         print(print_line_n)

# === Output === #

# *       *
# **     **
# ***   ***
# **** ****