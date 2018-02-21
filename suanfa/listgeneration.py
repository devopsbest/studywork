'''
求下列代码的输出结果
'''
mylist = [108, 20, 78, 15, 8, 2, 5, 3, 11]
result = [x for x in mylist[::2] if x % 2 == 0]
print(result)
'''
答案是：[108, 78, 8]
安老师点评：
这是一个列表生成式
主要考列表生成式是否理解？
列表切片，if, for
题目主要考察
mylist[::2] if x % 2 == 0
是考察每两个数，就是间隔一个数，
并且是偶数的
'''
# 等价
mylist = [108, 20, 78, 15, 8, 2, 5, 3, 11]
result =[]
for x in mylist[::2]:
    if x%2 ==0:
        result.append(x)
print(result)