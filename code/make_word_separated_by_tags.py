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
		l=line.split()
		for i in l:
			p=i.split('_')
			write_file.write(p[0])
			write_file.write(' ')
			write_file.write(p[1])
			write_file.write('\n')
print num	
