def prin(cont1en):
    print(" ds")
    print(" da")
    print(cont1en)


prin(12)

num=100
def fn():
    global  num
    num+=200
    prin(num)
fn()

def fnc(list1):
    list1.append("aaa")

list =["safas"]
fnc(list)
print(list)

def print_name(name,age=20):
    print(name,age)
print_name("小小来了")

def arge(a,b,*args,**kwargs):
    sum=a+b
    for i in args:
        sum+=i
    print(kwargs)
    return sum

print(arge(1,2,3,4,name="魔法师",tel="2123"))

#匿名函数
sum=lambda x,y:x+y
result=sum(1,2)
print(result)

stus=[{"name":"lisi","age":20},
        {"name":"misi","age":20},

        {"name":"misi","age":20},
      ]
stus.sort(key=lambda x:x["name"])
print(stus)