# CSE 101 - IP HW2
# K-Map Minimization 
# Name: DAKSH THAPAR
# Roll Number: 2018137
# Section:A
# Group:1
# Date:15/10/2018

from copy import *

'''bin_to_dec() takes a input in binary and converts it to decimal value, and stores in it a list
if the input contains a '_', the output is multiple terms by displaying all permutations when '_' is replaced by 0 or 1'''
def bin_to_dec(a):
	l=[]
	dec=0
	choice=[0,1]
	a=a[-1::-1] 
	
	if a.count('_')==3:						# case when there are 3 _ in input string, so it gives all 8 permutations (i.e. 2**3)
		ind1=a.find('_')
		ind2=a.find('_',ind1+1)
		ind3=a.find('_',ind2+1)

		for j in range(len(choice)):
			for k in range(len(choice)):
				for m in range(len(choice)):
		
					a=a[0:ind1]+str(choice[j])+a[ind1+1:]
					a=a[0:ind2]+str(choice[k])+a[ind2+1:]
					a=a[0:ind3]+str(choice[m])+a[ind3+1:]
					

					for i in range(len(a)):
						dec+=int(int(a[i])*(2**i))
					l.append(dec)
					dec=0
		dec=0
		return sorted(l)

	elif a.count('_')==2:				# case when there are 2 _ in input string, so it gives all 4 permutations (i.e. 2**2)
		ind1=a.find('_')
		ind2=a.find('_',ind1+1)

		for j in range(len(choice)):
			for k in range(len(choice)):

				a=a[0:ind1]+str(choice[j])+a[ind1+1:]
				a=a[0:ind2]+str(choice[k])+a[ind2+1:]

				for i in range(len(a)):
					dec+=int(int(a[i])*(2**i))
				l.append(dec)
				dec=0

		dec=0
		return sorted(l)

	elif a.count('_')==1:			# case when there are 1 _ in input string, so it gives all 2 permutations (i.e. 2**1)

		ind=a.index('_')
		for j in range(len(choice)):
			a=a[0:ind]+str(choice[j])+a[ind+1:]

			for i in range(len(a)):
				dec+=int(int(a[i])*(2**i))
			l.append(dec)
			dec=0
		return sorted(l)	
					
	elif a.count('_')==0: 			# case when there are no _ and hence simple conversion from binary to decimal
		for i in range(len(a)):
			dec+=int(int(a[i])*(2**i))
		l.append(dec)
		dec=0
		return sorted(l)

'''
groupify() is used here to distribute the minterms inputted in groups based on number of 1's in the minterms'''

def groupify(LIST_bin,LIST_dec,group_bin,group_dec):

	for i in range(len(LIST_bin)):
		if LIST_bin[i].count('1')==0:
			group_bin[0].append(LIST_bin[i])
			group_dec[0].append(LIST_dec[i])

		if LIST_bin[i].count('1')==1:
			group_bin[1].append(LIST_bin[i])
			group_dec[1].append(LIST_dec[i])
	
		if LIST_bin[i].count('1')==2:
			group_bin[2].append(LIST_bin[i])
			group_dec[2].append(LIST_dec[i])
	
		if LIST_bin[i].count('1')==3:
			group_bin[3].append(LIST_bin[i])
			group_dec[3].append(LIST_dec[i])
	
		if LIST_bin[i].count('1')==4:
			group_bin[4].append(LIST_bin[i])
			group_dec[4].append(LIST_dec[i])


'''
minimise() is used to obtain the prime implicants from our inputted minterms (lists containing minterms).
basically, a minterm belonging to a group (based on no. of 1's) is compared with the minterms of the following group, if there is only a single character, then they can be combined.
this process is carried out multiple times.
the minterms which dont combine with any other minterms of other groups are termed as prime implicants.'''

def minimise(group_bin,LIST_bin,numVar,PI_bin,PI_dec):

	temp_bin=[]
	single_bin=[]
	single_dec=[]
	list=[]
	
	for i in range(len(group_bin)):
		single_bin.append([])

	for i in range(len(group_bin)-1):
		for j in range(len(group_bin[i])):
			for k in range(len(group_bin[i+1])):
				count=0
				for x in range(numVar):
					if group_bin[i][j][x]==group_bin[i+1][k][x]:
						count+=1	
				if count==(numVar-1):
					temp_bin.append(group_bin[i][j])
					temp_bin.append(group_bin[i+1][k])
					for y in range(numVar):
						if group_bin[i][j][y]!=group_bin[i+1][k][y]:
							single_bin[i].append(group_bin[i][j][0:y]+'_'+group_bin[i][j][y+1:])
	p=deepcopy(single_bin)

	for i in range(len(single_bin)):
		for j in range(len(single_bin[i])):
			list.append(single_bin[i][j])
	q=deepcopy(list)

	for i in LIST_bin:
		if i not in temp_bin and i not in PI_bin:
			PI_bin.append(i)
			PI_dec.append(bin_to_dec(i))

	return p,q

