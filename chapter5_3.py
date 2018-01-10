#传递可变参数
def func(*args):
    print(args)
func(1, 2, 3)

def search(*t, **d):
    keys = d.keys()
    values = d.values()
    print(keys)
    print(values)
    for arg in t:
        for key in keys:
            if arg == key:
                print("find:", d[key])

search("one","three",one="1",two="2",three="3" )

#return返回多个值
def funcReturn(x,y,z):
    l = [x,y,z]
    l.reverse()
    numbers=tuple(l)
    return numbers

x,y,z = funcReturn(0,1,2)
print(x,y,z)

#计算阶乘
def refunc(n):
    i = 1
    if n > 1:
        i = n
        n = n * refunc(n-1)
    print("%d! =" %i, n)
    return n

refunc(5)

#使用reduce计算阶乘
from functools import reduce
print("5!=", reduce(lambda x,y:x*y,range(1,6)))

#Generator函数
def funcGen(n):
    for i in range(n):
        yield i

for i in funcGen(3):
    print(i)

r = funcGen(3)
print("这是Generator函数")
print(r.__next__())
print(r.__next__())
print(r.__next__())

# yield和return区别
print("yield和return区别")
def funReturn(n):
    for i in range(n):
        return i
def funYield(n):
    for i in range(n):
        yield i
print(funReturn(3))
print(funYield(3))