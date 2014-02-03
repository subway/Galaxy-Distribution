#!/usr/bin/python
import sys, time, os
from subprocess import call

labels = [] #Labels
files = [] #Input contig files
reference = "" #Reference genome
#prefix = "/usit/abel/u1/sabbai/Master/galaxy-dist/static/stat/"
prefix = os.getcwd().split("galaxy-dist")[0]+"galaxy-dist/static/stat/"

for arg in sys.argv:
	if arg.startswith('Label'):
		labels.append(arg[5:])
	elif arg.startswith('File'):
		files.append(arg[4:])
	elif arg.startswith('Ref') & (arg[3:] != "None"):
		reference = arg[3:]	

if (len(labels) != 0) and (len(labels) != len(files)):
	raise ValueError('Number of labels does not match 0 or the number of files with contigs %d vs %d' % (len(labels), len(files))); exit(1)
else:
	#Validation complete
	#Compute quality assessment
	#oscommand = "/usit/abel/u1/sabbai/Master/galaxy-dist/tools/assembly_benchmark/quast/quast.py "
	oscommand = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/quast/quast.py "
	outdir = prefix+time.strftime("%d%m%Y-%H%M%S")
        os.system("mkdir "+outdir)
        oscommand += '-o '+outdir+" "

	if reference != "":
		oscommand += "-R "+reference+" "
	lbl = ""
	if len(labels) != 0:
		lbl = "-l \""
		for l in labels:
			lbl += l+", "
		lbl = lbl[0:len(lbl)-2]+"\" "
		oscommand += lbl
	contig = ""
	for f in files:
		contig += f+" "
	oscommand += contig

	#Run command
	os.system(oscommand)

	f = open("stat.txt", 'w')

	try:
		f.write(open(outdir+"/report.txt", 'r').read())
	except:
		f.write("Cannot compute statistics")
	f.close()
