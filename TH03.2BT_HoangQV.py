
#Trang 28
from datetime import datetime
class Person:
    def __init__(self,name,year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight
    def Geeting(self):
        yearold = datetime.now().year
        tuoi = yearold - self.year
        return f"Xin chào {self.name}, bằn năm nay {tuoi} tuổi"
    def bmi_show(self):
        BMI = self.weight / (self.height * self.height)
        if BMI < 18.5:
            print("Underweight")
        elif BMI > 18.5 and BMI < 24.9:
            print("Normal Weight")
        elif BMI > 25 and BMI < 29.9:
            print("Overweight")
        else:
            print("Obese")
        return f"Chỉ số BMI là: {BMI}"
p1 = Person("Nguyen Van A", 1999, 1.7, 70)
print(p1.Geeting())
print(p1.bmi_show())

#Trang 44
