# -*- coding: utf-8 -*-
'''
高阶函数日常练习
1.1：map()函数接收两个参数，一个是函数，一个是Iterable。
例如：R = map(f,Iterable)，map会将Iterable中的所有元素放到f中间计算并得出结果放到R中。
1.2：reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
例如：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
2.Python内建的filter()函数用于过滤序列。
例如：R = filter(f,Iterable)，filter会将Iterable中的所有元素放到f中筛选并得出结果放到R中。
3.
'''
from functools import reduce

#1.1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    if isinstance(name, str):
        return name[0].upper() + name[1:].lower()
    else:
        print("请输入合法的姓名!")
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 1.2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积：

def prod(L):
    def plus(x, y):
        return x * y
    return reduce(plus,L)
# 方法二
# # 使用Lambda解决
# def prod(L):
#     return reduce(lambda x,y:x*y,L)

# 测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 1.3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':-1}
def str2float(str):
    n = 0
# 确定.号位置，n为小数点后有几个数
    for i in range(len(str)):
        if (str[i] =='.'):
            n=abs(i - (len(str)-1))
# 将字符传化为数字
    def strForNum(str):
        return DIGITS[str]
# 求数字之和
    def total(x, y):
        if (y != -1):
            return x*10 + y
        return  x
# map将字符串转化为数字，reduce求出数字之和，pow确定小数点位置
    return reduce(total,list(map(strForNum,str)))/pow(10,n)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# 2.1
# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数。
def is_palindrome(n):
    # 原来值如果与反过来原来值相同，则该值为回数
    return int(str(n)[::-1]) == n

# 测试
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')