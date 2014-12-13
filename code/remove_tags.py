print "Enter the file name"
inp=raw_input()
file1=inp
File=open(file1,'r')
print "enter output file"
w=raw_input()
write_file=open(w,'w')
for line in File:
	l=line.split()
	strin=""
	for ele in l:
		p=ele.split('_')
		write_file.write(p[0])
		write_file.write(' ')
	write_file.write('\n')
File.close()
write_file.close()
