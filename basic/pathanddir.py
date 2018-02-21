# 1.得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
import os
print(os.getcwd())
# 2.返回指定目录下的所有文件和目录名:os.listdir()
print(os.listdir(os.getcwd()))
# 3.函数用来删除一个文件:os.remove()
# 4.删除多个目录：os.removedirs（r“c：\python”）
# 5.检验给出的路径是否是一个文件：os.path.isfile()

# 6.检验给出的路径是否是一个目录：os.path.isdir()

# 7.判断是否是绝对路径：os.path.isabs()

# 8.检验给出的路径是否真地存:os.path.exists()

# 9.返回一个路径的目录名和文件名:os.path.split()
print(os.path.split("/Users/anderson/PycharmProjects/test/class2.py"))
# 10.分离扩展名：os.path.splitext()
print(os.path.splitext("/Users/anderson/PycharmProjects/test/class2.py"))
# 11.获取路径名：os.path.dirname()
print(os.path.dirname("/Users/anderson/PycharmProjects/test/class2.py"))
# 12.获取文件名：os.path.basename()
print(os.path.basename("/Users/anderson/PycharmProjects/test/class2.py"))
# 13.运行shell命令: os.system()
print(os.system("ls -l"))

# 14.读取和设置环境变量:os.getenv() 与os.putenv()
# 15.指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
print(os.name)
# 16.重命名：os.rename（old， new）
# 17.创建多级目录：os.makedirs（r“c：\python\test”）
# 18.创建单个目录：os.mkdir（“test”）
# 19.得到指定文件最后一次的访问时间 os.path.getatime()
print(os.path.getatime("/Users/anderson/PycharmProjects/test/class2.py"))
# 20.得到指定文件最后一次的改变时间 os.path.getmtime()
print(os.path.getmtime("/Users/anderson/PycharmProjects/test/class2.py"))
# 21.得到指定文件的大小 os.path.getsize()
print(os.path.getsize("/Users/anderson/PycharmProjects/test/class2.py"))
# 22.将目录名和文件的基名拼接成一个完整的路径 os.path.join()
for filename in os.listdir("/home"):
    print(os.path.join("/tmp", filename))

#实战
# 1.创建目录
import shutil
os.mkdir("file")
# 2.复制文件：
shutil.copyfile("oldfile","newfile")        #oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")            #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
# 3.复制文件夹：
shutil.copytree("olddir","newdir")        #olddir和newdir都只能是目录，且newdir必须不存在
# 4.重命名文件（目录）
os.rename("oldname","newname")              #文件或目录都是使用这条命令
# 5.移动文件（目录）
shutil.move("oldpos","newpos")
# 6.删除文件
os.remove("file")
# 7.删除目录
os.rmdir("dir")                             #只能删除空目录
shutil.rmtree("dir")                        #空目录、有内容的目录都可以删
# 8.转换目录
os.chdir("path")                            #换路径
# 一般获取当前路径是：
current_dir = os.path.split(os.path.realpath(__file__))[0]
print(current_dir)



