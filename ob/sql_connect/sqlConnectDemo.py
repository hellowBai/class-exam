import pymysql

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


conn.select_db(DB_NAME)

try:
# 查询数据条目
    count = cursor.execute('SELECT * FROM %s' %TABLE_NAME)
  #  count = cursor.execute('ALTER TABLE TEST.USER ADD column qq VARCHAR(10) ')
    print ('total records:', cursor.rowcount )

# 获取表名信息
    desc = cursor.description
    print(desc[0][0],end=" ")
    print(desc[0][1],end=" ")
# 获取表的值
    cursor.scroll(0, mode='absolute')
    results = cursor.fetchall()
    for result in results:
        print(result["name"])
except:
    print("when you reach ,it has error")

print(cursor)