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
:param tagList: List of relevant tags from this particular article to parse out (e.g. ['rawText', 'description']). If none is passed in, we take all text from the XML file.
:type tagList: List[str]
'''
def xml_parse_single_file(path, tagList = []) -> str:
        filename = path

	# [("<xocs:rawtext>","</xocs:rawtext>"),("<dc:description>","</dc:description>")] tagSetList example
        # Build the tagSetList
        tagSetList = []
        for tag in tagList:
            openTag = "<" + tag + ">"
            closeTag = "</" + tag + ">"
            tempList = []
            tempList.append(openTag)
            tempList.append(closeTag)
            tagSetTuple = tuple(tempList)
            tagSetList.append(tagSetTuple)
        print("tagSetList tuple: " + str(tagSetList))

        if not filename.endswith(".xml"):
            print("ERROR: You passed in a path to a non-xml file. Please ensure that the path is correct.")
            return

        with open(filename, 'r', errors='ignore') as file:
            #Check for match
            line = file.read()
            print("Parsing XML for file " + filename)
            f = open(filename.replace('xml', 'txt'),"w")

            # Only executes if no tag list was passed in
            if len(tagList) == 0:
                print("WARNING: No list of relevant tags passed in. The XML parser will parse out all text between all tags.")
                print("LOG: writing to outfile...")
                line = re.sub(xml_end_tag, '\n', line)
                f.write(re.sub(xml_tags, ' ', line))
                f.close()
                return filename.replace('xml', 'txt')

            # Only executes if tag list was passed in
            for tags in tagSetList: # 'tags' is a two-tuple of XML tags (e.g. ("<xocs:rawtext>","</xocs:rawtext>"))
                print("LOG: Processing a file with tagSetList " + str(tagSetList))
                fileContent = line
                print("LOG: Searching for text entries between " + tags[0] + " and " + tags[1] + ".")
                relevantTexts = re.findall(tags[0] + '.*' + tags[1], fileContent)
                relevantTextCount = str((len(relevantTexts)))
                print("Found " + relevantTextCount + " relevant texts.")
                for relevantText in relevantTexts:
                    if relevantText:
                        #removes all tags from the output and writes to the file
                        line = re.sub(xml_end_tag, '\n', line)
                        f.write(re.sub(xml_tags, ' ', line))
                    else:
                        continue
            f.close()
        return filename.replace('xml', 'txt')

'''
retrieve_article_text
Similar to xml_parse_single_file, but doesn't write any output to file; instead, returns raw text as a string object.
:param path: Path to the XML file that will be parsed in this function
:type path: str
:param tagList: List of relevant tags from this particular article to parse out (e.g. ['rawText', 'description']). If none is passed in, we take all text from the XML >:type tagList: List[str]
'''
def retrieve_article_text(path, tagList = []) -> str:
        filename = path
        rawText = ""
        # Build the tagSetList
        tagSetList = []
        for tag in tagList:
            openTag = "<" + tag + ">"
            closeTag = "</" + tag + ">"
            tempList = []
            tempList.append(openTag)
            tempList.append(closeTag)
            tagSetTuple = tuple(tempList)
            tagSetList.append(tagSetTuple)
        print("tagSetList tuple: " + str(tagSetList))
        if not filename.endswith(".xml"):
            print("ERROR: You passed in a path to a non-xml file. Please ensure that the path is correct.")
            return

        with open(filename, 'r', errors='ignore') as file:
            #Check for match
            line = file.read()
            print("Parsing XML for file " + filename)
            f = open(filename.replace('xml', 'txt'),"w")

            # Only executes if no tag list was passed in
            if len(tagList) == 0:
                print("WARNING: No list of relevant tags passed in. The XML parser will parse out all text between all tags.")
                line = re.sub(xml_end_tag, '\n', line)
                return line

            # Only executes if tag list was passed in
            for tags in tagSetList: # 'tags' is a two-tuple of XML tags (e.g. ("<xocs:rawtext>","</xocs:rawtext>"))
                print("LOG: Processing file with tagSetList " + str(tagSetList))
                fileContent = line
                print("LOG: Searching for text entries between " + tags[0] + " and " + tags[1] + ".")
                relevantTexts = re.findall(tags[0] + '.*' + tags[1], fileContent)
                relevantTextCount = str((len(relevantTexts)))
                print("Found " + relevantTextCount + " relevant texts.")
                for relevantText in relevantTexts:
                    if relevantText:
                        #removes all tags from the output and writes to the file
                        line = re.sub(xml_end_tag, '\n', line)
                        rawText = rawText + line
                    else:
                        continue
        return rawText
