#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import os, sys, time, numpy as np, matplotlib.pyplot as plt

# validate input
#usage = 'Usage: %s path to QUAST report.txt file' % sys.argv[0]
#global stat, title, header, plotPrefix, colorSet

def makeStaticPlot(path, header, input, y_label, plotTitle):
	fig = plt.figure()
	x = []
	y = []
	for i in range(len(header)-1,0,-1):
		x.append(header[i])
	if ('GC%' in y_label) | ('N per' in y_label):
		for i in range(len(input)-1,(len(input)-len(header)),-1):
			y.append(float(input[i]))
	else:
		for i in range(len(input)-1,(len(input)-len(header)),-1):
			y.append(int(input[i]))
	x_pos = np.arange(len(x))
	for i in range(0,len(x)):
		plt.bar(x_pos[i], y[i], align='center')
		plt.text(x_pos[i], 2.0, str(y[i]), rotation=90., ha="center", va="bottom", bbox=dict(boxstyle="square", alpha=0.5))
	plt.xticks(x_pos, x, rotation=80)
	plt.ylabel(y_label)
	plt.title(plotTitle)
	fig.tight_layout()
	plt.savefig(path+'/latestBARplot.jpeg')
	plt.close()

def makeScatterPlot(path, header, xval, yval, xlabel, ylabel):
	tmp = plt.scatter(xval, yval)
	plt.axis([0, max(xval)+5, 0, max(yval)+5])
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	#plt.legend(tmp, header, scatterpoints=1, loc='lower left', ncol=3, fontsize=10)
	plt.savefig(path+'/latestXYplot.jpeg')
	plt.close()

def addTopResult(assembly, result, title):
	result += title
	for rank in sorted(assembly, key=assembly.get, reverse=True):
		#result += '&#09;'
		result += rank
		result += ' ('
		result += str(assembly[rank])
		result += ' point)   '
	result += '<br>'
	return result

def getTopThree(assembly, data, topnumber, label):
	# Bigger is better
	top = 0
	for x in range(topnumber):
		last = top
		top = max(data)
		position = data.index(top)
		#Add points
		assembly[label[position]] += 3-x
		#If same result give same
		if (x != 0) & (top == last):
			assembly[label[position]] += 1
		#Make sure same max value won't show up
		data[position] = top*-1
       	return assembly

def getBottomThree(assembly, data, topnumber, label):
	# Smaller is better
	bottom = 0
	for x in range(topnumber):
		last = bottom
		bottom = min(i for i in data)
		position = data.index(bottom)
		#Add points
		assembly[label[position]] += 3-x
		#If same result give same
		if (x != 0) & (bottom == last):
			assembly[label[position]] += 1
		#Make sure same min value won't show up
		data[position] = bottom+max(data)+1
	return assembly

