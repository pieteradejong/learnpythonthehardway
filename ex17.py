from sys import argv
from os.path import exists

script, from_file, to_file = argv # put cmd line args into vars

print "Copying file from %s to %s." % (from_file, to_file)

indata = open(from_file).read() # open and read from_file, put contents in indata
out_file = open(to_file, 'w') # open the file in write mode
out_file.write(indata) # write the contents of indata to out_file
out_file.close()

print "Alrght, all done."