
CREATE DATABASE IF NOT EXISTS dnsServer;

USE dnsServer;


DROP TABLE IF EXISTS AuthoritativeNameServers;
DROP TABLE IF EXISTS TLDNameServers;
DROP TABLE IF EXISTS rootNameServer;
DROP TABLE IF EXISTS org;

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
    ipv4 VARCHAR(16) 
);

INSERT INTO org VALUES
("NationalInternetExchangeofIndia", "country"),
("PublicInterestRegistry", "generic"),
("EDUCAUSE","sponsored");
("VeriSignGlobalRegistryServices","generic");

INSERT INTO rootNameServer VALUES 
(".in", "232.154.567.45","NationalInternetExchangeofIndia"), 
(".org", "45.333.233.12","PublicInterestRegistry" ),
(".edu","345.22.45.993","EDUCAUSE"),
(".com","445.4.44.23","VeriSignGlobalRegistryServices"),
(".net","33.456.3.22","VeriSignGlobalRegistryServices");

INSERT INTO tldNameServers VALUES 
("a0.org.afilias-nst.info", "45.333.233.12", "192.29.56.5", "southPacific"), 
("b0.org.afilias-nst.org", "45.333.233.12", "199.19.54.1", "us" ),
("ns6.registry.in","232.154.567.45", "156.154.101.34", "india" ),
("ns4.registry.in","232.154.567.45","37.209.198.12","us",),
("c.edu-servers.net","345.22.45.993", "192.26.92.450", "africa"),
("d.edu-servers.net","345.22.45.993", "192.31.80.30", "china"),
("a.gtld-servers.net", "445.4.44.23","192.5.6.30","europe"),
("b.gtld-servers.net","445.4.44.23","192.33.14.30","southPacific"),
("c.gtld-servers.net","445.4.44.23","192.26.92.30","us"),
("a.gtld-servers.net", "33.456.3.22","192.5.6.30","europe"),
("b.gtld-servers.net","33.456.3.22","192.33.14.30","southPacific"),
("c.gtld-servers.net","33.456.3.22","192.26.92.30","us");


INSERT INTO AuthoritativeNameServers VALUES 
("156.154.101.34","11.345.2.3","bits-pilani"),
("37.209.198.12","34.222.56.49","bits-pilani"),
("199.19.54.1","123.56.44.14","khanacademy"),
("192.29.56.5","123.56.44.24","khanacademy"),
( "192.26.92.30","456.33.56.22","berkeley"),
( "192.26.92.450","456.33.56.245","berkeley"),
("192.5.6.30","345.66.754.3","google"),
("192.33.14.30","3.667.33.29","google"),
("192.26.92.30","233.3.643.4","google"),
("192.5.6.30","555.44.35.7","youtube"),
("192.33.14.30","765.6.3.456","youtube"),
("192.26.92.30","959.48.292.4","youtube"),
("192.5.6.30","383.25.2.4","slideshare"),
("192.33.14.30","383.25.234.4","slideshare"),
("192.26.92.30","383.25.337.4","slideshare");
