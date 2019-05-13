```
# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com
import math
import datetime
# list（列表）：有序的元素集合
# 方括号，逗号隔开
# list1 + list2
# list1 * 2
# len（list1）
# x in list1
# ls = [1,2,3,4,5,6]
# ls[-3:]               ==>[4,5,6]
# ls[2,5]               ==>[3,4,5]
# ls.append(7)          ==>[1, 2, 3, 4, 5, 6, 7]        ==>加元素在末尾
# ls.sort()             ==>对列表排序
# ls.reverse()          ==>对列表做逆序操作
# ls.index(x)           ==>输出列表值为x的位置
# ls.insert(i,x)        ==>在第i个位置插入x
# ls.count(x)           ==>返回x在列表中出现的次数
# ls.remove(i)          ==>删除列表第i个位置的值
# ls.pop(i)             ==>输出第i个位置的值并将其删除

# math库 ：
# math.fsum()   列表元素求和
# math.pi
# math.ceil(2.2)        ==>3
# math.floor(2.2)       ==>2
# math.pow(x,y)
# math.sqrt(x)

# datetime库:
# datetime.datetime.now()
# now = datetime.datetime.now()
# now.year
# datetime.datetime.strptime('2019/01/01',format('%Y/%m/%d'))
# datetime.datetime.strptime('2019-01-01',format('%Y-%m-%d'))
# now.isocalendar()
# datetime.strftime()
# datetime.datetime.strftime(now, "%d/%m/%Y")
saving = 0


# def convert(num):
#     if num > 9:
#         return str(num)
#     else:
#         return '0'+str(num)
    # input_date_str = str(now.year) + '/' + convert(now.month) + '/' + convert(now.day)

def save_money_in_n_week(money_saved_in_i_th_week, money_increased, total_week):
    # 局部变量：只存在于函数内的变量
    # 全局变量： 存在于函数内部以及函数外部
    # 声明全局变量
    global saving

    money_list = []
    save_money_list = []

    for i in range(total_week):
        money_list.append(money_saved_in_i_th_week)
        saving = int(math.fsum(money_list))
        save_money_list.append(saving)
        # print('the {}th week, increase {}, totally {}'.format(i+1, money_saved_in_i_th_week, saving))
        money_saved_in_i_th_week += money_increased
    return save_money_list


def main():

    money_saved_in_i_th_week = float(input('Please input the money you want to save in the first week:'))
    money_increased = float(input('Please input the money you want to increase each week:'))
    total_week = int(input('Please input the week:'))
    save_money_list = save_money_in_n_week(money_saved_in_i_th_week, money_increased, total_week)
    now = datetime.datetime.now()

    input_date_str = datetime.datetime.strftime(now, "%Y/%m/%d")
    print('Today is :', input_date_str)
    # input_date_str = input('Please input the date you want to begin:(yyyy/mm/dd)')
    input_date = datetime.datetime.strptime(input_date_str, format('%Y/%m/%d'))
    week_num = int(input_date.isocalendar()[1])

    print('You have already save {} in {}th week'.format(save_money_list[week_num - 1], week_num))


if __name__ == '__main__':
    main()
```