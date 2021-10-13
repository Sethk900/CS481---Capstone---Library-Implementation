import json, ast, os, re

def analyze_single_file(path):
	checked_names = {}
	top_name = ""

	try:
		with open(path, "r", encoding='utf-8') as Finput:
			lines = Finput.readlines()
	except:
		print("ERROR: Unable to read lines from infile.")
		return

	for line in lines:
		try:
			word = ast.literal_eval(line)
		except:
			print("WARNING: Unable to perform a literal evaluation of line " + str(line) + '.')
			continue
		placename = word[0]['word']
		if placename not in checked_names:
			checked_names[placename] = 1
		else:
			checked_names[placename] = checked_names[placename] + 1

	if(checked_names):
		top_name = max(checked_names, key=checked_names.get)
		max_count = checked_names[top_name]
		checked_names[top_name] = 0
		second_name = max(checked_names, key=checked_names.get)

	Finput.close()
	return top_name
