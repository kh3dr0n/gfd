#!/usr/bin/python
# Kh3dr0n 2013
# hack2brain.blogspot.com
# miro19k@gmail.com
import urllib,urllib2,sys
if(len(sys.argv) == 1):
	print("gfd url [cssfilename]")
	sys.exit()
src = urllib2.urlopen(sys.argv[1]).read();
url = src[src.find('url(')+4:src.find(')',src.find('url('))]
name = src[src.find('font-family:')+14:src.find(';\n',src.find('font-family'))-1]
print("Download TTF File ")
urllib.urlretrieve (url, "'"+name+".ttf'")
print("Done")
src = src.replace(url,name+".ttf")
if(len(sys.argv) == 3):
	text_file = open(sys.argv[2], "w")
	print("Saving " + sys.argv[2] + " File");
else:
	text_file = open("font.css", "w")
	print("Saving font.css File");
text_file.write(src)
text_file.close()