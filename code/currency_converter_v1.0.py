#Author： Ronnie Lee
#mail:ronnie14165@gmail.com
#url:ronnie14165.github.com
# 
import keyword

rmb_str_value = input('Please input CNY: ')
print(rmb_str_value,' CNY')
rmb_value = eval(rmb_str_value)
USD_VS_RMB = 6.77
usd_value = rmb_value / USD_VS_RMB
print('That is about ',usd_value,'USD')
