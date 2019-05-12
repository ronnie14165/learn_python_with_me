## Python实例练习
- [初级成品货币转换器](./code/currency_converter_v5.0.md)
- [递归实现分形树](./code/pentagram.md)
- [基础代谢计算](./code/bmr_v4.0.md)
- [存钱挑战](./code/money_challenge_v2.0.md)

## Python 基础知识介绍

### input && output
```
import math
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
```

### string
```
str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
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
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
```

```
row = int(input('请输入行数: '))
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
#转置矩阵，压缩解压缩
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

### Instance variables(实例变量)
```
class Girl:
    gender = "female"       # 类变量
    def __init__(self,name):
        self.name = name        # 实例变量

gamora = Girl("thanos_daughter")
pepper = Girl("iron_man_lover")
print(gamora.gender)
print(pepper.gender)
print(gamora.name)
print(pepper.name)
```

### inheritance(继承)
```
class parent():
    def print_family_name(self):
        print("Lee")

class child(parent):
    def print_first_name(self):
        print("Ronnie")
    def print_family_name(self):    # 因为覆盖而无法继承
        print("Li")

groot = child()
groot.print_first_name()
groot.print_family_name()
```

### multiple inheritance(多重继承)
```
class Mario():
    def move(self):
        print("Moving!")

class BigMario():
    def eat_mushroom(self):
        print("Bigger Size!!")

class ShootMario(Mario,BigMario): # 从两个类中继承
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
python内置的高阶函数，对列表中元素进行函数映射，生成映射后的新列表
```
income = [10,20,30]
def double_money(RMB):
    return RMB * 2

print(list(map(double_money,income)))
print(income)
```

### heapq
求列表最大值最小值
```
import heapq
#对数字的排序
grad = [314,255,999,1,25,77]
print(heapq.nlargest(3,grad))

#对更复杂的数据集的排序，key的写法
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

words = text.split()        # string to 列表
print(words)

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
```

### senior sorted dictionary
字典的多键排序
```
from operator import itemgetter

stocks = [
    {'ticker':'Sogou','price':250},
    {'ticker':'Google','price':425},
    {'ticker':'Apple','price':300},
    {'ticker':'Facebook','price':600},
    {'ticker':'Baidu','price':200},
]

for _ in sorted(stocks,key = itemgetter("ticker")): # 对公司名进行排序
    print(_)

for _ in sorted(stocks,key = itemgetter("price")):  # 对金额进行排序
    print(_)
```

### custom object sorting
自定义对象排序
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
文件读写（待补充）
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
异常
```
# try中间的内容会被监视，其中发生错误则会停止继续执行，进行except中的内容
while True:
    try:
        number = int(input("What is your favorite number? "))  # 输入字符会触发异常；输入0无实数意义
        print(1/number)
        break
    except ValueError:
        print("Please input valid value!")
    except ZeroDivisionError:
        print("The divider can not be zero!")
    except:     # 及其不推荐
        break
    finally:       # 无论有无异常执行
        print("The loop is over.")
```

### thread
线程
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







