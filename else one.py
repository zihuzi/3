# 开发时间：2021/2/20 15:04
for i in range(3):
    password=input('请输入密码：')
    if password=='8888':
            print('密码正确')
            break
    else:
        print('密码错误')
else:
        print('输入三次密码错误')
