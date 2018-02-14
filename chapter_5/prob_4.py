class Menu():
    def __init__(self):
        self.buttonlist = []

class AV(Menu):
    def __init__(self, num):
        Menu.__init__(self)
        self.buttonlist.append(num)
        print(self.buttonlist)

class Main(Menu):
    def __init__(self, num):
        Menu.__init__(self)
        self.buttonlist.append(num)
        print(self.buttonlist)

av = AV(12)
main = Main(14)
main_1=Main(15)


# === Output === #

# [12]
# [14]
# [15]