import pymysql
def inDemo(str,conn,DB_NAME,TABLE_NAME):
    cursor = conn.cursor()
    try:
        count = cursor.execute('SELECT * FROM %s.%s WHERE NAME =  "%s"   ' % (DB_NAME,TABLE_NAME,str))
        cursor.scroll(0, mode='absolute')
        results = cursor.fetchall()
        for result in results:
            print(result)
    except:
        print("it has error!!")