def iterariveANSServerCall(domainName, ansIP):
    print("\nNow checking in the ANS server!")
    cursor.execute('SELECT * FROM AuthoritativeNameServer WHERE ansIP = "'+ansIP+'" AND urlName = "'+domainName+'";')
    records = cursor.fetchall()
    for row in records:
        print("--------------------------------------")
        print("FINAL IP Address of website is : "+row[1])
        print("--------------------------------------")
    return records[0][1]

def iterativeTLDServerCall(tldIP,loc):
    print("\nNow Checking in TLD Name Server!!!")
    cursor.execute('SELECT * FROM tldNameServer WHERE tldIP = "'+tldIP+'" AND location= "'+loc+'";')
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
    print("In the DNS Resolver! ")
    splitURL = url.split('.')
    print("\nAT RESOLVER: Checking for ipv4 for url:"+url+"in Cache server!!!")
    cursor.execute('SELECT * FROM Cache WHERE urlName = "'+url+'";')
    records = cursor.fetchall()
    #checking cache 
    if(records):
        print(records)
    else:
        print("Cannot find IP in Cache Server!!! Now looking in Root Name Server")
        tldIP=iterativeRNSCall(splitURL[-1])
        print("Back in DNS Resolver! ")
        ansIP=iterativeTLDServerCall(tldIP,loc)
        print("Back in the DNS Resolver! ")
        finalIP=iterariveANSServerCall(splitURL[1],ansIP)
<<<<<<< HEAD
        print("The final IP address is "+finalIP)
=======
        print("The final IP address is "+finalIP)
>>>>>>> 22265f8792ecde65c0ff0dc8dd27c69a64539685
