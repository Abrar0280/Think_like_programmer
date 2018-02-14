

# ================================== Problem 1 ========================================= #

# Array=[1,2,3,4,5]
# length=len(Array)
# total=0
# positive_count=0
#
# for i in range(0,length):
#     if Array[i] > 0:
#         total += Array[i]
#         positive_count += 1
# # print(positive_count)
# average=total/positive_count
# print("Average of positive count is: {}".format(average))

# === Output === #

# Average of positive count is: 3.0

# ================================== Problem 2 ========================================= #

import random

DEBUG = False  # If set to true, displays chosen word before each game. For debugging and cheating only :)

DICT_FILE = r"C:\Users\Mohamedabrar.A\Desktop\meat_verbiage_list.txt"
GUESSES = 10


def prompt(s):
    while True:
        ans = input(s + " (Y/n) ").lower()
        if ans in ["y", "n"]:
            return ans == "y"


def loadWords():
    with open(DICT_FILE, "r") as f:
        return f.read().strip().split("\n")


def play(word):
    word = word.lower()
    if DEBUG:
        print("[DEBUG] word is %r" % (word))

    guesses = GUESSES
    toGuess = set(l for l in word.upper() if l.isalpha())
    letters = set()
    while guesses > 0:
        if len(toGuess) == 0:
            print("You win with %d guess%s left!" % (guesses, "" if guesses == 1 else "es"))

            print("The word is %r" % (word))

            return True
        print("=" * 78)

        print("You have %d guess%s left." % (guesses, "" if guesses == 1 else "es"))

        print("Word:    " + " ".join("_" if c in toGuess else c for c in word.upper()))

        print("Letters: " + " ".join(sorted(letters)))

        while True:
            l = input("Choose a letter: ").upper()
            if l.isalpha():
                if l not in letters:
                    letters.add(l)
                    if l in toGuess:
                        toGuess.remove(l)
                        print("Correct!")

                    else:
                        guesses -= 1
                        print("Sorry, not in the word.")

                    break
                else:
                    print("You already chose that letter!")

            else:
                print("That's not a letter!")
    print("=" * 78)
    print("Sorry, you lose.")
    print("The word was: %r" % (word))

    return False

if __name__ == "__main__":
    words = loadWords()
    random.shuffle(words)
    while True:
        play(words.pop())
        if not prompt("Would you like to play again?"):
            break


# === Output === #
#
# Would you like to play again? (Y/n) y
# ==============================================================================
# You have 10 guesses left.
# Word:    _ _ _ _ _ _ _ _
# Letters:
# Choose a letter: f
# Sorry, not in the word.
# ==============================================================================
# You have 9 guesses left.
# Word:    _ _ _ _ _ _ _ _
# Letters: F
# Choose a letter: q
# Sorry, not in the word.
# ==============================================================================
# You have 8 guesses left.
# Word:    _ _ _ _ _ _ _ _
# Letters: F Q
# Choose a letter: a
# Correct!
# ==============================================================================
# You have 8 guesses left.
# Word:    _ A _ A _ _ _ _
# Letters: A F Q
# Choose a letter: s
# Sorry, not in the word.
# ==============================================================================
# You have 7 guesses left.
# Word:    _ A _ A _ _ _ _
# Letters: A F Q S
# Choose a letter: z
# Sorry, not in the word.
# ==============================================================================
# You have 6 guesses left.
# Word:    _ A _ A _ _ _ _
# Letters: A F Q S Z
# Choose a letter: e
# Sorry, not in the word.
# ==============================================================================
# You have 5 guesses left.
# Word:    _ A _ A _ _ _ _
# Letters: A E F Q S Z
# Choose a letter: r
# Sorry, not in the word.
# ==============================================================================
# You have 4 guesses left.
# Word:    _ A _ A _ _ _ _
# Letters: A E F Q R S Z
# Choose a letter: g
# Correct!
# ==============================================================================
# You have 4 guesses left.
# Word:    _ A _ A G _ _ G
# Letters: A E F G Q R S Z
# Choose a letter: i
# Correct!
# ==============================================================================
# You have 4 guesses left.
# Word:    _ A _ A G I _ G
# Letters: A E F G I Q R S Z
# Choose a letter: l
# Sorry, not in the word.
# ==============================================================================
# You have 3 guesses left.
# Word:    _ A _ A G I _ G
# Letters: A E F G I L Q R S Z
# Choose a letter: v
# Sorry, not in the word.
# ==============================================================================
# You have 2 guesses left.
# Word:    _ A _ A G I _ G
# Letters: A E F G I L Q R S V Z
# Choose a letter: n
# Correct!
# ==============================================================================
# You have 2 guesses left.
# Word:    _ A N A G I N G
# Letters: A E F G I L N Q R S V Z
# Choose a letter: m
# Correct!
# You win with 2 guesses left!
# The word is 'managing'

