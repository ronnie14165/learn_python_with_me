```
# Author�� Ronnie Lee
# mail:ronnie14165@gmail.com
# url:ronnie14165.github.com
# bugs when input usd!!!!!!
print('Welcome to use currency_converter_v5.0!')
print('Hint: input <quit> when you want to quit')
print('Hint: input samples: 100usd; 100rmb')

USD_VS_RMB = 6.77


def main():
    currency_str_value = input('Please input(end with usd or rmb): ')
    while currency_str_value != 'quit':

        unit = currency_str_value[-3:]
        if unit == 'rmb':
            exchange_rate = 1 / USD_VS_RMB
        elif unit == 'usd':
            exchange_rate = USD_VS_RMB
        else:
            exchange_rate = -1

        if exchange_rate != -1:
            currency_value = currency_str_value[:-3]
            in_money = eval(currency_value)

            convert_currency = lambda x: x * exchange_rate  # lambda����û�з���ֵ

            out_money = convert_currency(in_money)

            print(currency_str_value, 'equals ', end=' ')
            print(out_money, end='')

            if unit == 'rmb':
                print('usd')
            else:
                print('rmb')

        else:
            print('error!')
        print('*****************************************')
        currency_str_value = input('Please input(end with usd or rmb): ')

    print('Thanks for using our program!')
    print('More awesome programs in www.github.com/ronnie14165 ')


if __name__ == '__main__':
    main()
# ֱ��main������error


```