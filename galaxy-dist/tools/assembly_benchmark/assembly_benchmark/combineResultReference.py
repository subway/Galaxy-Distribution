#!/usr/bin/python
import sys, os, json, time
from pyPdf import PdfFileWriter, PdfFileReader

def getLongestDelimiter(inputFile, header):
    delimiter = 0
    for line in inputFile:
        for k in element:
            if line.startswith(k.strip()):
                content = line.split(k.strip())[-1].strip()
                if delimiter < len(content):
                    delimiter = len(content)
                break
            if delimiter < len(header):
		delimiter = len(header)
    return delimiter+4


def combinePlotsPdf():
    output = PdfFileWriter()
    input1 = PdfFileReader(file(path1+'/plots.pdf', "rb"))
    input2 = PdfFileReader(file(path2+'/plots.pdf', "rb"))

    for page in range(0, input1.getNumPages()):
        output.addPage(input1.getPage(page))
    for page in range(0, input2.getNumPages()):
        output.addPage(input2.getPage(page))
    outputStream = file(path3+'/tmp.pdf', 'wb')
    output.write(outputStream)
    outputStream.close()
    #Change name of pdf file
    os.system('mv '+path3+'/tmp.pdf '+path3+'/plots.pdf')

def combineReportTxtTsv(header):
    txt = open(path3+'/tmp.txt','w') #txt file
    tsv = open(path3+'/tmp.tsv','w') #tsv file
    input1 = open(path1+'/report.txt','r').readlines()
    input2 = open(path2+'/report.txt','r').readlines()
	
    #Add headings
    txt.write(''.join(input1[0:2]))
    tsv.write(''.join(input1[0:2]))
    delimiter = ''
    longestDel = 0
    if not header:
        longestDel = getLongestDelimiter(input1, path1.split('/')[-1])
        for i in range(longestDel-len(path1.split('/')[-1])): delimiter += ' '
        txt.write('Assembly                     '+path1.split('/')[-1]+delimiter+path2.split('/')[-1]+'\n')
        tsv.write('Assembly\t'+path1.split('/')[-1]+'\t'+path2.split('/')[-1]+'\n')
    else:
        longestDel = getLongestDelimiter(input1, input1[2].split('Assembly')[-1].strip())
        for i in range(longestDel-len(input1[2].split('Assembly')[-1].strip())): delimiter += ' '
        txt.write('Assembly                     '+input1[2].split('Assembly')[-1].strip()+delimiter+path2.split('/')[-1]+'\n')
        header1 = ' '.join(input1[2].split('Assembly')[-1].strip().split()).replace(' ','\t')
        header2 = path2.split('/')[-1]
        tsv.write('Assembly\t'+header1+'\t'+header2+'\n')
    #Merge content
    for e in element:
        xInput = '-'
        yInput = '-'
        for x in input1:
            if x.startswith(e.strip()+'  '):
                xInput = x.split(e.strip())[-1].strip()
                break
        for y in input2:
            if y.startswith(e.strip()+'  '):
                yInput = y.split(e.strip())[-1].strip()
                break
	
        if (xInput == '-') & (yInput == '-'):
            break
        else:
            delimiter = ''
            for i in range(longestDel-len(xInput)):
                delimiter += ' '
            txt.write(e+xInput+delimiter+yInput+'\n')
            xInput = ' '.join(xInput.split()).replace(' ','\t')
            xInput = xInput.replace('\t+\t',' + ').replace('\tpart',' part')
            tsv.write(e.strip()+'\t'+xInput+'\t'+yInput+'\n')
	
    #Close files and change change name
    txt.close()
    tsv.close()
    os.system('mv '+path3+'/tmp.txt '+path3+'/report.txt')
    os.system('mv '+path3+'/tmp.tsv '+path3+'/report.tsv')

