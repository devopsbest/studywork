import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 8))  # figsize=(6, 8)参数为手动设定区域（长，宽）的大小

plt.xlabel('User number')
plt.ylabel('performace usage')
plt.title('Performance--Testing')

user_number = [200, 300, 400, 500, 600]
test_part1 = [139, 158, 269, 312, 201]
test_part2 = [201, 212, 243, 255, 289]
test_part3 = [190, 219, 222, 235, 245]
test_part4 = [189, 190, 199, 178, 175]
test = [user_number, test_part1, test_part2, test_part3, test_part4]


colors = ['red', 'blue', 'green', 'orange']
for i in range(1, 5):
    label = "test{}".format(i)
    plt.plot(test[0], test[i], c=colors[i - 1], label=label)  # 把label=label加进去
plt.legend(loc='best')  # 用这句把提示标签画出来，loc参数决定标签在图中放的位置
# print(help(plt.legend)) # 查看plt.legend函数都有什么参数可选
plt.show()
