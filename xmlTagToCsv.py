import csv
import bs4
import sys

def main():
	argc = len(sys.argv)
	if argc<2:
		print(f"\nusage: {sys.argv[0]} <xml file> <csv output> <data to extract 1> <data to extract2>\nThis is just to extract 2 items from xmlmorni")
		sys.exit(1)

	with open(sys.argv[1],'r') as r:
		data = r.read()

	bs_data = bs4.BeautifulSoup(data,'xml')
	sid = bs_data.findAll(sys.argv[3].upper())
	stitle = bs_data.find_all(sys.argv[4].upper())
	with open(sys.argv[2],'w', newline='') as f:
		wr = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
		wr.writerow([sys.argv[3], sys.argv[4]])
		#Using comprenhension lists and zip to write the tuple to a csv rows
		#extracting just the text from the tuple
		wr.writerows([(x.text,y.text) for x,y in zip(sid, stitle) if x and y != None])
	
if __name__ == '__main__':
	main()
