# 作业： 定义函数，模拟shell登陆，登陆失败超过三次提示并退出
# 自己设计用例，检测你的代码

count = 3


def input_account():
    username = raw_input("please input username:")
    password = raw_input("please input username:")
    return username, password


def check_result():
    for number in range(count):
        username, password = input_account()
        print("login {} times".format(number + 1))
        if username == 'root' and password == 'root':
            print("Welcome!")
            break
        else:
            print("your username and password is wrong")
            print("you fail {} times, you have {} choice".format(number + 1, count - number - 1))
            continue
    else:
        print("you have failed the max {} times".format(count))


check_result()
