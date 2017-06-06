import os

basedir = '.'
pagedir = basedir + '/content/pages'
postdir = basedir + '/content/posts'

#list all files in directory
listdir = os.listdir('.')

#remove .git from list if it exists, if not ignore it.
try:
	listdir.remove('.git')
except:
	pass

print (listdir)

#pages
listpages = os.listdir(pagedir)
print (listpages)

# https://stackoverflow.com/a/3961385/7327807
def get_line_number(phrase, file_name):
	with open(file_name, 'r') as openfile:
		for line_i, line in enumerate(openfile, 1):
			if phrase in line:
				return line_i
	openfile.close()

for i in range (0, len(listpages)):
	page_to_open = pagedir + '/' + listpages[i]
	
	lineNum = get_line_number('<style>', page_to_open)
	print(lineNum)
	
	pagefile = open(page_to_open, 'r')
	pagefile.close()





