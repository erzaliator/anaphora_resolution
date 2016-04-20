#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os


fi=open((os.path.join('Section_11', 'fullnews_id_2578406_date_7_7_2004.utf8.cml.V.tkn.cml_updated.mo.pos.chnk.prun.posn')),'r')
l =fi.readlines()

index=['579..585','552..578','586..652']
string=''
for i in l:
	print i
	string+=i
fi.close()

print string[575:587]
print string[548:578]
print string[581:658]
print string[579:]
fo=open((os.path.join('../my_ann/Section_11', 'fullnews_id_2578406_date_7_7_2004.utf8.cml.V.tkn.cml_updated.mo.pos.chnk.prun.posn')),'r')
m=fo.readlines()
for line in m:
	line=line[:-1]
	line=line.split('|')
	# print line[1],line[14],line[20]
	# print line
	indexes=line[1]
	if(indexes):		#Explicit
		print indexes,line
	else:				#Implicit
		print "imp",indexes,line
		print dm
fo.close()