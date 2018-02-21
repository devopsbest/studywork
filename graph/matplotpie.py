import matplotlib.pyplot as plt

fracs = [45, 30, 25]             #每一块占得比例，总和为100
explode=(0, 0, 0.08)             #离开整体的距离，看效果
labels = 'coding', 'commnication', 'professional'  #对应每一块的标志

plt.pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90, colors = ("g", "r", "y"))
                                 # startangle是开始的角度，默认为0，从这里开始按逆时针方向依次展开

plt.title('Performance review for Anderson')   #标题

plt.legend(loc='best')
#print(help(plt.legend()))

plt.show()