#!/usr/bin/python
import os
#read in directory, name,
print "beware ~ and ä-ö-ü not working, sart with / "
print "the directory and the name together have to for a valid path"

directory = raw_input('Please enter directory:')
if directory:
	print directory
else: print "enter directory"

name = raw_input('Please enter project name:')
if directory:
	print name
else: print "enter directory"

#Dicise wether you want to use virtualenv
print "Do you want to use virtualenv?"
d = raw_input("for yes type j")
if d == "j":
	os.system("virtualenv %s" % name)
	os.system("cd %s" % name)
	os.system("source bin/activate")
else:
	# create directory and cd
	os.chdir(directory)
	os.system("mkdir %s && cd %s" % name, name)



# git: init and add
os.system("git init")
os.system("git add .")













if __name__ == '__main__':
    main()