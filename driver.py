from linecache import checkcache
import mysql.connector

def getCache(url):
    cursor.execute('SELECT * FROM Cache WHERE urlName = "'+url+'";')
    records = cursor.fetchall()
    return records[0][1]
def checkCache(url):
    print("\nChecking for ipv4 for url: "+url+" in Cache server...")
    cursor.execute('SELECT * FROM Cache WHERE urlName = "'+url+'";')
    records = cursor.fetchall() 
    if(records):
        print("\nRecord has been found in the Cache! ")
        print("\nThe IP Address is: "+records[0][1])
        return "found"
    else:
        print("Cache is empty ")
        return "empty"
def iterativeANSServerCall(domainName, ansIP):
    print("\nNow checking in the ANS server!")
    cursor.execute('SELECT * FROM AuthoritativeNameServers WHERE ansIP = "'+ansIP+'" AND urlName = "'+domainName+'";')
    records = cursor.fetchall()
    for row in records:
        print("--------------------------------------")
        print("FINAL IP Address of website is : "+row[1])
        print("--------------------------------------")
    return records[0][1]

def iterativeTLDServerCall(tldIP,loc):
    print("\nNow Checking in TLD Name Server!!!")
    cursor.execute('SELECT * FROM tldNameServers WHERE tldIP = "'+tldIP+'";')
    records = cursor.fetchall()
    print("Found "+str(len(records))+"TLD Name Servers corresponding to the Top Level Domain!")
    print("Details Available in current TLD Name Server at "+tldIP+" :")
    for row in records:
        print("--------------------------------------")
        print("TLD Name Server: "+row[0])
        print("IP Address of Authoritative Name Server: "+row[2])
        print("Location of the TLD Name Server: "+row[3])
        print("--------------------------------------")
    return records[0][2]

def iterativeRNSCall(topLevelDomain):
    print("\nChecking in Root Name Server!!!")
    cursor.execute('SELECT * FROM rootNameServer INNER JOIN org USING(orgName) WHERE tldName =".'+topLevelDomain+'";')
    record = cursor.fetchone()
    print("Details Available in Root Name Server:")
    print("--------------------------------------")
    print("Top Level Domain: "+record[1])
    print("Organization: "+record[0])
    print("Organization type: "+ record[3])
    print("IP Address of TLD Server: "+record[2])
    print("--------------------------------------")
    #print("Now Querying the TLD Server of TLD "+record[1]+" located at IP address: "+record[2])
    return record[2]

def iterativeDNSResolver(url,loc):
    try:
        print("In the DNS Resolver! ")
        splitURL = url.split('.')
        print("Cannot find IP in Cache Server!!! Now looking in Root Name Server")
        tldIP=iterativeRNSCall(splitURL[-1])
        print("Back in DNS Resolver! ")
        ansIP=iterativeTLDServerCall(tldIP,loc)
        print("Back in the DNS Resolver! ")
        finalIP=iterativeANSServerCall(splitURL[-2],ansIP)
        print("The final IP address is "+finalIP)

    #adding to cache
        cursor.execute('INSERT INTO Cache VALUES ("'+url+'","'+finalIP+'");')
        cursor.execute('SELECT * FROM Cache;')
        records = cursor.fetchall()
        return finalIP
    except:
        print("Cannot find IP address for URL "+url+"!!!!")


def recursiveDNSResolution(url,location):
    try:
        splitURL = url.split('.')
        cursor.execute('SELECT * FROM Cache WHERE urlName = "'+url+'";')
        records = cursor.fetchall()
        if(not records):
            print("Cannot find IP in Cache Server!!!Now looking in Root Name Server")
        return recursiveRNSCall(splitURL[-1],splitURL[-2],url)
    except :
        print("Cannot find IP address for URL "+url+"!!!!")
        

def recursiveRNSCall(tld,dom,url):
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
    print("Now Querying the TLD Server of TLD "+record[1]+".....")
    return recursiveTLDServerCall(record[2],dom,url)
    

def recursiveTLDServerCall(tldIP,dom,url):
    print("\nNow Checking in TLD Name Server!!!")
    cursor.execute('SELECT * FROM tldNameServers WHERE tldIP = "'+tldIP+'";')
    records = cursor.fetchall()
    print("Found "+str(len(records))+" TLD Name Servers corresponding to the Top Level Domain!")
    for row in records:
        print("--------------------------------------")
        print("TLD Name Server: "+row[0])
        print("IP Address of Authoritative Name Server: "+row[2])
        print("Location of the TLD Name Server: "+row[3])
        print("--------------------------------------")
    return recursiveANSServerCall(records[0][2],dom,url)

def recursiveANSServerCall(ansIP,dom,url):
    print(ansIP)
    print("\nNow checking in Authoritative Name Server!!!!")
    cursor.execute('SELECT * FROM AuthoritativeNameServers WHERE ansIP = "'+ansIP+'" AND urlName = "'+dom+'";')
    records = cursor.fetchall()
    print("Found "+str(len(records))+" Authoritative Name Servers corresponding to the current domain!")
    for row in records:
        print("--------------------------------------")
        print("Authoritative Name Server : "+row[2])
        print("IP Address of given URL: "+row[1])
        print("--------------------------------------")

    print("\n IP Address of given url is :"+records[0][1])
    cursor.execute('INSERT INTO Cache VALUES ("'+url+'","'+records[0][1]+'");')
    cursor.execute('SELECT * FROM Cache;')
    records = cursor.fetchall()
    return records[0][1]

def connect():
    try:
        global myDB
        myDB = mysql.connector.connect(host = 'localhost',
                                            username = 'SCOTT',
                                            password = 'TIGER',
                                            autocommit=True
                                            )
        if myDB.is_connected():
            db_Info = myDB.get_server_info()

            print("Connected to MySQL Server version ", db_Info)
            global cursor
            cursor = myDB.cursor()

            with open('dns.sql', 'r') as f:
                sqlScript = f.read().split(";\n")
                for i in range(0,len(sqlScript)):
                    if(sqlScript[i] not in ('','\n')):
                        sqlScript[i]+=';'
                for i in range(0,len(sqlScript)):
                    cursor.execute(sqlScript[i])

        # url = input("Enter URL: ")
        #print(url)
        # result=checkCache(url)
        # if result=="empty":
        #     type=input("Enter r for Recursive and i for iterative ")
        #     if type in ["r","R"]:
        #         recursiveDNSResolution(url,'India')
                
        #     else: 
        #         iterativeDNSResolver(url,'India')

        # # parsedURL= url.split('.')
        # # #cursor.callproc("RNSfunc", [".org"])
        # # cursor.execute("CALL RNSfunc('." +parsedURL[-1]+"');")
        # # record = cursor.fetchone()
        # # print(record)
        


    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
def close():
        
        if myDB.is_connected():
            cursor.execute('DROP TABLE IF EXISTS CACHE;')
            cursor.close()
            myDB.close()
            print("MySQL connection is closed")


