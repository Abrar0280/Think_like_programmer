from tkinter import *
from random import choice
from hangman_ascii import HANGMAN

class Application(Frame):

    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.lives = 7
        self.guess_string = ""
        self.word = self.random_word()
        self.grid()
        self.create_widgets()

    def random_word(self):
        word_list = ["banana","bob","apple","juicy","cat","wolf","crazy"]
        return choice(word_list)

    def limit_entry(self,*args):
        value = self.user_entry.get()
        if len(value) > 1:
            self.user_entry.set(value[:1])

    def reset(self):
        self.word = self.random_word()
        self.guess_string = ""
        self.lives = 7
        self.display_word.delete(0.0, END)
        self.display_attempt.delete(0.0, END)
        self.hangman.set(HANGMAN[0])

    def create_widgets(self):
        self.instr_lbl = Label(self, text="Type a Letter:")
        self.instr_lbl.grid(row=2, column=0, sticky="wens", pady=2)

        self.user_entry = StringVar()
        self.user_entry.trace('w', self.limit_entry)
        self.guess_ent = Entry(self, textvariable=self.user_entry,justify="center")
        self.guess_ent.grid(row=3, column=0, sticky="n", pady=2)

        self.submit_bttn = Button(self, text="Submit", height=1, command=self.game)
        self.submit_bttn.grid(row=4, sticky="wens")

        self.reset_bttn = Button(self, text="Reset", height=1, command=self.reset)
        self.reset_bttn.grid(row=1, sticky="wens", pady = 15)

        self.display_word = Text(self, width=5, height=1)
        self.display_word.grid(row=5, column=0, sticky="wens")

        self.display_attempt = Text(self, width=5, height=1)
        self.display_attempt.grid(row=6, column=0, sticky="wens")

        self.hangman = StringVar()
        self.hangman.set(HANGMAN[0])
        self.hm_lbl = Label(self, textvariable=self.hangman,font=("arial",18),justify="left")
        self.hm_lbl.grid(row=0, column=0, sticky="wn")

    def find_letters(self,word, guessed):
        self.found = ' '.join([ch if ch in guessed else '_' for ch in word])
        return self.found

    def game(self):
        if self.lives != 0:
            user_letter = self.guess_ent.get()

            if len(user_letter) > 0 and user_letter.isalpha():
                if self.guess_string == "" and user_letter not in self.word:
                    self.hangman.set(HANGMAN[len(HANGMAN) - self.lives])
                    self.guess_string += user_letter[0]
                    self.lives -= 1
                elif user_letter in self.word:
                    self.guess_string += user_letter[0]
                elif user_letter not in self.guess_string:
                    self.hangman.set(HANGMAN[len(HANGMAN) - self.lives])
                    self.guess_string += user_letter[0]
                    self.lives -= 1

            self.letters_found = self.find_letters(self.word,self.guess_string)

            self.display_word.delete(0.0, END)
            self.display_word.insert(0.0, self.letters_found)

            self.display_attempt.delete(0.0, END)
            self.display_attempt.insert(0.0, "Lives: " + str(self.lives))
            self.guess_ent.delete(0, "end")
            if "_" not in self.letters_found:
                self.display_attempt.delete(0.0, END)
                self.display_attempt.insert(0.0, "You win!")
                self.hangman.set(HANGMAN[0])
        else:
            self.display_word.delete(0.0,END)
            self.display_word.insert(0.0, self.word.replace(""," ")[1:-1])
            self.display_attempt.delete(0.0, END)
            self.display_attempt.insert(0.0, "You lose.")

root = Tk()
root.geometry("100x510")
app = Application(root)
root.mainloop()