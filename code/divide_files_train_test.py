import os
#str1='/home/jyoti/Desktop/training_data/'
print "Enter path of corpus with backslash at last and make sure in that folder only corpus files are there which are to be used"
str1=raw_input()
list_of_files=os.listdir(str1)
length=len(list_of_files)
k=0
total_count=0
print "enter name of train file"
#str2='/home/jyoti/Desktop/train.txt'
str2=raw_input()
write_file_train=open(str2,'w')
print "Enter name of test file"
str3=raw_input()
#str3='/home/jyoti/Desktop/test.txt'
print "Enter number of lines you want to keep in train file"
num_line=raw_input()
num_line=int(num_line)
write_file_test=open(str3,'w')
while(k<length):
	files=str1+list_of_files[k]
	File=open(files,'r')
	for line in File:
		total_count=total_count+1
		if total_count<num_line:
			write_file_train.write(line)
		else:
			write_file_test.write(line)
	File.close()
	k=k+1
print total_count
write_file_train.close()
write_file_test.close()
