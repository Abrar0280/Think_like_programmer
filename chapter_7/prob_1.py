
class studentcollection():
    def __init__(self,id,grades=None):
        self.ID=id
        if grades is None:
            grades=[]
        self.Grades=grades
    def based_on_high_grade(self):
        highest_marks=max(self.Grades)
        # print(highest_marks)
        print("The leader of the class based on the highest score is: {} marks".format(highest_marks))
    def based_on_ID(self):
        last_element=self.ID[-1]

        print("The leader of the class based on the last member is: {}".format(last_element))

student=studentcollection([1,2,3,4,5,6,7,8,9],[10,20,45,54,60,34,89,90,26])
student.based_on_high_grade()
student.based_on_ID()


# === Output === #

# The leader of the class based on the highest score is: 90 marks
# The leader of the class based on the last member is: 9
