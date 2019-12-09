#!/usr/bin/python3
import xml.etree.ElementTree as ET
import glob, os
import argparse

parser = argparse.ArgumentParser(description='Creates list from directory of jpg and xml files')
parser.add_argument("inputdir", help="Directory (directly) containing all jpg and xml files")
parser.add_argument("outputfile", help="File to which output will be written")
args = parser.parse_args()

entrylist = ''
for fpath in glob.glob(os.path.join(args.inputdir, "*.xml")):
	root = ET.parse(fpath).getroot()
	impath = root.find('filename').text
	for bbox in root.findall('object'):
		classname = bbox.find('name').text
		coords = bbox.find('bndbox')
		entrylist += ("%s,%s,%s,%s,%s,%s\n" % (impath, coords[0].text, coords[1].text, coords[2].text, coords[3].text, classname))

with open(args.outputfile, "w+") as myfile:
	myfile.write(entrylist)
