DROP DATABASE IF EXISTS dnsServer;
CREATE DATABASE IF NOT EXISTS dnsServer;

USE dnsServer;

DROP TABLE IF EXISTS rootNameServer;
DROP TABLE IF EXISTS org;
DROP TABLE IF EXISTS TLDNameServers;
DROP TABLE IF EXISTS AuthoritativeNameServers;
DROP TABLE IF EXISTS Cache;

CREATE TABLE IF NOT EXISTS org(
    orgName VARCHAR(100) PRIMARY KEY,
    domType  VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS rootNameServer (
    tldName VARCHAR(5),
    tldIP VARCHAR(16) PRIMARY KEY,
    orgName VARCHAR(100),
    FOREIGN KEY(orgName) REFERENCES org(orgName)
);


CREATE TABLE IF NOT EXISTS TLDNameServers ( 
	nameServer VARCHAR(50) NOT NULL,
    tldIP VARCHAR(16) NOT NULL,
    ansIP VARCHAR(16) PRIMARY KEY,
    location VARCHAR(20) NOT NULL,
    FOREIGN KEY(tldIP) REFERENCES rootNameServer(tldIP)
);

CREATE TABLE IF NOT EXISTS AuthoritativeNameServers (
    ansIP VARCHAR(16) NOT NULL,
	ipv4 VARCHAR(16) PRIMARY KEY,
    urlName VARCHAR(20) NOT NULL

);

CREATE TABLE IF NOT EXISTS Cache(
    urlName VARCHAR(20) NOT NULL,
    ipv4 VARCHAR(16) PRIMARY KEY,
    tldIP VARCHAR(16),
    ansIP VARCHAR(16) 
);

INSERT INTO org VALUES
("NationalInternetExchangeofIndia", "country"),
("PublicInterestRegistry", "generic"),
("EDUCAUSE","sponsored");

INSERT INTO rootNameServer VALUES 
(".in", "232.154.567.45","NationalInternetExchangeofIndia"), 
(".org", "45.333.233.12","PublicInterestRegistry" ),
(".edu","345.22.45.993","EDUCAUSE");

INSERT INTO tldNameServers VALUES 
("a0.org.afilias-nst.info", "45.333.233.12", "192.29.56.5", "southPacific"), 
("b0.org.afilias-nst.org", "45.333.233.12", "199.19.54.1", "us" ),
("ns6.registry.in","232.154.567.45", "156.154.101.34", "india" ),
("c.edu-servers.net","345.22.45.993", "192.26.92.3200", "africa"),
("d.edu-servers.net","345.22.45.993", "192.31.80.30", "china");

INSERT INTO AuthoritativeNameServers VALUES 
("156.154.101.34","11.345.2.3","bits-pilani"),
( "192.26.92.30","456.33.56.22","berkeley"),
( "192.26.92.3200","456.33.56.245","berkeley"),
("199.19.54.1","123.56.44.14","khanacademy"),
("192.29.56.5","123.56.44.24","khanacademy");