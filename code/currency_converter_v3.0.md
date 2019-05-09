```
#Author: Ronnie Lee
#mail:ronnie14165@gmail.com
#url:ronnie14165.github.com

import keyword

# bugs when input usd!!!!!!


USD_VS_RMB = 6.77
print('Welcome to use currency_converter_v3.0!')
print('Hint: input <quit> when you want to quit')
print('Hint: input samples: 100usd; 100rmb')
currency_str_value = 'start'
i = 0
while currency_str_value != 'quit':
    i = i + 1
    print('the', i , 'time of loop')
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
    elif currency_str_value == 'quit':
        pass
    else:
        print('input error')
    print('*****************************************')

print('Thanks for using our program!')
print('More awesome programs in www.github.com/ronnie14165 ')
```


```
import keyword
USD_VS_RMB = 6.77
print('Hint: input <quit> when you want to quit')
print('Hint: input samples: 100usd; 100rmb')
currency_str_value = input('Please input(end with usd or rmb): ')
while currency_str_value != 'quit':
    unit = currency_str_value[-3:]
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

    print('**********************************')
    currency_str_value = input('Please input(end with usd or rmb): ')

print('Thanks for using our program!')
print('More awesome programs in www.github.com/ronnie14165 ')

```