#if 条件 elif 条件：else：

#输入一个年龄用input()
# age = input("please input your age : ")
# print(type(age)) #age 是string类型，变量是根据你所输入的类型来确定
#将age强转成int型
age = int(input("please input your age : "))
# print(type(age))
#if con1 elseif con2: else:
if age > 18:
    print("you can smoke!")
elif age == 21:
    print("you can mermory")
else:
    print("ok ok!")
    ####


