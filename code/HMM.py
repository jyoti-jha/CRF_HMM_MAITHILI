# usr/bin/python
# -*- coding: utf-8 -*-
import re
import string
import pprint
import operator
import unicodedata
import codecs
import math
import sys
d={}
words={}
tags={}
count=0
tmat={}
hello=0
ll=[]
print "Enter testing file"
file_names=raw_input()
q=[]
bigram={}
print "Enter Training File"
file_name=raw_input()
f=open(file_name)
bigram_tag=''
temptags={}
lines=0
transition_prob={}
mat=[]
path=[]
tp={}
tag_list=[]
final={}
dictionary_of_words_with_their_tags_count={}
def storing_words_and_tags_with_their_counts_in_a_list():
#	file_name=raw_input()
	f=open(file_name)
	lines=0
	print "hello"
	for line in f:
		lines=lines+1
		data = line
		p = re.split(r'(\s|\n )',data)
		for l in p:
			if l!='' and l!=' ' and l!='\n' and l!='\"':
				q=re.split('_',l)
				name_w = q[0]
				name_t = q[1]	
				if name_w!='hin' and name_w!='tel':
					try:
						dictionary_of_words_with_their_tags_count[l]=dictionary_of_words_with_their_tags_count[l] +1
					except:
						dictionary_of_words_with_their_tags_count[l]=1

				if name_w in words:
					if name_w!='hin' and name_w!='tel':
						words[name_w] = words[name_w]+1

				else:
					if name_w!='hin' and name_w!='tel':
						words[name_w]=1

				if name_t in tags:
					if name_w!='hin' and name_w!='tel' :
						tags[name_t] = tags[name_t]+1

				else:
					if name_w!='hin' and name_w!='tel':
						tags[name_t]=1
	tags["<start>"]=lines
#	print"hello..................................................................."
	
#	for key,value in tags.iteritems():
#		print key , value

#	for key,value in words.iteritems():
#		print key,value
def emission_probability():
	print "in emission"
	emission={}
	for ele,val in words.items():
		emission[ele]={}
	for current_word,val in words.items():
			temp=emission[current_word]
			for current_tag,val1 in tags.items():
				key=current_word+'_'+current_tag
				try:
					numerator=dictionary_of_words_with_their_tags_count[key] + 0.5*1.0
				except:
					numerator=0+0.5*1.0
				denominator=tags[current_tag]+0.5*10000
				prob=(1.0*numerator)/denominator
				p=''.join(current_word)
				#print p,current_tag,numerator,denominator,prob
				temp[current_tag]=prob
	#print emission["ఈ"]["DEM"]
	return emission


def transition_matrix():
        print "in transition"
        f=open(file_name)
        bigram_tag=''
        for line in f:
                data = line
                p = re.split(r'(\s|\n )',data)
                prev="<start>"
                for l in p:
                    if l!='' and l!=' ' and l!='\n' and l!='\"':
                        
                                q=re.split('_',l)
                            #	print q
                                name_w = q[0]
                                name_t = q[1]
                                if name_w!='tel' and name_w!='hin':
                                    cur=q[1]
                                else:
                                    	cur = "<start>"
                                        prev = "</start>"
                                
                                bigram_tag = prev+' '+cur
                                if bigram_tag in bigram and bigram_tag!='':
                                    bigram[bigram_tag]= bigram[bigram_tag]+1
                                else:
                                    bigram[bigram_tag]=1
                                
                                prev = cur
        
        
        
        #	count=0
	#tp={}
	temp={}
        for key,value in tags.iteritems():
            temptags[key]=value
	    tag_list.append(key)
	    tp[key]={}
        tag=''
        for key in tags.keys():
	    #ll.append(key)
            for k in temptags.keys():
                #print key , k
                    tag=key+' '+k
                    if tag in bigram:
                        n = bigram[tag]
                    else:
		    	n = 0
                    d = tags[key]
                    transition_prob[tag] = (n*1.0)/d
		    temp[k]=(n*1.0)+0.5/d+((0.5)*10000)
		    tp[key][k]=temp[k]
#	print "dkjfhk;wdjfhds\n\n\n"
#	print dic["DEM"]["NN"]
def viterbi():
	tag_count=0
	for key in tags.keys():
		tag_count=tag_count+1
#	file_names=raw_input()
	f=open(file_names)
	
	i=0
		
	for line in f:
                print line
		v = [{}]  # final viterbi matrix
		path={} 
		data=line	
		p= data.split(' ')
		tag1=''
#		ll=[]
		for i in range(2,len(p)-1):
			#print i , p[i]
			#if p[i]!=' ' and p[i]!='.' and p[i]!='\"' and p[i]!=',':
			ll.append(p[i])
		for y in tag_list:
			#print key
			tag1="<start>"+' '+y
#			print ll[0]
			try:
				v[0][y] = (tp["<start>"][y])*emission[ll[0]][y]
				path[y] = [y]
			except:
				v[0][y]=(tp["<start>"][y])*0.5
				path[y]=[y]
		
			
		for t in range(1 , len(ll)):
			v.append({})
			newpath = {}
	
			for y in tag_list:
			#	print emission["సమయాలలోనూ"][y]
				if ll[t] not in emission:
					emission_prob = 0.5
#					prob=0
				else:
					emission_prob=emission[ll[t]][y]
				
				(prob , state) = max((v[t-1][y0]* (tp[y0][y])*emission_prob,y0) for y0 in tag_list)
				#else:
				#	continue
				v[t][y]=prob
				newpath[y] = path[state] + [y]
			path = newpath
			n=0
			if len(ll)!=1:
				n=t
			(prob ,state) = max((v[n][y],y) for y in tag_list)
			if prob!=0 and ll[t]!='.' and ll[t]!='\'':
				#print ll[t]
				#print (prob,state)
				if ll[t] not in final:
					final[ll[t]]=state
	#	return(prob , path[state])


def write():
        print "in write"
	f = open(file_names)
	f2 = open("Hindi.out",'w')
	for line in f:
		h=0
		data=line
		p=data.split(' ')
		for i in p:
#			print i
			#print "gadha",i
			gadha = '\"'+'\n'
			h=h+1
			if i=="hin_001":
				continue
			if h==1:
				f2.write(i+' ')
				print i+' ',

			if i in final:
				f2.write(i+'_'+final[i]+' ')
				print i+'_'+final[i]+' ',
			elif i=='\n':
				f2.write(i)
				print i,
			elif i=='.' or i==',' or i=='"':
				f2.write(i+' ')
				print i+' ',
			else:
				if h!=1 and i!='\n' and i!='' and i!=gadha:
					f2.write(i+'_UNK ')
					print i+'_UNK',
		f2.write('\n')
		print 
				


	
				
		



storing_words_and_tags_with_their_counts_in_a_list()
emission=emission_probability()
transition_matrix()
viterbi()
write()
#for key,value in transition_prob.iteritems():
#	print key,value
#print emission

