'''
name="zhangsan"
passwd=123456
while True:
    inname=input("请输入用户名：")
    inpasswd=int (input("请输入密码："))
    if inname==name and inpasswd==passwd:
        print("欢迎%s"%name)
        break
    elif inname==name and inpasswd!=passwd:
        print("密码错误！")
    elif inname != name and inpasswd == passwd:
        print("用户名错误！")
        #作业一
'''
sum=0
'''i=1
while i<=40:
#while循环
'''
for i in range(1,41):
    if sum<100:
        sum+=5
    elif sum>=100 and sum<150:
        sum=sum+5*0.8
    elif sum>=150 and sum<400:
        sum=sum+5*0.5
    elif sum>=400:
        sum+=5
    i+=1
else:
    print(sum)