'''
letter_for_PI assigns letters to literals of PI.
for eg- '001_' corresponds to 'w`x`y'''

def letter_for_PI(PI_bin,numVar):
	lPI=[]
	string=''
	letters='wxyz'

	for i in range(len(PI_bin)):
		for x in range(numVar):
			if PI_bin[i][x]!='_':

				if PI_bin[i][x]=='0':
					string+=(letters[x]+"\'")
				elif PI_bin[i][x]=='1':
					string+=letters[x]
		
		lPI.append(string)	
		string=''

	return lPI

'''
multiply() is used to perform  mathematical multiplication operation between two elements.
in this case, lists are used, and outputs are obtained in such a way that the ouputted lists correspond to the product of inputted terms'''

def multiply(A,B):
	temp=[]
	C=[]

	for i in range(len(A)):
		for j in range(len(B)):
			c=''
			s=A[i]+B[j]
			s=''.join(sorted(set(s), key=s.index))
			c+=s
			c=''.join(sorted(c))
			temp.append(c)

	for i in temp:
		if i not in C:
			C.append(i)
	return C 

'''
first, a prime implicant table is created consisting of various PIs, suing the concept of 2-D lists.
essential pi's (EPI's) are obtained from PI table (basically rows corresponding to those columns in PI Table where there is only a single 1)
petrick() uses above- defined functions to give a product of sum output, and then further simplication takes place using identities - X.X=X, X+X=X, X+XY=X.
a final list of PI that can be combined with EPI is obtained, and then EPI is appended to that list.
it is made sure that string is stored in lexicographic order and there are no duplicate terms.
stringOut is the final output obtained, which is basically the final terms (consisting of all EPI terms and some of the PI terms) separated by '+'.'''

def petrick(lPI,PI_dec,list_main_dec):
	d=lPI
	PI_Table=[]

	for i in range(len(d)):
		PI_Table.append([])

	for i in range(len(d)):
		for j in range(len(list_main_dec)):
			PI_Table[i].append(0)
	
	for i in range(len(d)):
		for j in range(len(list_main_dec)):
			for k in range(len(PI_dec[i])):
				if PI_dec[i][k]==list_main_dec[j]:
					PI_Table[i][j]=1
	
	EPI=[]
	NOT_EPI=[]
	for j in range(len(list_main_dec)):
		count=0
		for k in range(len(d)):
			
			if PI_Table[k][j]==1:
				count+=1
				y=k

		if count==1 and d[y] not in EPI:
			EPI.append(d[y]) 							#list consisting of essential PI's
	
	for i in d:
		if i not in EPI:
			NOT_EPI.append(i)							#list consisting of non-essential PI's

	NAME_list=[]
	NAME="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	for i in range(len(PI_Table)):
		NAME_list.append(NAME[i])						#basically to assign a 'letter' name to each row of PI table 
	
	POS_string=''
	POS=[]
	count=0

	for j in range(len(list_main_dec)):
		count=0
		POS_string=''
		for k in range(len(PI_Table)):
			
			if PI_Table[k][j]==1:
							
				POS_string+=NAME_list[k]+'+'

		POS_string=POS_string[:-1]
		realcount=0
		for w in range(len(POS)):
			if POS_string==POS[w]:
				realcount+=1
		if realcount==0:
			POS.append(POS_string)
	
	POS.sort(key=len)
	C=0
	for i in range(len(POS)):
		if len(POS[i])<=1:
			C+=1
	
	POS=POS[C:]
	POS.sort()
	
	POS_final=[]
	for i in range(len(POS)):
		POS_final.append([])

	for i in range(len(POS)):
		for j in range(len(POS[i])):
			if POS[i][j]!='+':
				POS_final[i].append(POS[i][j])

	LI_2=[]
	#LI_2=[]
	for i in range(len(POS_final)-1):
		LI_2.append('')

	for i in range(len(POS_final)-1):
		if i==0:
			LI_2[i]=multiply(POS_final[i],POS_final[i+1])
		else:
			LI_2[i]=multiply(LI_2[i-1],POS_final[i+1])

	if len(LI_2)>1:
		LI=LI_2[-1]
		LI=sorted(LI,key=len)										#final list of simplified PI is obtained (after applying all identities in multiplication operations) 
	else:
		LI=[]	
	
	Count=0

	for i in range(len(LI)-1):
		for j in range(i+1,len(LI)):
			Count=0
			for m in range(len(LI[i])):
				if LI[i][m] in LI[j]:
					Count+=1
			if Count==len(LI[i]):
				LI[j]='_______________________________'
	LI=sorted(LI,key=len)
	if len(LI)>0:													#the above list is sorted on the basis of length
		Ultimate_PI=LI[0]
	else:
		Ultimate_PI=[]
	out=[]

	for i in Ultimate_PI:
		out.append(i)
	OUTER=[]

	for i in out:
		OUTER.append(d[NAME_list.index(i)])							#OUTER is basically the 'LI' list and the various EPI's appended to that list
	stringOut=''
	
	OUTER.extend(EPI)
	OUTER=list(set(OUTER))
	OUTER=sorted(OUTER)
	
	for i in range(len(OUTER)):
		stringOut+=OUTER[i]+'+'										#elements are separated by '+'
	stringOut=stringOut[:-1]
	return stringOut												#final output string

