import os
import getlinenumber as functionlist

basedir = '.'
pagedir = basedir + '/content/pages'
postdir = basedir + '/content/posts'
cssdir = basedir + './css'

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
	
	lineNum = functionlist.get_line_number('<style>', page_to_open)
	print(lineNum)
	
	css_to_open = basedir + '/main.css'
	cssfile = open(css_to_open, 'r')
	data = cssfile.read()
	print (cssfile.read())
	
	pagefile = open(page_to_open, 'w')
	
	pagefile.close()

	
	