def assessOutput(quastfile, ref):
	#Assemblies
	assembly = {}
	basicAsm = {}
	misassembliesAsm = {}
	unalignedAsm = {}
	mismatchAsm = {}
	geneAsm = {}
	#remove first two line
	#quastfile.readline();quastfile.readline()
	with open('data.json') as data_file:
		data = json.load(data_file)
		label = data['assembliesNames']
		report = data['report']
								
	#label = quastfile.readline().split()
	#label.pop(0)
	for l in label:
		assembly[l] = 0
		basicAsm[l] = 0
		misassembliesAsm[l] = 0
		unalignedAsm[l] = 0
		mismatchAsm[l] = 0
		geneAsm[l] = 0	
	
	#Statistic without reference
	basicStatKeyword = ['# contigs', \
			     'Largest contig', \
			     'Total length', \
			     'N50', \
			     'N75', \
			     'L50', \
			     'L75', \
			     'GC (%)']		     
	#Misassemblies
	misassembliesKeyword = ['# misassemblies', \
				'# relocations', \
				'# translocations', \
				'# inversions', \
				'# misassembled', \
				'Misassembled contig length', \
				'# local misassemblies']
	#Unaligned
	unalignedKeyword = ['# unaligned contigs' \
			    'Unaligned contig length' \
			    '# partially unaligned contigs' \
			    '# with misassembly' \
			    '# both parts are significant' \
			    'Partially unalignes length']
	#Mismatches
	mismatchKeyword = ['# mismatches' \
			   '# indels' \
			   'Indels length' \
			   '# short indels' \
			   '# long indels' \
			   '# N']
			   
	#Genome statistic
	genomeKeyword = ['Genome fraction' \
			 'Duplication ratio' \
			 '# genes' \
			 'Largest alignment' \
			 'NG50' \
			 'NG75' \
			 'NGA50' \
			 'NGA75' \
			 'LG50' \
			 'LG75' \
			 'LGA50' \
			 'LGA75']
			 
	if ref:
		mismatchKeyword.append('# N')
		basicStatKeyword.append('Reference')
	else:
		basicStatKeyword.append('# N')
		
	x = 0; result = ""; title = ""
	dropdown = ['<select>']
	
	for line in report:quastfile.readlines():
		data = [float(number) for number in line.split() if number.replace('.','',1).isdigit()]
		if len(data) != len(label):
			data.pop(0)
		#Add dropdown data
		text = ' '.join(line.split()[:-len(data)])
		dropdown.append('  <option value "'+line+'">'+text+'</option>')
		#get top X 3 or less
		topnumber = len(label) if len(label) < 3 else 3
		#without reference stat
		if any(word in line for word in basicStatKeyword):
			print "WITH - "+line
			#title = 'Statistic without reference\t'
			if line.startswith('# contigs') | \
			   line.startswith('L') | \
			   line.startswith('GC') | \
			   line.startswith('Reference') | \
			   line.startswith('# N'):
				#assembly = getBottomThree(assembly, data, topnumber, label)
				basicAsm = getBottomThree(basicAsm, data, topnumber, label)
			else:
				#assembly = getTopThree(assembly, data, topnumber, label)
				basicAsm = getTopThree(basicAsm, data, topnumber, label)
		elif any(word in line for word in misassembliesKeyword):
			print "MISAS - "+line
			#result = addTopResult(assembly, result, title)
			#title = 'Misassemblies\t'
			mismatchAsm = getBottomThree(misassembliesAsm, data, topnumber, label)
		elif any(word in line for word in unalignedKeyword):
			print "UNAL - "+line
			#result = addTopResult(assembly, result, title)
			#title = 'Unaligned\t'
			unalignedAsm = getBottomThree(unalignedAsm, data, topnumber, label)
		elif any(word in line for word in mismatchKeyword):
			print "MISM - "+line
			#result = addTopResult(assembly, result, title)
			#title = 'Mismatches\t'
			mismatchAsm = getBottomThree(mismatchAsm, data, topnumber, label)
		elif any(word in line for word in genomeKeyword):
			print "GENE - "+line
			#result = addTopResult(assembly, result, title)
			#title = 'Genome statistics\t'
			if line.startswith('Duplication') | \
			   line.startswith('LG'):
				geneAsm = getBottomThree(geneAsm, data, topnumber, label)
			else:
				geneAsm = getTopThree(geneAsm, data, topnumber, label)
		
	result = '<b>Rank 1 - 3p&nbsp;&nbsp;&nbsp;Rank 2 - 2p&nbsp;&nbsp;&nbsp;Rank 3 - 1p</b><br>'	
	result = addTopResult(basicAsm, result, '<pre>Basic stat &#09;&#09;')
	if ref:
		#result = addTopResult(basicAsm, result, '<pre>Basic stat &#09;&#09;')
		result = addTopResult(misassembliesAsm, result, 'Misassemblies &#09;&#09;')
		result = addTopResult(unalignedAsm, result, 'Unaligned &#09;&#09;')
		result = addTopResult(mismatchAsm, result, 'Mismatches &#09;&#09;')
		result = addTopResult(geneAsm, result, 'Genome statistics&#09;')
		result += "</pre>"
		return result
	dropdown.append('</select>')
	result += dropdown
	return result
def createTable(stat):
	return null
def createTable():
	tblHeader = True
	table = ['<TABLE BORDER="0">']
	first = True
	plotnr = 0;
	for line in stat:
		table.append('<TR>')
		elements = line.split()
		if not tblHeader:
			plotnr += 1
			info = "<TD><A HREF=\"javascript:toggleImg(\'plot"+str(plotnr)+"\');\"></TD>"
			for i in range(0,len(elements)-len(header)+1):
				info = info[0:-5]+elements[i]+" </TD>"
			table.append(info[0:-5]+'</A></TD>\n')
			
			for i in range(len(elements)-1,(len(elements)-len(header)),-1):
                        	table.append('<TD>'+elements[i]+'</TD>')
		else:
			tblHeader = False
			table.append('<TD>'+elements[0]+'</TD>')
			for i in range(len(elements)-1,0,-1):
				table.append('<TD>'+elements[i]+'</TD>')

		table.append('</TR>\n')
	table.append('</TABLE>')
	return ''.join(table)  

