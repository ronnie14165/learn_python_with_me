```
# Author: Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com

import datetime
from datetime import datetime
"""
tuple(元组);特殊的序列类型
一旦创建不能修改
(2,4,6)   ('red','green','blue')
函数多返回值
t = (1,2,3)   tuple       t[1] = 2 ==> error
l = [1,2,3]   list
s = (123)     int
a = (123,)    tuple
"""


def main():
    input_date_str = input('Please input the data(yyyy/mm/dd):')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day
    days_in_month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tuple[: month - 1]) + day
    if(year % 400 == 0) or ((year % 4 == 0) or (year % 100 != 0)):
        if month > 2:
            day += 1
    print(days)


if __name__ == '__main__':
    main()

```