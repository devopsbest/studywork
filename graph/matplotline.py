import matplotlib.pyplot as plt


transation= [300,456,564,439,376]
user_number = [200,300,400,500,600]
# fig = plt.figure()
fig = plt.figure(figsize=(10, 12)) # figsize=(10, 12)参数为手动设定区域（长，宽）的大小


plt.xticks(rotation=20) # 旋转20度
plt.xlabel('User number')
plt.ylabel('Transation')
plt.title('Performance--Transation')

plt.plot(user_number, transation)

plt.show()