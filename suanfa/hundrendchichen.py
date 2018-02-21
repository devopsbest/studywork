'''
百鸡问题是一个数学问题，出自中国古代约5—6世纪成书的《张邱建算经》
今有鸡翁一，值钱伍；鸡母一，值钱三；鸡鶵三，值钱一。凡百钱买鸡百只，问鸡翁、母、鶵各几何？
公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，如何买？
'''
'''
如果我们用x,y,z分别代表公鸡，母鸡，小鸡的个数
那么我们可以得到两个三元一次方程：
x + y + z = 100
5x + 3y + z/3 =100
如何解这个方程，计算机里面用遍历。
如果都买公鸡，最多买20只；
如果都买母鸡，最多买33只；
可以在这个范围内进行遍历
'''
# 百钱买买百鸡示范编程
def caculate_numbers():
    for cook in range(20):    #公鸡最多买20只，公鸡的遍历
        for hen in range(33): #母鸡最多买33只，母鸡的遍历
            children = 100 - cook - hen  #小鸡的个数
            #小鸡的个数必须是整数，对3求余数为0
            if (children % 3 == 0) and (5 * cook + 3 * hen + children / 3 == 100):
                print("cook:{},hen:{},children{}".format(cook, hen, children))
caculate_numbers()
'''
结果：
cook:0,hen:25,children75
cook:4,hen:18,children78
cook:8,hen:11,children81
cook:
'''