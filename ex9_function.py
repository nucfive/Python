#function def nanme(): 下定义
#如果函数有返回值可以如下写法
#def function(a, b):
#   return a + b
def function1():
    print("hello world")
function1()
def sum(num1, num2):
    print("num1 + num2 = " + str(num1 + num2))
sum(10, 20)

def sum1(num1, num2):
    return  num1 + num2
a = sum1(10, 20)
print(a)
#带有默认值的函数
def convert(weight):
    ponds = weight / 0.45
    print(ponds)

def convert2(weight = 100):
    ponds = weight / 0.45
    print(ponds)

convert(100)
convert2()
convert2(weight=200)