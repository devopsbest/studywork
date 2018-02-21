'''
不用内建函数，对一个列表求最大值，以及对列表按照从小到大排序
'''
lista = [1, 7, 45, 78, 33, 54, 89,64]
#print(max(lista))  # 用内建函数求最大值
#print(sorted(lista)) #用内建函数排序
'''
如果不用内建函数，可以这么考虑：
定义一个变量，给他赋一个值，
姑且认为这个值是最大的(一般是第一个元素，称他为哨兵)
然后列表遍历，每个值跟哨兵的值比较，如果比哨兵值大的，就给哨兵
所以遍历完列表，哨兵的值就是最大的
'''
#方法一
def get_max(obj):
    maxvalue = obj[0]            #第一个值赋给哨兵
    for i in range(1, len(obj)): #用for循环列表下标
        if obj[i] > maxvalue:    #判断是否比哨兵的值大
            maxvalue = obj[i]    #比哨兵值大，给哨兵
    return maxvalue              #循环结束，返回哨兵的值，也就是最大值
result = get_max(lista)          #调用这个函数，将函数返回值，赋给一个变量
print(result)                    #打印这个最大值
#方法二
def get_max_value(obj):
    max_value =0                #给哨兵初始值赋0
    for i in obj:               #用for迭代列表元素
        if i > max_value:
            max_value = i
    return max_value
print(get_max_value(lista))
#方法三
def get_maxx(obj):
    n = 0                       #循环计数器，初始值赋0
    max_value=0                 #哨兵的初始值赋0
    while n < len(obj):         #用while循环到列表的边界
        if obj[n] > max_value:  #判断是否比哨兵的值大
            max_value =obj[n]   #比哨兵值大，给哨兵
        n +=1                   #计数器+1
    return max_value
print(get_maxx(lista))
#排序，用到了冒泡算法
#冒泡算法，可参照 http://www.cnblogs.com/qlshine/p/6017957.html
#冒泡算法，可以理解为矮子里面挑长子
def sort_list(obj):
    for i in range(len(obj)):           # 这个循环负责设置冒泡排序进行的次数
        for j in range(i+1,len(obj)):   # ｊ为列表下标，理解为剩下的矮子
            if obj[i] > obj[j]:         #  找到了一个长子
                obj[i], obj[j] = obj[j], obj[i]  #长子站后面去
    return obj                          # 返回一个排好队的队列
print(sort_list(lista))
#方法二
def bubbleSort(nums):
    for i in range(len(nums)-1):        # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标，理解为剩下的矮子
            if nums[j] > nums[j+1]:     #  找到了一个长子
                nums[j], nums[j+1] = nums[j+1], nums[j] #长子站后面去
    return nums                         # 返回一个排好队的队列
print(bubbleSort(lista))