def getScript():
	script = "function toggleImg(id){ \n \
		var img = document.getElementById(id);\n \
	        img.style.display = (img.style.display=='none' ? 'block' : 'none');}"
	return script

def createHtml(nr, table):
	html = open('plot.html', 'w')
	content = "<!DOCTYPE html>\n<HTML><HEAD>\n \
		<SCRIPT type=\"text/javascript\">"+getScript()+"</SCRIPT> \
	    	<H3>"+title+"</H3></HEAD>\n<BODY>"
	content +="<P>"+table+"</BR>"
	
	for i in range(1,nr):
    		content += "<img style=\"display:none;\" id=\"plot"+str(i)+"\" src=\""
		content += plotPrefix+str(i)+".jpeg\" alt=\"Plot "+str(i)+"\"/>\n"
	content += "</BODY></HTML>"
	html.write(content)
	#print content
	html.close()

def getPrefix():
	#make a new folder 
	datetime = time.strftime("%d%m%Y-%H%M%S")
	os.mkdir(os.getcwd().split("galaxy-dist")[0]+"galaxy-dist/static/plots/"+datetime)
	prefix = "/static/plots/"+datetime+"/plot"
	return prefix

def getColorSet():
	color = ['red', 'blue', 'green', 'yellow', 'pink', 'purple', 'grey', 'orange', 'indigo', 'fuchshia']
	return color

def oldMain():
	try:
		filename = sys.argv[1]
	except:
		print usage; sys.exit(1)

	# open stat-file from QUAST
	try:

		f = open(filename, 'r')
		#grab the headers
		title = f.readline();f.readline()
		stat = []; stat.append(f.readline())
		header = stat[0].split()
		plotPrefix = getPrefix()
		colorSet = getColorSet()
		nr = 1
		for word in f.readlines():#[3:max(enumerate(open(filename)))[0]+1]:
			stat.append(word)
			wordArray = word.split()
			while switch(word):
				if case('# contigs (>= 0 bp)'):
					makeStaticPlot(wordArray, 'Contigs (>= 0 bp)', 'Contigs larger than 0bp', nr)
					nr += 1
					break
				if case('# contigs (>= 1000 bp)'):
                                       	makeStaticPlot(wordArray, 'Contigs (>= 1000 bp)', 'Contigs larger than 1000bp', nr)
                                        nr += 1 
                                        break
				if case('Total length (>= 0 bp)'):
                                       	makeStaticPlot(wordArray, 'Total length (>= 0 bp)', 'Total length larger than 0bp', nr)
                                        nr += 1
                                        break
				if case('Total length (>= 1000 bp)'):
                                        makeStaticPlot(wordArray, 'Total length (>= 1000 bp)', 'Total length larger than 1000bp', nr)
                                        nr += 1
					break
				if case('# contigs'):
					makeStaticPlot(wordArray, 'Number of contigs', 'Total number of contigs', nr)
                                        nr += 1
                                        break
				if case('Total length'):
					makeStaticPlot(wordArray, 'Total length', 'Total length', nr)
                                        nr += 1
                                        break
				if case('Largest contig'):
                                        makeStaticPlot(wordArray, 'Largest contig', 'Largest contig', nr)
                                        nr += 1
                                        break
				if case('GC (%)'):
                                        makeStaticPlot(wordArray, 'GC%', 'GC %', nr)
                                        nr += 1
                                        break
				if case('N50'):
                                        makeStaticPlot(wordArray, 'N50', 'N50', nr)
                                        nr += 1
                                        break
				if case('N75'):
                                        makeStaticPlot(wordArray, 'N75', 'N75', nr)
                                        nr += 1
                                        break
				if case('L50'):
					makeStaticPlot(wordArray, 'L50', 'L50', nr)
                                        nr += 1
                                        break
				if case('L75'):
                                        makeStaticPlot(wordArray, 'L75', 'L75', nr)
                                        nr += 1
                                        break
				if case('# N\'s per 100 kbp'):
                                        makeStaticPlot(wordArray, 'N per 100kbp', 'Number of N\'s per 100 kbp', nr)
                                        nr += 1
                                        break
				break
		f.close()
		createHtml(nr, createTable(stat))
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise

#print "This is the file"
print assessOutput(open(sys.argv[1], 'r'), True)
