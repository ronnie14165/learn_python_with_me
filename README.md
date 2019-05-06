## Python ����֪ʶ����

###input && output
```
import math
radius = float(input('������Բ�İ뾶: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('�ܳ�: %.2f' % perimeter)
print('���: %.2f' % area)
```

### string
```
str1 = 'hello, world!'
print('�ַ����ĳ�����:', len(str1))
print('��������ĸ��д: ', str1.title())
print('�ַ������д: ', str1.upper())
print('�ַ����ǲ��Ǵ�д: ', str1.isupper())
print('�ַ����ǲ�����hello��ͷ: ', str1.startswith('hello'))
print('�ַ����ǲ�����hello��β: ', str1.endswith('hello'))
print('�ַ����ǲ����Ը�̾�ſ�ͷ: ', str1.startswith('!'))
print('�ַ����ǲ���һ��̾�Ž�β: ', str1.endswith('!'))
```

### if...elif...else
```
name = 'bill'
if name is 'lee':
    print("hello lee")
elif name is 'bill':
    print("hello bill")
```

### for
```
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
```
```
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    (x, y) = (y, x)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d��%d�����Լ����%d' % (x, y, factor))
        print('%d��%d����С��������%d' % (x, y, x * y // factor))
        break
```

```
row = int(input('����������: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
```

### while
```
n = 5
while n < 10:
    print('Avenger, Assemble.')
    n += 1
```

### if...break
```
magic_number = 24
for n in range(100):
    if n is magic_number:
        print(n, 'is magic number')
        break
    else:
        print(n, 'is not magic number')
```

### funtion
```
def rmb_to_usd(rmb):
    amount = rmb / 6.77
    print(amount)
rmb_to_usd(100)
```

```
def predict_gf_age(my_age = 21):
    gf_age = my_age /2 +10;
    return gf_age

age1 = predict_gf_age(27)
print("her age is ",age1)
age2 = predict_gf_age()
print("her age is ",age2)
```

### keyword parameter
```
def keyword(a = 'v', b = 'p', c = 'n'):
    print(a,b,c)
keyword()
keyword('www','4399','com')
keyword(b = 'acm')
```

### changeable parameter
```
def add_number(*args):
    total = 0;
    for a in args:
        total += a
    print(total)    #the position of code does impact the algorithm!

add_number(3)
add_number(3,6)
add_number(3,6,9)
```

### parameter unpacking
```
def health_value(age, apple, cigs):
    value = 100 + age + apple*3.5 - cigs*2
    print(value)

pack = [21,0,0]
health_value(pack[0],pack[1],pack[2])
health_value(*pack)
```

### lambda function
```
answer = lambda x:x*3.1416926*2
print(answer(5))
def func(answer1 = lambda x:x*3.1415926*2):
    print(answer1(10))      #x=10
func()
func(lambda x : x*5)
```

### zip function
```
first = ['r','o','n','n','i','e']
last = ['l','e','e']
name = zip(first,last)
print(name)
for i,j in name:
    print(i, j)
#ת�þ���ѹ����ѹ��
```





