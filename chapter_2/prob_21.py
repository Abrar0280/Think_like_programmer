string= "This is a string and the task is to count number of words and finding the length of the longest words and greatest number of vowels."
word_length_each=[len(x) for x in string.split()]
# print("The word length of each in the string is {0}".format(word_length_each))
current_max = 0
for v in word_length_each:
    if v>current_max:
        current_max = v
# print("The max word length i the list is {}".format(current_max))

# ===== Vowels Code ===== #

words = string.split()
for word in words:
    vow = sum(letter in 'aeiou' for letter in word.lower())
    print("The number of vowels in", word, "are", vow)

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

