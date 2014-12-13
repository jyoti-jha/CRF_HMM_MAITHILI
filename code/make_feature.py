import codecs
print "Enter input file"
files=raw_input()
#files='/home/jyoti/Desktop/CRF++-0.58/train_file_english'
print "Enter output file"
write_file_name=raw_input()
#write_file_name='/home/jyoti/Desktop/train_file_english_cl1.txt'
write_file=codecs.open(write_file_name,'w',encoding="utf8")
File=codecs.open(files,'r',encoding="utf8")
flag=0
num=0
for line in File:
		print line
#	if line=="</Sentence>\n":
#		flag=0
#		continue
#	if line=="<Sentence id=''''>\n":
#		flag=1
#		continue
#	if flag==1:
		num=num+1
		l=line.split()
		string=l[0]
		length=len(string)
                if len(l) <=1:
		 	continue
		if len(string)>=8:
			write_file.write(l[0])
			write_file.write('\t')
			write_file.write(string[0])
			write_file.write('\t')
			write_file.write(string[0:2])
			write_file.write('\t')
			write_file.write(string[0:3])
			write_file.write('\t')
			write_file.write(string[0:4])
			write_file.write('\t')
			write_file.write(string[(length-4):length])
			write_file.write('\t')
			write_file.write(string[(length-3):length])
			write_file.write('\t')
			write_file.write(string[(length-2):length])
			write_file.write('\t')
			write_file.write(string[(length-1):length])
			write_file.write('\t')
			write_file.write(l[1])
			write_file.write('\n')
		
		elif len(string)==4:
			write_file.write(l[0])
			write_file.write('\t')
			write_file.write(string[0])
			write_file.write('\t')
			write_file.write(string[0:2])
			write_file.write('\t')
			write_file.write(string[0:3])
			write_file.write('\t')
			write_file.write(string[0:4])
			write_file.write('\t')
			write_file.write(string[0:4])
			write_file.write('\t')
			write_file.write(string[0:4])
			write_file.write('\t')
			write_file.write(string[0:4])
			write_file.write('\t')
			write_file.write(string[0:4])
			write_file.write('\t')
			write_file.write(l[1])
			write_file.write('\n')
		elif len(string)<4:
			write_file.write(l[0])
			write_file.write('\t')
			count=0
			for i in range(0,8):
				if(count>=1):
					write_file.write('\t')
				if(i==length):
					left=8-count
					break
				else:
					write_file.write(string[0:i+1])
					count=count+1
			if(left!=0):
				for i in (range(0,left-1)):
			  		write_file.write(l[0])
			  		write_file.write('\t')
			 	write_file.write(l[0])
				write_file.write('\t')
				write_file.write(l[1])
			 	write_file.write('\n')
		elif len(string)>4:
			print string
		   	write_file.write(l[0])
			write_file.write('\t')
			for i in range(0,4):
				write_file.write(string[0:i+1])
				write_file.write('\t')
			start=length-3
			for i in range(start,length):
				write_file.write(string[i-1:length])
				write_file.write('\t')
			write_file.write(string[length-1:length])
			write_file.write('\t')
			write_file.write(l[1])
			write_file.write('\n')
print num	
