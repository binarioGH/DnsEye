#-*-coding: utf-8-*-
from time import strftime

def banner(p=True):
	text = '''
		 _______
		|		\\	  
		|    _   \\   
		|   | |   |
		|   | |   |
		|   | |	  |  
		|   |_|	  | N S  E Y E    
		|	  	  |
		|	 	 /	  
		|_______/     		'''
	text += "\n\n		[+]Github: https://github.com/binarioGH\n\n"
	if p: 
		print(text)
	else:
		return text


def getText(query, record):
	TEXT = "-"*40
	TEXT += "\n 	{}:".format(record, RECORDS[record])
	for info in query:
		TEXT += "\n		{}".format(info)
	TEXT += "\n"
	return TEXT

RECORDS = {
	"A": "IPV4 Adress Record",
	"AAAA": "IPV6 Adress Record",
	"AFSDB": "AFS Data Base Record",
	"APL":  "Adress Prefix List",
	"CAA":  "Certification Authority Authorization",
	"CDNSKEY": "Child Copy of DNSKEY Record",
	"CDS":  "Child DS", 
	"CERT": "Certificate Record",
	"CNAME": "Canonical Name Record",
	"DHCID": "DHCP Identifier",
	"DLV": "DNSSEC Lookaside Validation Record",
	"DNAME": "Alias For A Name And All Its Subnames",
	"DNSKEY": "DNS Key Record",
	"DS": "Delegation Signer",
	"HIP": "Host Identity Protocol",
	"IPSECKEY": "IPsec Key",
	"KEY": "Key Record",
	"KX": "IPsec Key",
	"LOC": "Location Record",
	"MX": "Mail Exchange Record",
	"NAPTR": "Naming Authority Pointer",
	"NS": "Name Server Record",
	"NSEC": "Next Secure Record",
	"NSEC3": "Next Secure Record Version 3",
	"NSEC3PARAM": "NSEC3 parameters",
	"OPENPGPKEY": "OpenPGP public key record",
	"PTR": "PTR Resource Record",
	"RRSIG": "DNSSEC signature",
	"RP": "Responsible Person",
	"SIG": "Signature",
	"SMIMEA":"S/MIME cert association",
	"SOA": "Start Of [A Zone Of] Authority Record",
	"SRV": "Service Locator",
	"SSHFP": "SSH Public Key Fingerprint",
	"TA": "DNSSEC Trust Authorities",
	"TKEY":  "Transaction Key Record",
	"TLSA":  "TLSA certificate association",
	"TSIG":  "Transaction Signature",
	"TXT":  "Text Record",
	"URI":  "Uniform Resource Identifier"
}

getDate = lambda: strftime("%m-%d-%y-%H-%M-%S")
loadRecords = lambda: list(RECORDS)