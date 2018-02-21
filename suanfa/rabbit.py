'''
题目：说有一对可爱的兔子，出生后的第三个月开始，
每一月都会生一对小兔子。当小兔子长到第三个月后，
也会每个月再生一对小小兔子.

要求：假设条件，兔子都不死的情况下，问每个月的兔子总数为多少？

思路：兔子的规律为数列0,1,1,2,3,5,8,13,21......似斐那波契数列的感觉
'''


# 第一种采用迭代的方式实现
def func(num):
    numList = [0, 1]
    for i in range(num - 2):
        numList.append(numList[-2] + numList[-1])
    return numList


mouth = int(input("亲！请输入月份："))

f = func(mouth)
# f[len(f)-1]*2,计算出列表中最后一位数值，乘以2的原因是兔子都是成对计算的
print("第%d个月的兔子数量是：%d" % (mouth, f[len(f) - 1] * 2))

# 第二种采用递归的方式实现
def func(num):
    if num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = func(num - 2) + func(num - 1)
    return result


mouth = int(input("亲！请输入月份："))
n = 0
while n < mouth:
    print("第%d个月的兔子总数是：%d" % (n + 1, func(n) * 2))
    n += 1


# 第三种实现方案：最简单的循环计算每项的值
def func(num):
    a = 0
    b = 1
    m = 0
    while m < num:
        print("第%d个月兔子的总数是：%d" % (m + 1, a * 2))
        a, b = b, a + b
        m += 1


mouth = int(input("亲！请输入月份："))
func(mouth)