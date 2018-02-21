import matplotlib.pyplot as plt

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cost = [8, 7, 9, 9, 3, 10, 10, 12, 8, 6, 11, 10]
profit = [12, 11, 11, 13, 5, 11, 13, 15, 10, 9, 12, 13]

bar1 = plt.barh(month, profit, 0.5, color='y', linewidth = 0, align ='center')
bar2 = plt.barh(month, cost, 0.5, color='g', linewidth = 0, align ='center')

plt.legend((bar1[0], bar2[0]), ('Profits', 'Costs') )

plt.show()