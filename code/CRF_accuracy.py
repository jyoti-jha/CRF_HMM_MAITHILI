print "Enter test feature file"
files=raw_input()
#files='/home/jyoti/Desktop/features_made_on_test_data.txt'
File=open(files,'r')
correct=0
total=0
for line in File:
	print line
	total=total+1
	l=line.split('\t')
#	print l
	if(len(l)<11):
		continue
	actual_tag=l[9]
	predicted_tag=l[10].split('\n')
	predicted_tag=predicted_tag[0]
#	print actual_tag,predicted_tag
	if(actual_tag==predicted_tag):
		correct=correct+1
	else:
	 	print l[0],actual_tag,predicted_tag
accuracy=(correct*1.0/total*1.0)*100
print accuracy

