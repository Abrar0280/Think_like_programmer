
class Student():
    def __init__(self,stu_id, name, grade):
        self.ID=stu_id
        self.Name=name
        self.Grade=grade

    def details(self):
        return "ID: {0}, Name: {1}, Grade: {2}".format(self.ID,self.Name,self.Grade)

    def total(self):
        if self.Grade >= 93 and self.Grade <= 100:
            print("Score Range: 93-100 and has Grade: A")
        elif self.Grade >= 90 and self.Grade <= 92:
            print("Score Range: 90-92 and has Grade: A-")
        elif self.Grade >= 87 and self.Grade <= 89:
            print("Score Range: 87-89 and has Grade: B+")
        elif self.Grade >= 83 and self.Grade <= 86:
            print("Score Range: 83-86 and has Grade: B")
        elif self.Grade >= 80 and self.Grade <= 82:
            print("Score Range: 80-82 and has Grade: B-")

s=Student(1,"Abrar",90)
s_1=Student(2,"Mohamed",95)
s_2=Student(3,"Rahman",100)
s_3=Student(4,"Hassh",99)
s_4=Student(5,"Basith",80)
s_5=Student(6,"Raghul",84)
s.total()
s_1.total()
s_2.total()
s_3.total()
s_4.total()
s_5.total()

# === Output === #

# Score Range: 90-92 and has Grade: A-
# Score Range: 93-100 and has Grade: A
# Score Range: 93-100 and has Grade: A
# Score Range: 93-100 and has Grade: A
# Score Range: 80-82 and has Grade: B-
# Score Range: 83-86 and has Grade: B
