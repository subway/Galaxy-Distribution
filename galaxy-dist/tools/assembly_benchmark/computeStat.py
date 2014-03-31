#!/usr/bin/python
import compareStatGraph as csg, combineResultReference as crr, sys, os

def runCommand(customPath, reference, gene, labels, files, filetype):
	oscommand = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/quast/quast.py "
	os.system('mkdir '+customPath) 
	oscommand += '-o '+customPath
		
	if reference != '':
		oscommand += ' -R ' + reference
		if gene != '':
			oscommand += ' -G ' + gene
	
	lbl = ''
	if len(labels) != 0:
		lbl = ' -l "'
		for l in labels:
			lbl += l+', '
		lbl = lbl[0:len(lbl)-2]+'"'
		oscommand += lbl
	if ((minThreshold != 0) | ( maxThreshold != 1000)):
	    oscommand += ' -t '+minThreshold+','+maxThreshold
	if filetype:
	   oscommand += ' --scaffolds'
	if threads != 0:
	    oscommand += ' -T '+threads
	    
	dataset = ''
	for f in files:
		dataset += ' '+f
	oscommand += dataset

	#Run command
	os.system(oscommand)

def writeHtmlFile(path):
	#Process result, add xy-plot functionality and assessment
	result = open('result.html', 'w')
	result.write('<!DOCTYPE html>\n')
	result.write('<html lang="en">\n')
	result.write('  <head></head>\n')
	result.write('  <body>\n')
	result.write('    <a name="top"><h1>Assembly Benchmark</h1></a>\n')
	result.write('    <p><h2>Content</h2>\n')
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
		#result.write('    <hr>\n')
		result.write('    <hr>\n<a name="'+pathlist+'"><h3>'+pathlist+'</h3></a><ul>\n')
		for filename in [f for f in sorted(os.listdir(path), key=str.lower) if os.path.isfile(path+'/'+f)]:
			result.write('    <li><a href="'+pathlist+'/'+filename+'">'+filename+'</a><br>\n')
		result.write('    </ul></p>\n')
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

