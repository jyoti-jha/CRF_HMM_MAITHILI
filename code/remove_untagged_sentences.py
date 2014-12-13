print "Enter corpus"
file1=raw_input()
File= open(file1,'r')
print "Enter name of output file"
inp=raw_input()
w=open(inp,'w')
for line in File:
	flag=0
	l=line.split()
	for i in l:
		p=i.split('_')
		if p[1]=='':
			print line
			flag=1
			break
	if flag==0:
		w.write(line)
File.close()
w.close()
