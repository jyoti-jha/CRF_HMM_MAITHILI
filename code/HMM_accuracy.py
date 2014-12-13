print "enter correct tagged file"
inp=raw_input()
file1=open(inp,'r')
#file1=open('/home/jyoti/courses/Semester-7/NLP/PROJECT/data/train_test/correct_tagged_test','r')
file2=open('/home/jyoti/courses/Semester-7/NLP/PROJECT/code/Hindi.out','r')
predicted_tag=[]
actual_tag=[]
for line in file1:
	l=line.split()
	count=0
	print l
	for ele in l:
#		if count==0:
#			count=1
#			continue
		p=ele.split('_')
		if len(p)==1:
			continue
		else:
#			print p[1]
			actual_tag.append(p[1])
print actual_tag
for line in file2:
	l=line.split()
	print l
	count=0
	if len(l)==0:
		continue
	for ele in l:
#		if count==0:
#			count=1
#			continue
		p=ele.split('_')
		if len(p)==1:
			continue
		else:
			predicted_tag.append(p[1])			
correct=0
print len(actual_tag)
print len(predicted_tag)
for ele in range(0,len(actual_tag)):
	if actual_tag[ele]==predicted_tag[ele]:
		correct=correct+1
	
accuracy=correct*1.0/len(actual_tag)
print accuracy
file1.close()
file2.close()

