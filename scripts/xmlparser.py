import sys
import os
import re
from pathlib import Path

#regular expression to remove xml tags
xml_tags = re.compile('<.*?>')

'''
xml_parse_single_file
Accepts as input a path to an XML file. Parses the relevant fields out of the XML file, writes the result to a text file, and returns the path to the text file.
:param path: Path to the XML file that will be parsed in this function
:type path: str
'''
def xml_parse_single_file(path) -> str:
        with path as filename:
            if not filename.endswith(".xml"):
                return
            with open(filename, 'r', errors='ignore') as file:
                tagFound = False
                #Check for match
                line = file.read()
                print(filename)
                f = open(directory2 + '/' + folder[0] + filename,"w")
                for tags in folder[1]:
                    results = re.findall(tags[0] + '.*' + tags[1],line)
                    for result in results:
                        #Send output to test file
                        if result:
                            #removes all tags from the output and writes to the file
                            f.write(re.sub(xml_tags, ' ', result))
                            tagFound = True
                        else:
                            pass
                f.close()
                stats1[idx]+=1
                if tagFound == True:
                    stats2[idx]+=1
                else:
                    print("NO TAGS FOUND")
