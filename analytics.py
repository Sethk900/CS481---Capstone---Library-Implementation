from scripts.geoparser import geoparse_single_file
from scripts.xmlparser import xml_parse_single_file
from scripts.analysis import geoparser_output_analysis
'''
generate_file_label
Accepts as input a path to an XML file, parses the raw text from the file, geoparses the resultant text, and analyses the geoparser results to ultimately provide
a prediction of the area in which the study took place.
Returns the predicted study location as a dictionary object.
:param path: path to an XML file for which you want to predict the geographic study location
:type path: str
'''
def generate_file_label(path) -> dict:
	generated_files = []
	raw_text_file = xml_parse_single_file(path)
	geoparser_results = geoparse_single_file(path)
	predicted_study_location = geoparser_output_analysis(geoparser_results)
	print("Predicted Study Location: " + predicted_study_location['word'])
	return predicted_study_location

