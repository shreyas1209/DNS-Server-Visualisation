DROP DATABASE IF EXISTS dnsServer;
CREATE DATABASE IF NOT EXISTS dnsServer;

USE dnsServer;

DROP TABLE IF EXISTS rootNameServer;
DROP TABLE IF EXISTS organization;
DROP TABLE IF EXISTS TLDNameServer;
DROP TABLE IF EXISTS AuthoritativeNameServer;

CREATE TABLE IF NOT EXISTS organization(
    organization VARCHAR(100) PRIMARY KEY,
    domType  VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS rootNameServer (
    tldName VARCHAR(5),
    tldIP VARCHAR(16) PRIMARY KEY,
    organization VARCHAR(100),
    FOREIGN KEY(organization) REFERENCES organization(organization)
);


CREATE TABLE IF NOT EXISTS TLDNameServer ( 
	nameServer VARCHAR(50) NOT NULL,
    tldIP VARCHAR(16) NOT NULL,
    ansIP VARCHAR(16) PRIMARY KEY,
    location VARCHAR(20) NOT NULL,
    FOREIGN KEY(tldIP) REFERENCES rootNameServer(tldIP)
);

CREATE TABLE IF NOT EXISTS AuthoritativeNameServer (
    ansIP VARCHAR(16) NOT NULL,
	ipv4 VARCHAR(16) PRIMARY KEY,
    urlName VARCHAR(20) NOT NULL,
    FOREIGN KEY(ansIP) REFERENCES TLDNameServer(ansIP)
);


INSERT INTO organization VALUES
("NationalInternetExchangeofIndia", "country"),
("PublicInterestRegistry", "generic"),
("EDUCAUSE","sponsored");

INSERT INTO rootNameServer VALUES 
(".in", "232.154.567.45","NationalInternetExchangeofIndia"), 
(".org", "45.333.233.12","PublicInterestRegistry" ),
(".edu","345.22.45.993","EDUCAUSE");

INSERT INTO tldNameServer VALUES 
("a0.org.afilias-nst.info", "45.333.233.12", "199.19.56.1", "southPacific"), 
("b0.org.afilias-nst.org", "45.333.233.12", "199.19.54.1", "us" ),
("ns6.registry.in","232.154.567.45", "156.154.101.20", "india" ),
("c.edu-servers.net","345.22.45.993", "192.26.92.30", "africa"),
("d.edu-servers.net","345.22.45.993", "192.31.80.30", "china");

INSERT INTO AuthoritativeNameServer VALUES 
("156.154.101.20","11.345.2.3","www.bits-pilani.in"),
( "192.26.92.30","456.33.56.2","http://berkeley.edu"),
("199.19.54.1","123.56.44.234","www.khanacademy.org");
