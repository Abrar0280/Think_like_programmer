class Student():
    def __init__(self,lis):
        self.Mul_lis=lis
    def sort(self):
        return sorted(self.Mul_lis, key=lambda x: x[2])

l=[[1000,"John",2],[1001,"Jim",9],[1002,"Jason",1]]
stud=Student(l)
print("The sorted list based on grades: {}".format(stud.sort()))

# === Output === #

# The sorted list based on grades: [[1002, 'Jason', 1], [1000, 'John', 2], [1001, 'Jim', 9]]
