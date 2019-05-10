#Author： Ronnie Lee
#mail:ronnie14165@gmail.com
#url:ronnie14165.github.com
"""
字符串的正向反向索引

0   1   2   3   4   5
p   y   t   h   o   n
-6  -5  -4  -3  -2  -1


In Python Console
import keyword
print(keyword.kwlist)

pass 占位符,不会报错
if ... == '...'
    pass
elif ......

"""
import keyword
USD_VS_RMB = 6.77
currency_str_value = input('Please input(end with usd or rmb): ')
# print(currency_str_value)
unit = currency_str_value[-3:]
# print(unit)
if unit == 'rmb':
    rmb_currency_value = currency_str_value[:-3]
    rmb_value = eval(rmb_currency_value)
    usd_value = rmb_value / USD_VS_RMB
    print(usd_value,'usd')
elif unit == 'usd':
    usd_currency_value = currency_str_value[:-3]
    usd_value = eval(usd_currency_value)
    rmb_value = usd_value * USD_VS_RMB
    print(rmb_value,'rmb')
else:
    print('input error')




