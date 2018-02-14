
class Student_Record_Title():
    def __init__(self,paper_title):
        self.Paper_Title=paper_title
    def Course(self):
        return "The Name of the course is: {}".format(self.Paper_Title)

class Student_Record_Year(Student_Record_Title):
    def __init__(self, paper_title, year):
        Student_Record_Title.__init__(self,paper_title)
        self.Year=year
    def Record_Year(self):
        return "The Record Year is: {}".format(self.Year)

class Student_Record_Audit(Student_Record_Year):
    def __init__(self,paper_title, year,audit):
        Student_Record_Year.__init__(self,paper_title, year)
        self.Audit=audit
    def Student_Audit(self):
        return "The Audit of student: {}".format(self.Audit)

x=Student_Record_Audit("Transforms", 2015, "Yes")
print(x.Course())
print(x.Record_Year())
print(x.Student_Audit())

# === Output === #

# The Name of the course is: Transforms
# The Record Year is: 2015
# The Audit of student: Yes
