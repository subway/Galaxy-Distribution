#!/usr/bin/python
from matplotlib.mlab import PCA

data = [['speed',{1,2,3}],['test',{2,3,4}],['plotdata',{3,4,5}],['last',{6,7,8}]]
PCA(data)

exit(0)

input = ['not','tall 1','tall2']
header = ['not', 'title1', 'title2']
x = []
y = []
r = range(10,100,10)
print "r - ",r
r = range(100,10,-10)
print "r2 - ",r
for i in range(1,3,-1):
	print i
	x.append(input[i])
	y.append(header[i])
print input
print header
print x
print y

print range(1,10)

line = "\"abc, abc, "
line = line[0:len(line)-2]+"\""
print line
testlist = [1,2,4,5,1,3,42,33]
for i in [i for i,x in enumerate(testlist) if x == 1]:
	print i

print [i for i,x in enumerate(testlist) if x == 1][0]
