#-*-coding: utf-8-*-
from dns import resolver
from sys import argv 
from optparse import OptionParser as opt
from lib import *
from whois import whois



def main(args=[]):
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-d", "--dns", dest="dns", default=0, help="Set a DNS, or a DNS list (-d [dns] / -d dns1,dns2,dns3)")
	op.add_option("-s", "--save", action="store_true", dest="save", default=False,help="Save all the gathered info in a file.")
	op.add_option("-f", "--filename", dest="filename", default="{}.txt".format(getDate()), help="Set the file's name.")
	op.add_option("-o", "--only", dest="only", default="all", help="If you want to check just a few records, you should use --only record1,record2,record3")
	op.add_option("-n", "--not", dest="no", default="", help="If you don't want to check some records, you should use --not notThisrecord1,notThisrecord2")
	op.add_option("-p", "--doNotPrint", action="store_false", dest="print", default=True, help="Use this flag if you don't want to print the output in the console.")
	op.add_option("-l", "--listRecords", action="store_true", dest="listRecords", help="Display a list with all DNS records and their functions.")
	op.add_option("-u", "--dontcheckup", action="store_false", dest="checkup", default=True, help="Don't check if the DNS is up, this will speed up the program.")
	op.add_option("-w", "--whoislog", action="store_true", dest="whois", default=False, help="Get information from a whois query.")
	op.add_option("-v", "--whoislcmdlist", action="store_true", dest="whoiscmd", default=False, help="Display all whois commands.")	
	op.add_option("-c", "--whoiscommands", dest="onlywhois", default="all", help="Select just a few whois commands, so the script don't print out every single one.")
	op.add_option("-m", "--whoisnotcommands", dest="notwhois", default="", help="Avoid getting the output of some whois commands.")
	(o, args) = op.parse_args()
	print("\n\n\n")
	if not o.dns and not o.listRecords:
		print("You didn't define a DNS...")
		exit()

	if o.save:
		log = open(o.filename, "w")
		bnner = banner(p=False)
		log.write("{}\n".format(bnner))

	o.only = o.only.upper()
	o.no = o.no.upper()
	only = o.only.split(",")
	no =  o.no.split(",")
	if only[0] != "ALL":
		recordList = only
	else:
		recordList = loadRecords()

	o.dns = o.dns.lower()
	dnslist = o.dns.split(",")
	for dns in dnslist:
		if o.checkup or o.whois:
			try:
				whoislog = whois(dns)
			except:
				text = "\n\n**  {} is not up.\n\n".format(dns)
				dnslist.remove(dns)
				continue
			else:
				text = "\n\n**  {} is up.\n\n".format(dns)
				if o.whois:
					o.onlywhois = o.onlywhois.lower()
					wcmd = o.onlywhois.split(",") #wcmd = whois commands
					o.notwhois = o.notwhois.lower()
					nwcmd = o.notwhois.split(",") #nwcmd = not whois commands
					if wcmd[0] == "all":
						whoislist = list(whoislog)
					else: 
						whoislist = wcmd
					for info in whoislist:
						if info in nwcmd:
							continue
						wtext ="	* {}:\n 		-{}".format(info, whoislog[info])
						if o.print:
							print(wtext)
						if o.save:
							log.write("{}\n".format(wtext))
			
			finally:
				if o.print:
					print(text)
				if o.save:
					log.write("{}\n".format(text))

			if dns[:4] == "www.":
				dnslist[dnslist.index(dns)] = dns[4:]
				dns = dns[4:]

		


	if o.listRecords:
		text = ""
		for record in recordList:
			if record in no:
				continue
			text += "{} - {}\n".format(record, RECORDS[record])
		print(text)
		if o.save:
			log.write("\n{}".format(text))
	if o.whoiscmd:
		text = "\n\n\n- Whois Commands:\n"
		for cmd in WHOISCMD:
			text += "	**{}\n".format(cmd)
		if o.print:
			print(text)
		if o.save:
			log.write(text)


	else:
		anscount = 0
		for dns in dnslist:
			text = "\n\n****  Starting analysis on {}\n\n".format(dns)
			if o.print:
				print(text)
			if o.save:
				log.write("\n{}\n".format(text))
			for record in recordList:
				if record in no:
					continue
				try:
					query = resolver.query(dns, record)
				except:
					text = "-"*40
					text += "\n 	{} did not answared.".format(record)
				else:
					text = getText(query, record)
					anscount += 1
				if o.print:
					print(text)
				if o.save:
					log.write(text + "\n")
			text = "\n\n\n||||	{} records answared.".format(anscount)

			if anscount == 0:
				if recordList == ["", ""]:
					text += "\n 		-Maybe you should add some records to the list."
				else:
					text += "\n 		- Check your internet connection."
					text += "\n 		- Check if the DNS is up."
			elif anscount == len(recordList):
				text += "\n 		- Nice, every single records answared!!!!!"
			if o.print:
				print(text)
			if o.save:
				log.write(text + "\n")
	if o.save:
		log.close() 


if __name__ == '__main__':
	banner()
	main(args=argv[0:])