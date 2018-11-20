class Father:
    def eat(self):
        print("father can eat!")

class Son(Father):
    #pass #pass是关键字，目的是让编译通过
    def eat(self):
        print("son can eat !") #重载，
my_son = Son()
my_son.eat()