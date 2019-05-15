```

# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com

"""
len()
str.isnumeric()
str.isalpha()
str.islower()
str.isupper()
break continue 语句password_v2.0.py

文件：存储在外部介质（硬盘）上数据信息的集合
文本文件：只有字符编码存储的文件，能被最简单的文本编译器直接读取
编码：信息从一种形式转换为另一种形式
ACSII， Unicode， UTF-8
\n:转移符之换行符

文件操作：打开文件，操作文件，关闭文件
open（filename, mode)
r
w
a
r+      读写
write()
writelines()
close()

面向过程：以程序执行过程为中心
面向对象：以事物为中心
对象：属性，行为

类（class）:某种类型集合的描述
class ClassName
__init__(self):构造函数

"""


class PasswordTool:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        if len(self. password) >= 8:
            self. strength_level += 1
        else:
            print('The length of password should contain at least 8 digits.')

        if self. check_number_exist():
            self. strength_level += 1
        else:
            print('Password should contain digital.')

        if self. check_letter_exist():
            self. strength_level += 1
        else:
            print('Password should contain letter.')

    def check_number_exist(self):
        has_number = False
        for _ in self.password:
            if _.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        has_letter = False
        for _ in self.password:
            if _.isalpha():
                has_letter = True
                break
        return has_letter


def main():

    try_times = 5
    while try_times > 0:
        password = input('Please input password:')

        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open('password_v5.0.txt', 'a')
        f.write('password is {}; password_level is {}'.format(password, password_tool. strength_level) + '\n')
        f.close()

        if password_tool. strength_level == 3:
            print('This is a valid  password.')
            break
        else:
            print('The is a invalid password. Please try again.')
            print()
            try_times -= 1
    if try_times == 0:
        print('You have try too many times.')


if __name__ == '__main__':
    main()
```