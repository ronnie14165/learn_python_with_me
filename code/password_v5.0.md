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
break continue ���password_v2.0.py

�ļ����洢���ⲿ���ʣ�Ӳ�̣���������Ϣ�ļ���
�ı��ļ���ֻ���ַ�����洢���ļ����ܱ���򵥵��ı�������ֱ�Ӷ�ȡ
���룺��Ϣ��һ����ʽת��Ϊ��һ����ʽ
ACSII�� Unicode�� UTF-8
\n:ת�Ʒ�֮���з�

�ļ����������ļ��������ļ����ر��ļ�
open��filename, mode)
r
w
a
r+      ��д
write()
writelines()
close()

������̣��Գ���ִ�й���Ϊ����
�������������Ϊ����
�������ԣ���Ϊ

�ࣨclass��:ĳ�����ͼ��ϵ�����
class ClassName
__init__(self):���캯��

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