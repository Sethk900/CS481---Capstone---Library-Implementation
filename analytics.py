import os
from scripts.geoparser import geoparse_single_file
from scripts.xmlparser import xml_parse_single_file
from scripts.analysis import analyze_single_file


'''
generate_file_label
Accepts as input a path to an XML file, parses the raw text from the file, geoparses the resultant text, and analyses the geoparser results to ultimately provide
a prediction of the area in which the study took place.
Returns the predicted study location as a dictionary object.
:param path: path to an XML file for which you want to predict the geographic study location
:type path: str
'''


def generate_file_label(path: str, keep_generated_files: bool = False) -> dict:
    generated_files = []
    raw_text_file = xml_parse_single_file(path)
    generated_files.append(raw_text_file)
    geoparser_results = geoparse_single_file(path, path.replace('.txt', '') + '_output.txt')
    predicted_study_location = analyze_single_file(geoparser_results)
    result = {}
    filename = path.split('/')
    filename = filename[len(filename)]
    result[filename] = predicted_study_location

    # If user doesn't want to keep the generated files, remove them
    removal_string = "rm " + raw_text_file + " " + geoparser_results
    os.system(removal_string)

    # Return the article location label as a dict
    return result
