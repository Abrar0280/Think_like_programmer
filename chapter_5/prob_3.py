class Automobile():
    def __init__(self,manu_name,model_name,model_year):
        self.Manufacture_Name=manu_name
        self.Model_Name=model_name
        self.Model_Year=model_year
    def details(self):
        return "{0} {1} {2}".format(self.Model_Year, self.Manufacture_Name,self.Model_Name)

vehicle=Automobile("Chevrolet","Impala",1957)
print(vehicle.details())

# === Output === #

# 1957 Chevrolet Impala
