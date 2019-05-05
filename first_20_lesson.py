#author： Ronnie Lee
#mail:ronnie14165@gmail.com
#url:ronnie14165.github.com

##      lambda funcion
# answer = lambda x:x*3.1416926*2
# print(answer(5))
#
# def func(answer1 = lambda x:x*3.1415926*2):
#     print(answer1(10))      #x=10
#
# func()
# func(lambda x : x*5)

##      zip function
# first = ['r','o','n','n','i','e']
# last = ['l','e','e']
# name = zip(first,last)
# print(name)
# for i,j in name:
#     print(i, j)
##转置矩阵，压缩解压缩

##      parameter unpacking
# def health_value(age, apple, cigs):
#     value = 100 + age + apple*3.5 - cigs*2
#     print(value)
#
# pack = [21,0,0]
# health_value(pack[0],pack[1],pack[2])
# health_value(*pack)


##      changeable parameter
# def add_number(*args):
#     total = 0;
#     for a in args:
#         total += a
#     print(total)    #the position of code does impact the algorithm

# add_number(3)
# add_number(3,6)
# add_number(3,6,9)


##      keywork parameter
# def keyword(a = 'v', b = 'p', c = 'n'):
#     print(a,b,c)
# keyword()
# keyword('www','4399','com')
# keyword(b = 'acm')


##          range of variable


##      function default value
# def predict_gf_age(my_age = 21):
#     gf_age = my_age /2 +10;
#     return gf_age
#
# age1 = predict_gf_age(27)
# print("her age is ",age1)
# age2 = predict_gf_age()
# print("her age is ",age2)

##      function return
# def predict_gf_age(my_age):
#     gf_age = my_age /2 +10;
#     return gf_age
#
# age = predict_gf_age(21)
# print("her age is ",age)


##      FUNCTION
# def func():
#     print("dream")
# func()
# def rmb_to_usd(rmb):
#     amount = rmb / 6.77
#     print(amount)
# rmb_to_usd(89)


##      continue function
# except_number = [2,5,7]
# for n in range(10):
#     if n in except_number:
#         continue
#     print(n)


##      break funcrion

# magic_number = 26
# for n in range(100):
#     if n is magic_number:
#         print(n, 'is magic number')
#         break
#     else:
#         print(n, 'is not magic number')


##      while function.

# n = 5
# while n < 10:
#     print('nothing')
#     n += 1

##      for function
# for x in range(3,12,2):
#     print(x,'nothing')

# words = ['a','ads','adc','acm']
# for w in words[0:2]:
#     print(w,len(w))

##      if ...  elif...
# age = 27
# if age < 18:
#     print("233")
#
# name = 'bill'
# if name is 'lee':
#     print("hello lee")
# elif name is 'bill':
#     print("bill")


