file=open("./for_test.txt","w")
file.writelines("小小来了\n")
file.close()
file=open("./for_test.txt","r")
s1=file.read()
print(s1)
file.close()