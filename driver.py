import mysql.connector

try:
    myDB = mysql.connector.connect(host = 'localhost',
                                         username = 'scott',
                                         password = 'tiger',
                                         autocommit=True
                                         )
    if myDB.is_connected():
        db_Info = myDB.get_server_info()

        print("Connected to MySQL Server version ", db_Info)
        cursor = myDB.cursor()
        cursor.execute ('CREATE DATABASE IF NOT EXISTS dnsServer')
        cursor.execute('USE dnsServer;')

        with open('dns.sql', 'r') as f:
            sqlScript = f.read().split(";\n")
            for i in range(0,len(sqlScript)):
                if(sqlScript[i] not in ('','\n')):
                    sqlScript[i]+=';'
            #print(sqlScript)
            for i in range(0,len(sqlScript)):
                cursor.execute(sqlScript[i])
                print(sqlScript[i])

    url = input("Enter URL: ")
    parsedURL= url.split('.')

    #cursor.callproc("RNSfunc", [".org"])
    cursor.execute("CALL RNSfunc('." +parsedURL[-1]+"');")
    record = cursor.fetchone()
    print(record)
    


except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if myDB.is_connected():
        cursor.close()
        myDB.close()
        print("MySQL connection is closed")




