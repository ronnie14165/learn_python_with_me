## Pythonʵ����ϰ
- [������Ʒ����ת����](./code/currency_converter_v5.0.md)
- [�ݹ�ʵ�ַ�����](./code/pentagram.md)
- [������л����](./code/bmr_v4.0.md)
- [��Ǯ��ս](./code/money_challenge_v2.0.md)

## Python ����֪ʶ����

### input && output
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

### set
```
tutorial = {"cpp","python", "java","python"}
print(tutorial)
if "python" in tutorial:
    print("Yes")
else:
    print("No")
```

### dictionary
```
classmates = {"ronnie":"bill","eric":"dick"}
for i,j in classmates.items():
    print(i+j)
    print(j+i)

print(classmates)
print(classmates["ronnie"])
```

### import module
```
import random
for _ in range(10):
    x = random.randrange(1, 100)
    print(_,'   ',x)
```

### list
```
first,*second,third = ["linux","xidian","edu","cn"]
print(first)
print(second)
print(*second)
print(third)

myurl = ["ronnie14165","github","com"]
first,second,third = ["ronnie14165","github","com"]
print(myurl)
print(myurl[0])
print(third)
```

### sorted dictionary
```
url = {
    # key: value
    "google":"www.google.com",
    "github":"www.github.com",
    "personal":"ronnie14165.github.com",
}
print(min(zip(url.keys(),url.values())))
print(max(zip(url.keys(),url.values())))
print(url)
print(sorted(zip(url.keys(),url.values())))
```

## class and object
```
class Enemy:
    life = 10
    def attack(self):
        # print("-1")
        self.life -= 1
    def check(self):
        if self.life < 1:
            print("Dead")
        else:
            print("Alive")
eric = Enemy()
for _ in range(2):
    # print(_)
    eric.attack()
    print(eric.life)
eric.check()
```

### init function in class
```
class work:
    def __init__(self):
        print("init function is used")
    def func(self):
        print("func function is used")
ronnie = work()
ronnie.func()

class Boss:
    # x = 5
    life = 100
    def __init__(self,x):
        self.life = x
    def get_life(self):
        print(self.life)

groot = Boss(8)
groot.get_life()
thor = Boss(10)
thor.get_life()
```

### Instance variables(ʵ������)
```
class Girl:
    gender = "female"       # �����
    def __init__(self,name):
        self.name = name        # ʵ������

gamora = Girl("thanos_daughter")
pepper = Girl("iron_man_lover")
print(gamora.gender)
print(pepper.gender)
print(gamora.name)
print(pepper.name)
```

### inheritance(�̳�)
```
class parent():
    def print_family_name(self):
        print("Lee")

class child(parent):
    def print_first_name(self):
        print("Ronnie")
    def print_family_name(self):    # ��Ϊ���Ƕ��޷��̳�
        print("Li")

groot = child()
groot.print_first_name()
groot.print_family_name()
```

### multiple inheritance(���ؼ̳�)
```
class Mario():
    def move(self):
        print("Moving!")

class BigMario():
    def eat_mushroom(self):
        print("Bigger Size!!")

class ShootMario(Mario,BigMario): # ���������м̳�
    def shoot(self):
        print("Shooting!!!")

ronnie = ShootMario()
ronnie.move()
ronnie.eat_mushroom()
ronnie.shoot()
```
### struct
```
from struct import *
packed_data = pack('iif',6,19,4.73)
print(packed_data)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
orgin_data = unpack('iif',packed_data)
print(orgin_data)
```

### map
python���õĸ߽׺��������б���Ԫ�ؽ��к���ӳ�䣬����ӳ�������б�
```
income = [10,20,30]
def double_money(RMB):
    return RMB * 2

print(list(map(double_money,income)))
print(income)
```

### heapq
���б����ֵ��Сֵ
```
import heapq
#�����ֵ�����
grad = [314,255,999,1,25,77]
print(heapq.nlargest(3,grad))

#�Ը����ӵ����ݼ�������key��д��
stocks = [
    {'ticker':'Google','price':425},
    {'ticker':'Apple','price':300},
    {'ticker':'Facebook','price':600},
]

print(heapq.nsmallest(2,stocks,key=lambda stocks:stocks['price']))
```

### most frequency word
My translation homework
```
from collections import Counter
text = "The world will be better if genetic engineering is not limited. Through genetic engineering in the agricultural sector, the hungry problem in the worldwide will be solved. The death rate in the third world is going to be decrease, we would notice that a bunch of diseases, such as AIDS and hemophilia are going to be erased. The primary task of any democratic system is to improve the sense of happiness for all the people generally. However, the writer did not provide a clear method to quantize happiness. Shall we encourage college students to attend courses that they really interested or choose the courses which are going to improve their competitive strength in the market? In my point of view, pursuing for interests is priority to the considerations of the real situation. Despite of this, those students who have financial difficulties are more prone to choose the courses which could offer them decent jobs. Otherwise, it should be noted that, students could choose courses based on interests, they could also choose some courses focused on improving the future of their recruitment."

words = text.split()        # string to �б�
print(words)

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
```

### senior sorted dictionary
�ֵ�Ķ������
```
from operator import itemgetter

stocks = [
    {'ticker':'Sogou','price':250},
    {'ticker':'Google','price':425},
    {'ticker':'Apple','price':300},
    {'ticker':'Facebook','price':600},
    {'ticker':'Baidu','price':200},
]

for _ in sorted(stocks,key = itemgetter("ticker")): # �Թ�˾����������
    print(_)

for _ in sorted(stocks,key = itemgetter("price")):  # �Խ���������
    print(_)
```

### custom object sorting
�Զ����������
```
from operator import attrgetter
class User:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def __repr__(self):
        return self.name + ":" + str(self.id)
user = [
    User("Ronnie",24),
    User("Groot",2),
    User("Bob",77),
    User('Alice',23)
]

for _ in user:      # origin sequence
    print(_)
for _ in sorted(user, key = attrgetter("name")):
    print(_)
for _ in sorted(user, key = attrgetter("id")):
    print(_)
```

### download pic from
```
import random
import urllib.request

def download_image(url):
    name = random.randrange(1,100000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_image('https://pic3.zhimg.com/50/v2-1109c1eb8bfb4eb3de613774237f511a_b.jpg')

```

### simple operation on file
�ļ���д�������䣩
```
fw = open('sample.txt','w')
fw.write('Love You. \n')
fw.write('I Love Python. \n')
fw.close()

fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
```

### error
�쳣
```
# try�м�����ݻᱻ���ӣ����з����������ֹͣ����ִ�У�����except�е�����
while True:
    try:
        number = int(input("What is your favorite number? "))  # �����ַ��ᴥ���쳣������0��ʵ������
        print(1/number)
        break
    except ValueError:
        print("Please input valid value!")
    except ZeroDivisionError:
        print("The divider can not be zero!")
    except:     # ���䲻�Ƽ�
        break
    finally:       # ���������쳣ִ��
        print("The loop is over.")
```

### thread
�߳�
```
import  threading
class Wechat_message(threading.Thread):
    def run(self):
        for _ in range(1000):
            print(threading.current_thread().getName())
x = Wechat_message(name = "Sending Message")
y = Wechat_message(name = "Accepting Message")
x.start()
y.start()
```







