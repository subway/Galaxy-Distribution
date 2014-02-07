#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import compareStatGraph as csg, sys, time, os, numpy as np, matplotlib.pyplot as plt
from subprocess import call

labels = [] #Labels
files = [] #Input contig files
reference = "" #Reference genome
genes = "" #Genefile
scaffolds = False
minThreshold = 0;
maxThreshold = 1000;
threads = 0 #Nr of threads 
html_file = ""
path = ""

prefix = os.getcwd().split("galaxy-dist")[0]+"galaxy-dist/static/stat/"

for arg in sys.argv:
	if arg.startswith('Label'):
		labels.append(arg[5:].replace(' ', '_'))
	elif arg.startswith('File'):
		files.append(arg[4:])
	elif arg.startswith('Ref'):
		reference = arg[3:]
	elif arg.startswith('Gene'):
		genes = arg[4:]
	elif arg.startswith('Scaff'):
		scaffold = True
	elif arg.startswith('Min'):
		minThreshold = int(arg[3:])
	elif arg.startswith('Max'):
		maxThreshold = int(arg[3:])
	elif arg.startswith('Thr'):
		try:
			threads = int(arg[3:])
		except ValueError:
			threads = 0
	else: #path
		path = arg
			
if len(files) == 0:
	raise ValueError('Provide at least one fasta file')
elif (len(labels) != 0) and (len(labels) != len(files)):
	raise ValueError('Number of labels does not match 0 or the number of files with contigs %d vs %d' % (len(labels), len(files)))
elif (minThreshold >= maxThreshold):
	raise ValueError('Threshold minimum cannot be larger than threshold maximum %d vs %d' % (minThreshold, maxThreshold))
else:
	#Validation complete
	#Compute quality assessment
	oscommand = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/quast/quast.py "
	outdir = prefix+time.strftime("%d%m%Y-%H%M%S")
        os.system("mkdir "+path)#outdir)
        oscommand += '-o '+path#+outdir
		
	if reference != "":
		oscommand += " -R "+reference
	lbl = ""
	if len(labels) != 0:
		lbl = " -l \""
		for l in labels:
			lbl += l+", "
		lbl = lbl[0:len(lbl)-2]+"\""
		oscommand += lbl
	if genes != "":
		oscommand += " -G "+genes
	if ((minThreshold != 0) | ( maxThreshold != 1000)):
	    oscommand += " -t "+minThreshold+","+maxThreshold
	if scaffolds:
	   oscommand += " --scaffolds"
	if threads != 0:
	    oscommand += " -T "+threads
	    
	contig = ""
	for f in files:
		contig += " "+f
	oscommand += contig

	#Run command
	os.system(oscommand)


	#Process result, add xy-plot functionality and assessment
	oldReport = open(path+'/report.html', 'r')
	newReport = open(path+'/newReport.html', 'w')

	#Add checkbox for xy-plot
	#Make barchart
	header = 'A B C D E F'
	header = header.split(' ')
	x = [10, 5, 20, 30, 40, 100]

	y = [1.0, 4.5, 5, 6, 7, 25]

	csg.makeStaticPlot(path, header, x, 'Ylabel', 'Test plot')
	csg.makeScatterPlot(path, header, x, y, 'x-label', 'y-label', 'Test plot')

	#Add conclusion
	conclusion = csg.getScript()
	if len(reference) == 0:
		conclusion += csg.assessOutput(path+'/json/report.json', False, path)
	else:
		conclusion += csg.assessOutput(path+'/json/report.json', True, path)
	#conclusion += csg.createddl('test')
	#conclusion += '\t<a href="latestBARplot.jpeg" target="_blank">Latest barplot here</a><br>'
	#conclusion += '\n<a href="latestXYplot.jpeg" target="_blank">Latest scatterplot here</a>'
	for line in oldReport:
		if 'id=\'subheader\'' not in line:
			newReport.write(line)
		else:
			newReport.write(line+conclusion)
	
	#Show result
	url = 'newReport.html'
	result = open('result.html', 'w')
	result.write('<html>')
	result.write('  <head>')
	result.write('    <meta http-equiv="refresh" content="0; url='+url+'" />')
	result.write('  </head>' )
	result.write('  <body>')
	result.write('    Redirecting to resultpage... <br><a href="'+url+'">Click here if you are not redirected</a>')
	result.write('  </body>')
	result.write('</html>')
	result.close()
