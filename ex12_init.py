class Students:
    def __init__(self, name, age): #类似构造函数功能
        self.name = name
        self.age = age
    def work(self):
        print(self.name,"can work!")
        print(self.name,"is", self.age)

s1 = Students(name = "wrf", age = 18)
s1.work()
s2 = Students("wrf1", 19)
s2.work()
