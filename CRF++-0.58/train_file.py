import os
import codecs
file1='/home/jyoti/courses/Semester-7/CL-1/Assignment-2/tnt/train_hindi/'
list_of_files=os.listdir(file1)
length=len(list_of_files)
k=0
count=0
w_f=codecs.open('train_file_hindi','w',encoding="utf8")
while k< length:
	file_name=file1+list_of_files[k]
	read=codecs.open(file_name,'r',encoding="utf8")
	for line in read:
			if count <10000:
				w_f.write(line)
				count=count+1
	k=k+1
