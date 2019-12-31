import pymysql
def inDemo(str,conn,DB_NAME,TABLE_NAME):
    cursor = conn.cursor()
    try:
        count = cursor.execute('SELECT * FROM %s.%s' % (DB_NAME,TABLE_NAME))
        print("insert into %s.%s value (%d,'%s',%d,%d,%d)"%(DB_NAME,TABLE_NAME,str[0],str[1],str[2],str[3],str[4]))
        cursor.execute("insert into %s.%s value (%d,'%s',%d,%d,%d)"%(DB_NAME,TABLE_NAME,str[0],str[1],str[2],str[3],str[4]))
    except:
        print("it has error!! check your input!!")