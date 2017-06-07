import os
import getlinenumber

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


for i in range (0, len(listpages)):
	page_to_open = pagedir + '/' + listpages[i]
	
	lineNum = getlinenumber.get_line_number('<style>', page_to_open)
	print(lineNum)
	
	pagefile = open(page_to_open, 'r')
	pagefile.close()
