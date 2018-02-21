l = [34, 16, 78, 2, 34, 56, 5]

for i in range(len(l)-1):
    print('------' * 9)
    print('待操作的列表--->', l, '操作索引--->', i)
    print('------' * 9)
    for j in range(i+1, len(l)):
        print(l[i], l[j])
        if l[i] > l[j]:
            print('调换位置%s, %s' %(l[j], l[i]))
            l[i], l[j] = l[j], l[i]
            print('调换完位置的列表--->', l)

print(l)

