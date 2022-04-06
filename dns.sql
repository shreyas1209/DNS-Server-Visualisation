drop table rootNameServer ;
drop table TLDNameServer;
drop table ANS;
drop table rootTLD;
drop table TLDANS;

CREATE TABLE IF NOT EXISTS rootNameServer (
	domainName VARCHAR(5) PRIMARY KEY, 
    ipAddress1 VARCHAR(16) NOT NULL,
    domainType VARCHAR(15),
    organisation VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS TLDNameServer (
	nameServer VARCHAR(50) NOT NULL,
    ipAddress2 VARCHAR(16) PRIMARY KEY, 
    location VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS ANS (
	ipv4 VARCHAR(16) PRIMARY KEY,
    urlName VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS rootTLD(
	domainName VARCHAR(5),
    nameServer VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS TLDANS(
	nameServer VARCHAR(50) NOT NULL,
	urlName VARCHAR(20) NOT NULL
);

INSERT INTO RootNameServer VALUES 
(".in", "232.154.567.45", "country", "NationalInternetExchangeofIndia"), 
(".org", "45.333.233.12", "generic", "PublicInterestRegistry" ),
(".edu","345.22.45.993","sponsored","EDUCAUSE");

INSERT INTO tldNameServer VALUES 
("a0.org.afilias-nst.info", "199.19.56.1", "southPacific"), 
("b0.org.afilias-nst.org", "199.19.54.1", "us" ),
("ns6.registry.in", "156.154.101.20", "india" ),
("c.edu-servers.net", "192.26.92.30", "africa"),
("d.edu-servers.net", "192.31.80.30", "china");

INSERT INTO roottld VALUES 
(".org","a0.org.afilias-nst.info"),
(".org","b0.org.afilias-nst.org"),
(".in","ns6.registry.in"),
(".edu","c.edu-servers.net"),
(".edu","d.edu-servers.net");

INSERT INTO tldans VALUES 
("ns6.registry.in","www.bits-pilani.in"),
("c.edu-servers.net","http://berkeley.edu"),
("a0.org.afilias-nst.info","www.khanacademy.org");

INSERT INTO ans VALUES 
("11.345.2.3","www.bits-pilani.in"),
("456.33.56.2","http://berkeley.edu"),
("123.56.44.234","www.khanacademy.org");








