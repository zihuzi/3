# 开发时间：2021/2/20 11:56
for item in 'py':   # 字符串
    print(item)
for i in range(2):  # 序列
    print(i)
for _ in range(3):  # 不需要变量，可以用下划线代替
    print('python')

# 计算1-100偶数和
sum=0
for i in range(1,101):
    if i % 2 == 0:
        sum+=i
print(sum)