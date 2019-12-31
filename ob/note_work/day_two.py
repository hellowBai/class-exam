str="HELLOW,WORLD"
str3={"":""}
del str3[""]
for i in range(1,len(str)):
    str3[str[i]]=str.count(str[i])
print(str3)


str4={"":""}
del str4[""]
code=-1
print("添加名单，删除，修改名单，查询名单,退出系统")
while code!=5:
    code=(int)(input("请选择功能："))
    if code==1:
        str_ = input("请输入名单：")
        str4[str_]=input("名单信息")
    elif code==2:
        del str4[input("请输入名单：")]
    elif code==3:
        str_=input("请输入名单：")
        print(str4[str_])
        str4[str_]=input("请输入名单信息：")
    elif  code==4:
        print(str4[input("请输入名单：")])

