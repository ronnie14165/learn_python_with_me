```
# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com
import math
# list���б��������Ԫ�ؼ���
# �����ţ����Ÿ���
# list1 + list2
# list1 * 2
# len��list1��
# x in list1
# ls = [1,2,3,4,5,6]
# ls[-3:]               ==>[4,5,6]
# ls[2,5]               ==>[3,4,5]
# ls.append(7)          ==>[1, 2, 3, 4, 5, 6, 7]        ==>��Ԫ����ĩβ
# ls.sort()             ==>���б�����
# ls.reverse()          ==>���б����������
# ls.index(x)           ==>����б�ֵΪx��λ��
# ls.insert(i,x)        ==>�ڵ�i��λ�ò���x
# ls.count(x)           ==>����x���б��г��ֵĴ���
# ls.remove(i)          ==>ɾ���б��i��λ�õ�ֵ
# ls.pop(i)             ==>�����i��λ�õ�ֵ������ɾ��

# math�� ��
# math.fsum()   �б�Ԫ�����
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
```