def combineTransposedReportTxtTsv():
    #Tranposition
    transpose = []
    txt = open(path3+'/transposed_report.txt','w')
    tsv = open(path3+'/transposed_report.tsv','w')
    input1 = open(path3+'/report.txt','r').readlines()
    txt.write(''.join(input1[0:2]))
    tsv.write(''.join(input1[0:2]))
    element.append('Assembly    ')
    space = []
    for line in input1:
        for e in element:
            if line.startswith(e.strip()+'  '):
                content = line.split(e.strip())
                tmp = []
                delimiter = len(e.strip())
                tmp.append(e.strip())
                if ' part' in line:
                    content = content[-1].split('part')
                    for cont in content:
                        for c in cont.split('-'):
                            c = c.strip()
                            if c != '':
                                tmp.append(c+' part')
                                if delimiter < (len(c)+5):
                                    delimiter = len(c)+5
                            else:
                                tmp.append('-')
                                if delimiter < len(c):
                                    delimiter = len(c)
                else:
                    content = content[-1].strip().split()
                    for c in content:
                        tmp.append(c)
                        if delimiter < len(c):
                            delimiter = len(c)
                space.append(delimiter)
                transpose.append(tmp)
                break	
    transpose = zip(*transpose)
    for x in transpose:
        delimiter = '  '
        for y in range(len(x)):
            delimiter = '  '
            for s in range(space[y]-len(x[y])):
                delimiter += ' '
            txt.write(x[y]+delimiter)
            tsv.write(x[y]+'\t')
        txt.write('\n')
        tsv.write('\n')
    txt.close()
    tsv.close()

def mergeJsonFile(jsonpath1, jsonpath2, jsonpath3, header, col1, col2):
    #Get list of json files
    jsonList = []
    f = open(path3+'/jsonlist.txt', 'w')
    #Get new json files from path1
    for p in [d for d in sorted(os.listdir(jsonpath1), key=str.lower) if os.path.isfile(jsonpath1+'/'+d)]:
        if not p in jsonList:
            jsonList.append(p)
    #Get new json files from path2
    for p in [d for d in sorted(os.listdir(jsonpath2), key=str.lower) if os.path.isfile(jsonpath2+'/'+d)]:
        if not p in jsonList:
            jsonList.append(p)
    for j in jsonList:
        #if both folder have the file, merge
        if ((j in os.listdir(jsonpath1)) & (j in os.listdir(jsonpath2))):
            #merge file
            file1 = json.load(open(jsonpath1+'/'+j))
            file2 = json.load(open(jsonpath2+'/'+j))
            file3 = {}
            content = []
            for key in file1.keys():
                if j != 'report.json':
                    if key == 'list_of_GC_distributions':
                        content.append(file1[key])
                        for f2 in range(1,len(file2[key][0])):
                            content[0][0].append(file2[key][0][f2])
                        file3[key] = content
                    elif key == 'lists_of_gc_info':
                        if ((file1[key] != None) & (file2[key] != None)):
                            content.append(file1[key])
                            content.append(file2[key])
                            file3[key] = content
                        else:
                            file3[key] = None
                    elif key == 'reflen':
                        content.append(file1[key])
                        file3[key] = [file1[key],file2[key]]
                    elif key != 'filenames':
                        content = file1[key]
                        for f2 in range(len(file2[key])):
                            content.append(file2[key][f2])
                        file3[key] = content
                    else:
                        file3[key] = header
                else:
                    #Report file:
                    if key == 'date':
                        file3[key] = time.strftime("%d %B %Y, %A, %H:%M:%S")
                    elif key == 'minContig':
                        file3[key] = file1[key]
                    elif key == 'assembliesNames':
                        file3[key] = header
                    else: #The key is 'report'
                        report1 = file1[key]
                        report2 = file2[key]
                        content = [['',[]],
                                   ['',[]],
                                   ['',[]],
                                   ['',[]],
                                   ['',[]],
                                   ['',[]],
                                   ['',[]]]

                        for x in range(len(content)):
                            content[x][0] = report1[x][0]
                            content[x][1] = {}
                            iterator = []
                            if len(report1[x][1]) >= len(report2[x][1]):
                                iterator = report1[x][1]
                            else:
                                iterator = report2[x][1]
                            for y in iterator:                                
                                rTmp1 = []
                                rTmp2 = []
                                for r in report1[x][1]:
                                    if y['metricName'] == r['metricName']:
                                        rTmp = r['values']
                                        break
                                for r in report2[x][1]:
                                    if y['metricName'] == r['metricName']:
                                        rTmp2 = r['values']
                                        break
                                if ((rTmp1 != []) | (rTmp2 != [])):
                                    content[x][1]['values'] = []
                                    content[x][1]['quality'] = y['quality']
                                    content[x][1]['isMain'] = y['isMain']
                                    content[x][1]['metricName'] = y['metricName']  
                                if ((rTmp1 != []) & (rTmp2 != [])):
                                    for val in rTmp:
                                        content[x][1]['values'].append(val)
                                    for val in rTmp2:
                                        content[x][1]['values'].append(val)
                                elif rTmp1 != []:
                                    content[x][1]['values'] = rTmp1
                                    for val in range(col2):
                                        content[x][1]['values'].append("")
                                elif rTmp2 != []:
                                    for val in range(col1):
                                        content[x][1]['values'].append("")
                                    for val in rTmp2:
                                        content[x][1]['values'].append(val)
                        file3[key] = content

            with open(jsonpath3+'/'+j, 'w') as outfile:
                json.dump(file3, outfile)
        #else copy file to new folder in jsonpath3
        elif j in os.listdir(jsonpath1):
            os.system('cp '+jsonpath1+'/'+j+' '+jsonpath3)
        else:
            os.system('cp '+jsonpath2+'/'+j+' '+jsonpath3)
        f.write(j+'\n')
    f.close()    


