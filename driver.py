import mysql.connector

def recursiveRNSCall(tld):
    print("\nChecking in Root Name Server!!!")
    cursor.execute('SELECT * FROM rootNameServer INNER JOIN org USING(orgName) WHERE tldName =".'+tld+'";')
    record = cursor.fetchone()
    print("Details Available in Root Name Server:")
    print("--------------------------------------")
    print("Top Level Domain: "+record[1])
    print("Organization: "+record[0])
    print("Organization type: "+ record[3])
    print("IP Address of TLD Server: "+record[2])
    print("--------------------------------------")
    print("\nCould not find the final ipv4 address of the url!")
    print("Now Querying the TLD Server of TLD "+record[1]+"located at IP address: "+record[2]+".....")
    recursiveTLDServerCall(record[2])
    

def recursiveTLDServerCall(tldIP):
    print("\nNow Checking in TLD Name Server!!!")
    cursor.execute('SELECT * FROM tldNameServer WHERE tldIP = "'+tldIP+'";')
    records = cursor.fetchall()
    print("Found "+str(len(records))+"TLD Name Servers corresponding to the Top Level Domain!")
    print("Details Available in current TLD Name Server at "+tldIP+" :")
    for row in records:
        print("--------------------------------------")
        print("TLD Name Server: "+row[0])
        print("IP Address of Authoritative Name Server: "+row[2])
        print("Location of the TLD Name Server: "+row[3])
        print("--------------------------------------")



def recursiveDNSResolution(url,location):
    splitURL = url.split('.')
    print("\nAT RESOLVER: Checking for ipv4 for url:"+url+"in Cache server!!!")
    cursor.execute('SELECT * FROM Cache WHERE urlName = "'+url+'";')
    records = cursor.fetchall()
    if(not records):
        print("Cannot find IP in Cache Server!!!Now looking in Root Name Server")
        recursiveRNSCall(splitURL[-1])
        

try:
    myDB = mysql.connector.connect(host = 'localhost',
                                         username = 'SCOTT',
                                         password = 'TIGER',
                                         autocommit=True
                                         )
    if myDB.is_connected():
        db_Info = myDB.get_server_info()

        print("Connected to MySQL Server version ", db_Info)
        cursor = myDB.cursor()

        with open('dns.sql', 'r') as f:
            sqlScript = f.read().split(";\n")
            for i in range(0,len(sqlScript)):
                if(sqlScript[i] not in ('','\n')):
                    sqlScript[i]+=';'
            for i in range(0,len(sqlScript)):
                cursor.execute(sqlScript[i])

    url = input("Enter URL: ")
    recursiveDNSResolution(url,'India')
    # parsedURL= url.split('.')

    # #cursor.callproc("RNSfunc", [".org"])
    # cursor.execute("CALL RNSfunc('." +parsedURL[-1]+"');")
    # record = cursor.fetchone()
    # print(record)
    


except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if myDB.is_connected():
        cursor.close()
        myDB.close()
        print("MySQL connection is closed")




