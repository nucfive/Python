#列表白表达式
#取出一个列表中某些数据 一般做法
newList = ['魏如峰', '微软', '张鑫', '李霖', '李龙']
# emptyList = []
# for name in newList:
#     if name.startswith('李'):
#         emptyList.append(name)
# print(emptyList)
#第二种表达形式
print([name for name in newList if name.startswith('魏')])
