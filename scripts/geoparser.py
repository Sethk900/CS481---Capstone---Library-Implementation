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

:param infilepath: Path to a txt file containing raw text that represents the body of a given journal article.
:type path: str
:param 
'''
def geoparse_single_file(infilepath: str, outfilepath: str = None) -> str:
        if outfilepath is None:
                outfilepath = infilepath.split('.')[0] + '_output.txt'
        outfile = open(outfilepath, 'w', encoding='utf-8')
        infile = open(infilepath, 'r', encoding = 'utf-8')
        content = infile.read()
        content = content.encode('utf-8')
        content_string = str(content)
        words = content_string.split(' ')
        for word in words:
                if len(word) < 2:
                        continue
                #print(word + " of type " + str(type(word)))
                #continue
                output = geo.geoparse(word)
                '''
                IMPLEMENT FILTERS HERE
                Filters, at least right now, are typically implemented using regular expressions.
                To implement one, you should build a regular expression that matches an attribute that you want to exclude from the geoparser output.
                Then, use the if statement below to filter out geonames that possess that attribute.
                '''
                if len(output) > 0 and capital.match(word):
                        outfile.write(str(output))
                        outfile.write('\n')
        outfile.close()
        infile.close()
        return outfilepath
