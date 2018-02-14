import operator

class studentsort():
    def __init__(self,**kwargs):
        self.Name=kwargs

    def details(self):
        sorted_x = sorted(self.Name.items(), key=operator.itemgetter(1))
        print(sorted_x)
        # for k,v in self.Name.items():
        #     print(v)

my_dict={"Jane":80,"John":56,"Basith":99,"Brock":78,"sam":90,"Tom":40}
sort=studentsort(**my_dict)
sort.details()

# === Output === #

# [('Tom', 40), ('John', 56), ('Brock', 78), ('Jane', 80), ('sam', 90), ('Basith', 99)]

