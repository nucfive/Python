# oob
class Student():
    name = "wrf"
    age = "19"
    def eat(self):#self
        print(self.name + " student can eat, and he is " + self.age)
    def study(self):
        print("student can study")

wrf = Student()
wrf.eat()
wrf.study()