class Student:

    def __init__(self,roll_no,name,grade):
        self.Roll_no=roll_no
        self.Name=name
        self.Grade = grade

    def details(self):
        return "The roll_no: {0}, Name: {1}, Grade: {}".format(self.Roll_no,self.Name,self.Grade)

class Average(Student):
    def __init__(self,roll_no,grade,name):
        super().__init__(roll_no,grade,name)

    def average(self):
        Average = len(str(self.Grade))
        return Average

l=[[1000,"Abrar",100000],[10001,"Rahman",90000000],[10002,"Basith",1010102]]
x=Average(1000,"Abrar",90)
print("The length of grade value is: {0}".format(x.average()))

# === Output === #

# The length of grade value is: 2