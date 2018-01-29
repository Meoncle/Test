'''
将中所有的字符串变成小写
'''
# 方法一
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
# 挑选出L1中的字符串,将字符串变成小写后放入L2中
for i in L1:
    if isinstance(i ,str):
        result = i.lower()
        L2.append(result)

# # 方法二
# # 列表生成式
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [i.lower() for i in L1 if isinstance(i, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')