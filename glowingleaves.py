import os

#list all files in directory
listdir = os.listdir(path='.')

#remove .git from list if it exists, if not ignore it.
try:
	listdir.remove('.git')
except:
	pass

print (listdir)
