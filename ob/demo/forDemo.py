sum=0
for i in range(1,101):
    sum+=i
print("add=%d"%sum)
print("_"*50)

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d "%(j,i,i*j),end=" ")
    print()
print("_"*40)

for i in range(0,20):
    for j in range(0,33):
        if i*5+j*3+(100-i-j)/3==100:
            print("male=%d,female=%d,little=%d"%(i,j,100-i-j))
print("_"*50)
"""
银行贷款
等额本金  月还款金额
            总额/月份 +利息
        利息  0.5%
 等额本息  月还款金额
            总额/月份+利息           

"""
foundation=500000
month=240
all=foundation
for i in range(1,month):
    tex=(foundation)*0.05/12
    sum+=tex
    foundation=foundation-all/month
    print("you should pay for %d"%(tex+all/month))
print("tex=%d"%sum)