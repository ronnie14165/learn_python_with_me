# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com
import math
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


def main():
    i = 1
    money_saved_in_i_th_week = 10
    money_increased = 10
    total_week = 52
    saving = 0
    money_list = []

    while i <= total_week:
        # saving += money_saved_in_i_th_week
        money_list.append(money_saved_in_i_th_week)
        saving = int(math.fsum(money_list))
        print('the {}th week, increase {}, totally {}'.format(i, money_saved_in_i_th_week, saving))
        money_saved_in_i_th_week += money_increased

        i += 1


if __name__ == '__main__':
    main()