def combineHTML():
    
def combine(inPath1, inPath2, inPath3, inHeader):
    global path1; path1 = inPath1
    global path2; path2 = inPath2
    global path3; path3 = inPath3
    header = inHeader

    global element; element = ['# contigs (>= 0 bp)          ',
		   '# contigs (>= 1000 bp)       ',
		   'Total length (>= 0 bp)       ',
		   'Total length (>= 1000 bp)    ',
		   '# contigs                    ',
		   'Total length                 ',
		   'Largest contig               ',
		   'Reference length             ',
		   'GC (%)                       ',
		   'Reference GC (%)             ',
		   'N50                          ',
		   'NG50                         ',
		   'N75                          ',
		   'NG75                         ',
		   'L50                          ',
		   'LG50                         ',
		   'L75                          ',
		   'LG75                         ',
		   '# misassemblies              ',
		   'Misassembled contigs length  ',
		   '# local misassemblies        ',
		   '# unaligned contigs          ',
		   'Unaligned contigs length     ',
		   'Genome fraction (%)          ',
		   'Duplication ratio            ',
		   '# N\'s per 100 kbp            ',
		   '# mismatches per 100 kbp     ',
		   '# indels per 100 kbp         ',
		   '# genes                      ',
		   'Largest alignment            ',
		   'NA50                         ',
		   'NGA50                        ',
		   'NA75                         ',
                   'NGA75                        ',
		   'LA50                         ',
		   'LGA50                        ',
		   'LA75                         ',
		   'LGA75                        '
		   ]
    #Combine all plots.pdf files
    #combinePlotsPdf()

    #Combine report txt/tsv
    #combineReportTxtTsv(header)

    #Combine transposed_report txt/tsv
    #combineTransposedReportTxtTsv()
    #Merge jsonfiles
    mergeJsonFile(path1+'/json',path2+'/json',path3+'/json', open(path3+'/report.tsv').readlines()[2].strip().split('\t')[1:], 1, 1)
             
#Main()
combine('/usit/invitro/data/galaxy/master/sabbai/galaxy-dist/database/files/001/dataset_1387_files/A_hydrophila_ATCC_7966',
        '/usit/invitro/data/galaxy/master/sabbai/galaxy-dist/database/files/001/dataset_1387_files/B_cereus_ATCC_1098',
        '/usit/invitro/data/galaxy/master/sabbai/galaxy-dist/database/files/001/dataset_1387_files/combined_reference',
        False)
