#文档的读写 使用open()
#第一种读写方式
# f1 = open("test.txt")
# text = f1.read()
# print(text)
# f1.close()

f1 = open("test.txt", "a") #"w", 覆盖的写 "a" 接着原来的写，不覆盖
f1.write("wrf wrf \n")
f1.close()