def minFunc(numVar, stringIn):
	M=[]
	group_bin=[]
	group_dec=[]
	for i in range(5):
		M.append('')
		group_bin.append([])
		group_dec.append([])

	M[0]=[]
	M[1]=['0','1']
	M[2]=['00','01','10','11']
	M[3]=['000','001','010','011','100','101','110','111']
	M[4]=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

	list_main_dec=[]
	list_dcare_dec=[]
	LIST_dec=[]
	list_main_bin=[]
	list_dcare_bin=[]
	LIST_bin=[]

	index_d= stringIn.index('d')

	for i in range(index_d):
		if stringIn[i].isdigit() and stringIn[i+1].isdigit():
			list_main_dec.append(int(stringIn[i:i+2]))				

		elif i>0 and stringIn[i].isdigit() and not(stringIn[i-1].isdigit()):			
			list_main_dec.append(int(stringIn[i]))

	for i in range(index_d,len(stringIn)):
		if stringIn[i].isdigit() and stringIn[i+1].isdigit():
			list_dcare_dec.append(int(stringIn[i:i+2]))				
		elif i>index_d and stringIn[i].isdigit() and not(stringIn[i-1].isdigit()):			
			list_dcare_dec.append(int(stringIn[i]))
		elif stringIn[-1]=='-':
			list_dcare_dec=[]

	LIST_dec.extend(list_main_dec)
	LIST_dec.extend(list_dcare_dec)

	for i in range(len(list_main_dec)):
		list_main_bin.extend([M[numVar][list_main_dec[i]]])

	for i in range(len(list_dcare_dec)):
		list_dcare_bin.extend([M[numVar][list_dcare_dec[i]]])

	for i in range(len(LIST_dec)):
		LIST_bin.extend([M[numVar][LIST_dec[i]]])

	groupify(LIST_bin,LIST_dec,group_bin,group_dec)
	PI_dec=[]
	PI_bin=[]
	
	if (len(list_main_dec)+len(list_dcare_dec))==2**numVar:								#if all minterms are selected for a specific vaue of numVar (eg. 16 minterms for numVar=4), then '1' is outputted
		return '1'
	elif (len(list_main_dec))==0:														#if there are no main minterms inputted (all minterms minus dont care minterms), then '0' is ouputted 
		 return '0'

	else:
		y=minimise(group_bin,LIST_bin,numVar,PI_bin,PI_dec)								#otherwise minimise the minterms inputted, till we arrive with PIs, and perform petrick's method
		z=minimise(y[0],y[1],numVar,PI_bin,PI_dec)
		z1=minimise(z[0],z[1],numVar,PI_bin,PI_dec)
		minimise(z1[0],z1[1],numVar,PI_bin,PI_dec)
		stringOut=petrick(letter_for_PI(PI_bin,numVar),PI_dec,list_main_dec)
		return stringOut

