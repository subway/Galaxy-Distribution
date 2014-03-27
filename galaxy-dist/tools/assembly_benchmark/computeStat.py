#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import compareStatGraph as csg, fileManipulation as fm, sys, time, os, numpy as np, matplotlib.pyplot as plt
from subprocess import call

labels = [] #Labels
files = [] #Input contig files
reference = "" #Uploaded reference genome
dbRef = [] #Builtin reference genome
multi = False
genes = "" #Uploaded genefile
dbGeneOK = False #Check if builtin genefile will be used
dbGene = [] #Builtin genefiles
scaffolds = False
minThreshold = 0;
maxThreshold = 1000;
threads = 0 #Nr of threads 
html_file = ""
path = ""

refPath = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/reference/refGen/"
genePath = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/reference/genefiles/" 
builtInRef = {'NC_002505':refPath+'NC_002505.fna',
	      'NC_002505G':genePath+'NC_002505.gff',
	      'NC_002506':refPath+'NC_002506.fna',
	      'NC_002506G':genePath+'NC_002506.gff',
	      'NC_003909':refPath+'NC_003909.fna',
	      'NC_003909G':genePath+'NC_003909.gff',
	      'NC_005707':refPath+'NC_005707.fna',
	      'NC_005707G':genePath+'NC_005707.gff',
	      'NC_007488':refPath+'NC_007488.fna',
	      'NC_007488G':genePath+'NC_007488.gff',
	      'NC_007489':refPath+'NC_007489.fna',
	      'NC_007489G':genePath+'NC_007489.gff',
	      'NC_007490':refPath+'NC_007490.fna',
	      'NC_007490G':genePath+'NC_.007490gff',
	      'NC_007493':refPath+'NC_007493.fna',
	      'NC_007493G':genePath+'NC_007493.gff',
	      'NC_007494':refPath+'NC_007494.fna',
	      'NC_007494G':genePath+'NC_007494.gff',
	      'NC_008570':refPath+'NC_008570.fna',
	      'NC_008570G':genePath+'NC_008570.gff',
	      'NC_009007':refPath+'NC_009007.fna',
	      'NC_009007G':genePath+'NC_009007.gff',
	      'NC_009008':refPath+'NC_009008.fna',
	      'NC_009008G':genePath+'NC_009008.gff',
	      'NC_010063':refPath+'NC_010063.fna',
	      'NC_010063G':genePath+'NC_010063.gff',
	      'NC_010079':refPath+'NC_010079.fna',
	      'NC_010079G':genePath+'NC_010079.gff',
	      'NC_010394':refPath+'NC_010394.fna',
	      'NC_010394G':genePath+'NC_010394.gff',
	      'NC_010397':refPath+'NC_010397.fna',
	      'NC_010397G':genePath+'NC_010397.gff',
	      'NC_012417':refPath+'NC_012417.fna',
	      'NC_012417G':genePath+'NC_012417.gff',
	      'NC_016010':refPath+'NC_016010.fna',
	      'NC_016010G':genePath+'NC_016010.gff',
	      'NC_016776':refPath+'NC_016776.fna',
	      'NC_016776G':genePath+'NC_016776.gff'
	}

prefix = os.getcwd().split("galaxy-dist")[0]+"galaxy-dist/static/stat/"