#Main code handler
if __name__ == '__main__':

	global refPath; refPath = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/reference/refGen/"
	global genePath; genePath = os.getcwd().split("galaxy-dist")[0]+ "galaxy-dist/tools/assembly_benchmark/reference/genefiles/" 
	
	global prefix; prefix = os.getcwd().split("galaxy-dist")[0]+"galaxy-dist/static/stat/"
	global history; history = [] #History element with previous run
	global contigLabel; contigLabel = [] #Labels for contig files
	global scaffoldLabel; scaffoldLabel = [] #Labels for scaffold files
	global contig; contig = [] #Input contig files
	global scaffold; scaffold = [] #Input scaffold files
	global ref; ref = '' #Uploaded reference genome
	global dbRef; dbRef = [] #Builtin reference genome
	global multi; multi = False #If uploaded ref is multiple files in one or not
	global minThreshold; minThreshold = 0;
	global maxThreshold; maxThreshold = 1000;
	global threads; threads = 0 #Nr of threads 
	global path; path = ''	
	
	for arg in sys.argv:
		if arg.startswith('History'):
			history.append(arg[7:])
		elif arg.startswith('Dataset'):
			data = arg[7:].split(',')
			if data[2] == 'contig':
				contig.append(data[1])
				if data[0] != '':
					contigLabel.append(data[0])
			else:
				scaffold.append(data[1])
				if data[0] != '':
					scaffoldLabel.append(data[0])
		elif arg.startswith('dbRef'):
			data = arg[5:].split(':')
			key = data[0].split(',')
			if data[1] == 'None':
				for k in key:
					dbRef.append(refPath+k+'.fna,')
			else:
				for k in key:
					dbRef.append(refPath+k+'.fna,'+genePath+k+'.gff')
			if len(dbRef) > 1: multi = True
		elif arg.startswith('Ref'):
			ref = arg[3:]
			if ref.split(',')[1] == 'True':
				multi = True
		elif arg.startswith('Min'):
			minThreshold = int(arg[3:])
		elif arg.startswith('Max'):
			maxThreshold = int(arg[3:])
		elif arg.startswith('Thr'):
			threads = int(arg[3:])
		else: #path
			path = arg

	if len(contig) + len(scaffold) == 0:
		raise ValueError('Provide at least one dataset')
	elif (len(contigLabel) != 0) and (len(contigLabel) != len(contig)):
		raise ValueError('Number of labels does not match 0 or the number of datasets with contigs')
	elif (len(scaffoldLabel) != 0) and (len(scaffoldLabel) != len(scaffold)):
		raise ValueError('Number of labels does not match 0 or the number of datasets with scaffolds')
	elif (minThreshold >= maxThreshold):
		raise ValueError('Threshold minimum cannot be larger than threshold maximum %d vs %d' % (minThreshold, maxThreshold))
	elif ((len(contig)+len(scaffold)) > 1) & ((len(dbRef) > 1) | multi):
		raise ValueError('Cannot have multiple datasets and reference genomes\n \
		Choose either one dataset with multiple reference genomes or\n \
		one reference genome with multiple datasets')
	else: #Validation complete
		os.system('mkdir '+path)
		
		if ((len(dbRef) < 2) & (not multi)):
			reference = ''
			gene = ''
			if len(ref) != 0:
				tmpRef = ref.split(',')
				reference = tmpRef[0]
				if tmpRef[2] != 'None':
					gene = tmpRef[2]
			elif len(dbRef) != 0:
				data = dbRef[0].split(',')
				reference = data[0]
				gene = data[1]
			if len(contig) != 0:
				resultPath = path+'/Contig'
				runCommand(resultPath, reference, gene, contigLabel, contig, False)
			if len(scaffold) != 0:
				resultPath = path+'/Scaffold'
				runCommand(resultPath, reference, gene, scaffoldLabel, scaffold, True)
			if (len(contig) != 0) & (len(scaffold) != 0):
				if (len(contigLabel)+len(scaffoldLabel)) == (len(contig)+len(scaffold)):
					runCommand(path+'/combined_dataset', reference, gene, contigLabel+scaffoldLabel, contig+scaffold, False)
				else:
					runCommand(path+'/combined_dataset', reference, gene, '', contig+scaffold, False)	
		else:
			data = []
			scaff = False
			if len(contig) != 0:
				data.append(contigLabel)
				data.append(contig)
			else:
				data.append(scaffoldLabel)
				data.append(scaffold)
				scaff = True
			if len(dbRef) != 0:
				for r in dbRef:
					reference = r.split(',')
					runCommand(path+'/'+reference[0].split('/')[-1][:-4], reference[0], reference[1], data[0], data[1], scaff)
				os.system('mkdir '+path+'/combined_reference')
				os.system('mkdir '+path+'combined_reference/json')
				os.system('co -rf '+path+dbRef[0].split(',')[0].split('/')[-1][:-4]+'/report_html_aux '+path+'/combined_reference')
				os.system('cp '+path+'/B_cereus_ATCC_1098/report.html '+path+'/combined_reference')
				#os.system('cp -rf '+path+'/B_cereus_ATCC_1098/json '+path+'/combined_reference')
				for i in range(1,len(dbRef)):
					if i == 1:
						crr.combine(path+'/'+dbRef[0].split(',')[0].split('/')[-1][:-4], \
							  path+'/'+dbRef[1].split(',')[0].split('/')[-1][:-4], \
							  path+'/combined_reference', False)
					else:
						crr.combine(path+'/combined_reference', \
							  path+'/'+dbRef[i].split(',')[0].split('/')[-1][:-4], \
							  path+'/combined_reference', True)
			elif len(ref) != 0:
				reference = ref.split(',')
				refSplit = []
				gene = ''
				with open(reference[0]) as r:
					content = r.read()
					refSplit = content.split('>')
				if reference[2] != 'None':
					with open(reference[2]) as r:
						content = r.read()
						gene = content.split('###')
					for i in range(len(refSplit)):
						tmpRef = open(path+'/tmpRef.fna','w')
						tmpRef.write('>'+refSplit[i])
						tmpRef.close()
						tmpGene = open(path+'/tmpGene.gff','w')
						tmpGene.write(gene[i]+'###')
						tmpGene.close()
						for h in heading:
							if h.startswith('NC_'):
								runCommand(path+'/'+h, path+'/tmpRef.fna', path+'/tmpGene.gff', data[0], data[1], scaff)
								break
						os.system('rm '+path+'/tmpRef.fna '+path+'/tmpGene.gff')
				else:
					for i in range(len(refSplit)):
						tmpRef = open(path+'/tmpRef.fna','w')
						tmpRef.write('>'+refSplit[i])
						tmpRef.close()
						heading = refSplit[i].split('\n')[0].split('|')
						for h in heading:
							if h.startswith('NC_'):
								runCommand(path+'/'+h, path+'/tmpRef.fna', '', data[0], data[1], scaff)
								break
						os.system('rm '+path+'/tmpRef.fna')
		writeHtmlFile(path)
