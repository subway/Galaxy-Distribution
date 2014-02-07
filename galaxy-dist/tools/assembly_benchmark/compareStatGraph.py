#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import os, sys, time, numpy as np, matplotlib.pyplot as plt, json
from pprint import pprint
from matplotlib.mlab import PCA

# validate input
#usage = 'Usage: %s path to QUAST report.txt file' % sys.argv[0]
#global stat, title, header, plotPrefix, colorSet

#x = [[92036,33710,60973],[156,241,196],[21,30,0]]
x = [[92036,156,21],[33710,241,30],[60973,196,0]]
#x = [[0,8],[8,9],[12,11],[20,12]]
#y = [[0,8,12,20],[8,9,11,12],[0,8,12,20],[8,9,11,12]]
dataMatrix = np.array(x)
print dataMatrix
myPCA = PCA(dataMatrix)
print "\na - centered unit sigma version of input a"
print myPCA.a
print "\nmu - a numdims array of means of a"
print myPCA.mu
print "\nsigma - a numdims array of atandard deviation of a"
print myPCA.sigma
print "\nfracs - the proportion of variance of each of the principal components"
print myPCA.fracs
print "\nWt - the weight vector for projecting a numdims point or array into PCA space"
print myPCA.Wt
print "\nY - a projected into PCA space"
print myPCA.Y


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

def makeScatterPlot(path, header, xval, yval, xlabel, ylabel, plotTitle):
	tmp = plt.scatter(xval, yval)
	plt.axis([0, max(xval)+5, 0, max(yval)+5])
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(plotTitle)
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

def assessOutput(quastfile, ref, path):
	#Assemblies
	assembly = {}
	basicAsm = {}
	misassembliesAsm = {}
	unalignedAsm = {}
	mismatchAsm = {}
	geneAsm = {}
	#remove first two line
	#quastfile.readline();quastfile.readline()
	with open(quastfile) as data_file:
		data = json.load(data_file)
		label = data['assembliesNames']
		report = data['report']
		pprint(data)
	#label = quastfile.readline().split()
	#label.pop(0)
	for l in label:
		assembly[l] = 0
		basicAsm[l] = 0
		misassembliesAsm[l] = 0
		unalignedAsm[l] = 0
		mismatchAsm[l] = 0
		geneAsm[l] = 0	
	
	topnumber = len(label) if len(label) < 3 else 3
	result = "Rank 1 - 3p, Rank 2 - 2p, Rank 3 - 1p"
	ddl = []
	for line in report:
		title = line[0]
		for field in line[1]:
			ddl.append(field['metricName']) 
			if field['metricName'] != '# genes':
				values = [float(x) for x in field['values']]
				if field['quality'] == 'Less is better':
					basicAsm = getBottomThree(basicAsm, values, topnumber, label)
					assembly = getBottomThree(assembly, values, topnumber, label)
				elif field['quality'] == 'More is better':
					basicAsm = getTopThree(basicAsm, values, topnumber, label)
					assembly = getTopThree(assembly, values, topnumber, label)
				else:
					for l in label:
						basicAsm[l] += 1
						assembly[l] += 1
		result = addTopResult(basicAsm, result, '\n'+title+'\t')
		for l in label:
			basicAsm[l] = 0;
	result = addTopResult(assembly, result, '\nOverall\t')
	result += createddl(ddl, path)
	return result
def makePlot(path):
	header = 'A B C D E F'
	header = header.split(' ')
	x = [10, 5, 20, 30, 40,]
	
	y = [1.0, 4.5, 6, 7, 25]
	
	makeStaticPlot(path, header, x, 'Ylabel', 'Test plot')
def createddl(option, path):
	ddl = '<select name="ddl1">'
	ddl += '  <option value="def">--- Select ---</option>'
	ddl2 = '<select name="ddl2">'
        ddl2 += '  <option value="def">--- Select ---</option>'
	ddl3 = '<select name="ddl3">'
        ddl3 += '  <option value="def">--- Select ---</option>'
	for opt in option:
		ddl += '  <option value="'+opt+'">'+opt+'</option>'
		ddl2 += '  <option value="'+opt+'">'+opt+'</option>'
		ddl3 += '  <option value="'+opt+'">'+opt+'</option>'
	ddl += '</select>'
	ddl2 += '</select>'
	ddl3 += '</select>'
	ddl2 += ddl3
	ddl += '<button name="btn1" type="button" onClick="javascript:createBarPlot();">Create plot</button>'
	ddl += '\t<a href="latestBARplot.jpeg" target="_blank">Latest barplot here</a><br>'
	ddl2 += '<button name="btn2" type="button" onClick="javascript:createScatterPlot();">Create plot</button>'
	ddl2 += '\t<a href="latestXYplot.jpeg" target="_blank">Latest scatterplot here</a>'
	ddl += ddl2
	return ddl
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
	#function toggleImg(id){ \n \
	#var img = document.getElementById(id);\n \
	#img.style.display = (img.style.display=='none' ? 'block' : 'none');}\n \
	
	script = '<SCRIPT type="text/javascript">\n \
	function createBarPlot(){\n \
	   window.open(\'latestBARplot.jpeg\', \'blank\').focus();}\n \
	</SCRIPT>\n<SCRIPT type="text/javascript">\n \
	function createScatterPlot(){\n \
	   window.open(\'latestXYplot.jpeg\', \'blank\').focus();}\n \
	</SCRIPT>'
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
#print assessOutput(open(sys.argv[1], 'r'), True)