for arg in sys.argv:
	if arg.startswith('Label'):
		labels.append(arg[5:].replace(' ', '_'))
	elif arg.startswith('File'):
		files.append(arg[4:])
	elif arg.startswith('Ref'):
		reference = arg[3:]
	elif arg.startswith('dbRef'):
		key = arg[5:].split(',')
		for k in key:
			dbRef.append(builtInRef[k])
			dbGene.append(builtInRef[k+'G'])
	elif arg.startswith('dbGene'):
		dbGeneOK = True
	elif arg.startswith('Multi'):
		multi = True
	elif arg.startswith('Gene'):
		if arg != 'GeneNone':
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
	if len(dbRef) > 1: multi=True
	if multi:
		oscommand = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/quast/metaquast.py "
	else:
		oscommand = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/quast/quast.py "
        os.system("mkdir "+path)
        oscommand += '-o '+path
		
	if reference != "":
		oscommand += " -R " + reference
		if genes != "":
			oscommand += " -G " + genes
	elif len(dbRef) > 0:
		oscommand += " -R "
		for r in dbRef:
			oscommand += r+","
		#Remove last , that are not used
		oscommand = oscommand[:-1]
		if dbGeneOK:
			#mergedGenefile = open(path+'/result.gff', 'w')
			merged = 'cat'
			for genefile in dbGene:
				merged += ' '+genefile

			os.system(merged + ' > mergedGenefile.gff')
			oscommand += ' -G mergedGenefile.gff' 
	lbl = ""
	if len(labels) != 0:
		lbl = " -l \""
		for l in labels:
			lbl += l+", "
		lbl = lbl[0:len(lbl)-2]+"\""
		oscommand += lbl
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
	#os.system('rm '+path+'/result.gff')

	#Process result, add xy-plot functionality and assessment
	result = open('result.html', 'w')
	result.write('<!DOCTYPE html>\n')
	result.write('<html lang="en">\n')
	result.write('  <head></head>\n')
	result.write('  <body>\n')
	result.write('    <a name="top"><h1>Assembly Benchmark</h1></a>\n')
	result.write('    <p><h2>Content</h2>\n')
	
	if multi:#Multiple output folder
		result.write('    <dl>\n')
		for pl in [d for d in sorted(os.listdir(path), key=str.lower) if os.path.isdir(path+'/'+d)]:
			#Make scroll-links
			result.write('    <dt><a href="#'+pl+'"><strong><font color="black">'+pl+'</font></strong></a></dt>\n<dd>')
			for p in [d for d in sorted(os.listdir(path+'/'+pl), key=str.lower) if os.path.isdir(path+'/'+pl+'/'+d)]:
				if p.strip() != 'report_html_aux':
					result.write('    <a href="#'+pl+'-'+p+'"><font color="black">'+p+'</font></a><br>\n')
			result.write('    </dd><br>\n')
		result.write('    </dl>\n')
		for pathlist in [d for d in sorted(os.listdir(path), key=str.lower) if os.path.isdir(path+'/'+d)]:
			path += '/'+pathlist
			oldReport = open(path+'/report.html', 'r')
			newReport = open(path+'/newReport.html', 'w')
		
		        #Add plot file
			plot = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/draw_custom_plot.js"
			os.system('cp '+plot+' '+path+'/report_html_aux/scripts/')
			
			#Add own modifications
			for line in oldReport:
				if line.strip() == '<head>':
					newReport.write(line+csg.getScript())
				elif 'id=\'subheader\'' not in line:
					newReport.write(line)
				else:
					newReport.write(line+csg.assessOutput(path+'/json/report.json'))
			oldReport.close()
			newReport.close()
			
		        #Replace reportfile
			os.system('mv '+path+'/newReport.html '+path+'/report.html')
			
		        #Show result
			result.write('    <hr>\n')
			result.write('    <a name="'+pathlist+'"><h3>'+pathlist+'</h3></a><ul>\n')
			result.write('    <li>Result/Report (<a href="'+pathlist+'/report.html">html</a>)<br>\n')
			result.write('    <li>Result/Report (<a href="'+pathlist+'/report.txt">txt</a>)<br>\n')
			result.write('    <li>Result/Report (<a href="'+pathlist+'/transposed_report.txt">transposed txt</a>)</ul></p>\n')
			#Add all the other folders
			for p in [d for d in sorted(os.listdir(path), key=str.lower) if os.path.isdir(path+'/'+d)]:
				if p.strip() != 'report_html_aux':
					result.write('   <p><a name="'+pathlist+'-'+p+'"><strong>'+p+'</strong></a><ul>\n')
					for filename in [f for f in sorted(os.listdir(path+'/'+p), key=str.lower) if os.path.isfile(path+'/'+p+'/'+f)]:
						result.write('    <li><a href="'+pathlist+'/'+p+'/'+filename+'">'+filename+'</a><br>\n')
					result.write('    </ul></p>\n')
			result.write('    <a href="#top"><font color="black">[To the top]</font></a><br>')	
		        #Get original path
			path = path[:-len(pathlist)-1]
		result.write('    </body>\n')
		result.write('</html>')
		result.close()
						
	else: #Single output folder
		result.write('    <a href="#quast-report"><font color="black">quast-report</font></a><br>\n')
		for pl in [d for d in sorted(os.listdir(path), key=str.lower) if os.path.isdir(path+'/'+d)]:
			#Make scroll-links
			if pl.strip() != 'report_html_aux':
				result.write('    <a href="#'+pl+'"><font color="black">'+pl+'</font></a><br>\n')

		oldReport = open(path+'/report.html', 'r')
		newReport = open(path+'/newReport.html', 'w')
	       		
		#Add plot file
		plot = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/draw_custom_plot.js"
		os.system('cp '+plot+' '+path+'/report_html_aux/scripts/')
		#Add own modifications
		for line in oldReport:
			if line.strip() == '<head>':
				newReport.write(line+csg.getScript())
			elif 'id=\'subheader\'' not in line:
				newReport.write(line)
			else:
				newReport.write(line+csg.assessOutput(path+'/json/report.json'))
		oldReport.close()
		newReport.close()
                #Replace reportfile
		os.system('mv '+path+'/newReport.html '+path+'/report.html')
                #Show result
		result.write('    <hr><a name="quast-report"><h3>quast-report</h3></a><ul>\n')
		result.write('    <li>Result/Report (<a href="report.html">html</a>)<br>\n')
		result.write('    <li>Result/Report (<a href="report.txt">txt</a>)<br>\n')
		result.write('    <li>Result/Report (<a href="transposed_report.txt">transposed txt</a>)</ul></p>\n')
		#Add all the other folders
		for p in [d for d in sorted(os.listdir(path), key=str.lower) if os.path.isdir(path+'/'+d)]:
			if p.strip() != 'report_html_aux':
				result.write('   <p><a name="'+p+'"><strong>'+p+'</strong></a><ul>\n')
				for filename in [f for f in sorted(os.listdir(path+'/'+p), key=str.lower) if os.path.isfile(path+'/'+p+'/'+f)]:
					result.write('    <li><a href="'+p+'/'+filename+'">'+filename+'</a><br>\n')
				result.write('    </ul></p>\n')
		result.write('    <a href="#top"><font color="black">[To the top]</font></a><br>')
		result.write('    </ul></p>\n  </body>\n')
		result.write('</html>')
		result.close()
