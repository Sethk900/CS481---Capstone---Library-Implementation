 #!/usr/bin/python3
# Currently modified to process only one file each time the script is run
from mordecai import Geoparser
import re
import os

xmlfile = re.compile('.*\.xml')
capital = re.compile('.*[A-Z]*.*')
geo = Geoparser()

'''
geoparse_single_file
Accepts as input the path to a file of raw text representing the body of a given journal article. The function parses out any location names and writes them to an output file as a list of Python dictionaries.

:param path: Path to a txt file containing raw text that represents the body of a given journal article.
:type path: str
'''
def geoparse_single_file_deprecated(path) -> str:
	inputfile = path
	name, extension = os.path.splitext(inputfile)
	outfilename = name + "_output.txt"
	if xmlfile.match(inputfile): # Only process XML files
		with open(inputfile, "r", encoding="utf-8") as infile:
			print("Geoparsing data from " + inputfile + "...")
			try:
				data = infile.readlines().encode('utf-8')
			except:
				with open(outfilename, "w") as outfile:
					outfile.write("Unicode Error")
				outfile.close()
				data = "none"
		infile.close()
		for line in data:
			for word in line.split(): # For testing: eventually we'll want to parse a single word at a time to see what the geoparser is having a hard time with
				output = geo.geoparse(str(word))
				with open(outfilename, "w", errors='ignore') as outfile:
					for line in output:
						'''
						IMPLEMENT FILTERS HERE
						Filters, at least right now, are typically implemented using regular expressions. 
						To implement one, you should build a regular expression that matches an attribute that you want to exclude from the geoparser output. 
						Then, use the if statement below to filter out geonames that possess that attribute.
						'''
						if capital.match(line['word']): # Filter out place names that don't contain any capital later (Comment out to remove filter)
							try:
								outfile.write(str(line))
								outfile.write("\n")
							except:
								print("Unicode error when trying to write word " + word['word'] + " to outfile.")

				outfile.close()
	return outfilename

def geoparse_single_file(infilepath, outfilepath):
        outfile = open(outfilepath, 'w', encoding='utf-8')
        infile = open(infilepath, 'r', encoding = 'utf-8')
        content = infile.read()
        content = content.encode('utf-8')
        content_string = str(content)
        words = content_string.split(' ')
        for word in words:
                if len(word) < 2:
                        continue
                print(word + " of type " + str(type(word)))
                #continue
                output = geo.geoparse(word)
                if len(output) > 0:
                        outfile.write(str(output))
                        outfile.write('\n')
        outfile.close()
        infile.close()
        return outfilepath
