
# ============================ Problem 1 ========================================= #

# class studentcollection():
#     def __init__(self,id,grades=None):
#         self.ID=id
#         if grades is None:
#             grades=[]
#         self.Grades=grades
#     def based_on_high_grade(self):
#         highest_marks=max(self.Grades)
#         # print(highest_marks)
#         print("The leader of the class based on the highest score is: {} marks".format(highest_marks))
#     def based_on_ID(self):
#         last_element=self.ID[-1]
#
#         print("The leader of the class based on the last member is: {}".format(last_element))
#
# student=studentcollection([1,2,3,4,5,6,7,8,9],[10,20,45,54,60,34,89,90,26])
# student.based_on_high_grade()
# student.based_on_ID()


# === Output === #

# The leader of the class based on the highest score is: 90 marks
# The leader of the class based on the last member is: 9

# ============================ Problem 2 ========================================= #

# some_list = [["X", '4x01'], ["X", '3x02'], ["X", '4x02'], ["X", '3x01']]
#
# l = sorted(some_list, key=lambda x:x[-2:])
# print(l)

# import operator
#
# class studentsort():
#     def __init__(self,**kwargs):
#         self.Name=kwargs
#
#     def details(self):
#         sorted_x = sorted(self.Name.items(), key=operator.itemgetter(1))
#         print(sorted_x)
#         # for k,v in self.Name.items():
#         #     print(v)
#
# my_dict={"Jane":80,"John":56,"Basith":99,"Brock":78,"sam":90,"Tom":40}
# sort=studentsort(**my_dict)
# sort.details()

# === Output === #

# [('Tom', 40), ('John', 56), ('Brock', 78), ('Jane', 80), ('sam', 90), ('Basith', 99)]


# ============================ Problem 3 ========================================= #

# class Student_Record_Title():
#     def __init__(self,paper_title):
#         self.Paper_Title=paper_title
#     def Course(self):
#         return "The Name of the course is: {}".format(self.Paper_Title)
#
# class Student_Record_Year(Student_Record_Title):
#     def __init__(self, paper_title, year):
#         Student_Record_Title.__init__(self,paper_title)
#         self.Year=year
#     def Record_Year(self):
#         return "The Record Year is: {}".format(self.Year)
#
# class Student_Record_Audit(Student_Record_Year):
#     def __init__(self,paper_title, year,audit):
#         Student_Record_Year.__init__(self,paper_title, year)
#         self.Audit=audit
#     def Student_Audit(self):
#         return "The Audit of student: {}".format(self.Audit)
#
# x=Student_Record_Audit("Transforms", 2015, "Yes")
# print(x.Course())
# print(x.Record_Year())
# print(x.Student_Audit())

# === Output === #

# The Name of the course is: Transforms
# The Record Year is: 2015
# The Audit of student: Yes


# ============================ Problem 4 ========================================= #