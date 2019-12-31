import random

randownumber=random.randint(1,10)
num=0
while True:
    num=(int)(input("please input your guess num："))
    if num==randownumber:
        print("congratralation!!")
        break
    elif num>randownumber:
        print("too big!")
    elif num<randownumber:
        print("too small!")
