


# find a phrase's line number in a file
# https://stackoverflow.com/a/3961385/7327807
def get_line_number(phrase, file_name):
	with open(file_name, 'r') as openfile:
		for line_i, line in enumerate(openfile, 1):
			if phrase in line:
				return line_i
	openfile.close()
