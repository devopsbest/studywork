'''
别人的一个面试题
请定义一个函数，实现如下输入与输出：
请输入一个整数：8
       ********
      *******
     ******
    *****
   ****
  ***
 **
*
'''
#安老师示范代码
def print_something():
    numbers = int(input("请输入一个整数："))
    if numbers > 0 and isinstance(numbers, int):
        while numbers > 0:
            print(" " * (numbers - 1) + "*" * numbers)
            print("\n")
            numbers -= 1
    else:
        print("您输入不符合要求")
print_something()