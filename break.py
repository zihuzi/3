# 开发时间：2021/2/20 12:11
# 输入密码，最多三次，正确结束循环
for i in range(3):
    password=input('请输入密码：')
    if password=='8888':
            print('密码正确')
            break
    else:
        print('密码错误')
# 同样功能
i=0
while i<3:
    password=input('请输入密码：')
    if password=='8888':
            print('密码正确')
            break
    else:
        print('密码错误')
    i+=1