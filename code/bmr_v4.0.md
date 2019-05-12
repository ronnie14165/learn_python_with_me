```
# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com

# float(4)
# int(3.14)
# str(3.14)
# int('4')
# int('something')  ==>     error
# type('abc')       ==>     str
# type('3')         ==>     str
# type(3)           ==>     int
# type(3.0)         ==>     float

# input 接收到的均为str类型
# input.str_find(' ')

# input.str_split():    字符串分隔
# 输出为列表类型

# print('BMR value equals{}Calories'.format(bmr))


def main():
    y_or_n = input('Would you like to quit?(Please input <y> or <n>)')

    while y_or_n != 'y':

        print('Please input the information as follow:(Separate them by a space)')
        input_str = input('gender weight height age')

        input_str_list = input_str.split(' ')
        try:
            gender = input_str_list[0]
            weight = float(input_str_list[1])
            height = float(input_str_list[2])
            age = int(input_str_list[3])

            if gender == 'male':
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
            elif gender == 'female':
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
            else:
                bmr = -1

            if bmr != -1:
                print('gender:{},weight:{},height{},age{}'.format(gender, weight, height, age))
                print('BMR value equals', bmr, 'Calories')

            else:
                print('Input error')

        except ValueError:
            print('Please input valid information.')

        except IndexError:
            print('Please input complete information.')

        except:             # 有无错误？
            print('Unknown error.')

        y_or_n = input('Would you like to quit?(Please input <y> or <n>)')


if __name__ == '__main__':
    main()
```