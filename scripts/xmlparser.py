import sys
import os
import re
from pathlib import Path

#regular expression to remove xml tags
xml_tags = re.compile('<.*?>')
xml_end_tag = re.compile('<\/.*?>')
'''
xml_parse_single_file
Accepts as input a path to an XML file. Parses the relevant fields out of the XML file, writes the result to a text file, and returns the path to the text file.
:param path: Path to the XML file that will be parsed in this function
:type path: str
'''
def xml_parse_single_file(path) -> str:
        filename = path
        if not filename.endswith(".xml"):
            return
        print('open is assigned to %r' % open)
        with open(filename, 'r', errors='ignore') as file:
            #Check for match
            lines = file.readlines()
            print(filename)
            f = open(filename.replace('xml', 'txt'),"w")
            for line in lines:
                if line:
                    #removes all tags from the output and writes to the file
                    line = re.sub(xml_end_tag, '\n', line)
                    f.write(re.sub(xml_tags, ' ', line))
                    tagFound = True
                else:
                    continue
            f.close()
        return filename.replace('xml', 'txt')
