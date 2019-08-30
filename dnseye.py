#-*-coding: utf-8-*-
from dns import resolver
from sys import argv 
from optparse import OptionParser as opt
from lib import *



def main(args=[]):
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-d", "--dns", dest="dns", default=0, help="Set a DNS.")
	op.add_option("-s", "--save", action="store_true", dest="save", default=False,help="Save all the gathered info in a file.")
	op.add_option("-f", "--filename", dest="filename", default="{}.txt".format(getDate()), help="Set the file's name.")
	op.add_option("-o", "--only", dest="only", default="all", help="If you want to check just a few records, you should use --only record1,record2,record3")
	op.add_option("-n", "--not", dest="no", default="", help="If you don't want to check some records, you should use --not notThisrecord1,notThisrecord2")
	op.add_option("-p", "--doNotPrint", action="store_false", dest="print", default=True, help="Use this flag if you don't want to print the output in the console.")
	op.add_option("-l", "--listRecords", action="store_true", dest="listRecords", help="Display a list with all DNS records and their functions.")
	(o, args) = op.parse_args()
	print("\n\n\n")
	if not o.dns and not o.listRecords:
		print("You didn't define a DNS...")
		exit()

	if o.save:
		log = open(o.filename, "w")

	o.only = o.only.upper()
	o.no = o.no.upper()
	only = o.only.split(",")
	no =  o.no.split(",")
	if only[0] != "ALL":
		recordList = only
	else:
		recordList = loadRecords()

	if str(o.dns)[:4] == "www." and o.recordList:
		o.dns = o.dns[4:]

	if o.listRecords:
		text = ""
		for record in recordList:
			if record in no:
				continue
			text += "{} - {}\n".format(record, RECORDS[record])
		print(text)
		if o.save:
			log.write("\n{}".format(text))
	else:
		for record in recordList:
			if record in no:
				continue
			try:
				query = resolver.query(o.dns, record)
			except:
				text = "-"*40
				text += "\n 	{} did not answared.".format(record)
			else:
				text = getText(query, record)
			if o.print:
				print(text)
			if o.save:
				log.write(text + "\n")
	if o.save:
		log.close() 


if __name__ == '__main__':
	banner()
	main(args=argv[0:])