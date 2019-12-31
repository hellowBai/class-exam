import pymysql
import com.searchDemo
import com.insertDemo
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()

DB_NAME="test"
TABLE_NAME="user"

code=input()

while code=='1':
    name=input("what is your name:")
    com.searchDemo.inDemo(name,conn,DB_NAME,TABLE_NAME)
    code = input()

while code=='2':
    value=[]
    add=input("what is your want to add id:")
    value.append((int)(add))
    add=input("what is your want to add name:")
    value.append(add)
    add=input("what is your want to add qq:")
    value.append((int)(add))
    add=input("what is your want to add ace:")
    value.append((int)(add))
    add=input("what is your want to add tel:")
    value.append((int)(add))
    print(value)
    com.insertDemo.inDemo(value,conn,DB_NAME,TABLE_NAME)
    code = input()

