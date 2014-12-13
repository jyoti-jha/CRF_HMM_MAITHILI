import sys
print "Enter file"
inp=raw_input()
File=open(inp,'r')
string="hin_001"
for line in File:
	    sys.stdout.write('hin_001 {l}'.format(l=line))

