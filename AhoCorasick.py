def gotofunc(pat):
	newstate=0
	g={}
	d=[0 for i in range(20)]
	output=["" for i in range(20)]
	d[0]=0
	for i in range(0 ,len(pat)):
		state=0
		j=0
		
		p=list(pat[i])
		while (state,p[j]) in g:
			state=g[(state,p[j])]
			j+=1
		for k in range(j,len(p)):
			newstate+=1
			g[state,p[k]]=newstate
			d[newstate]=d[state]+1
			state=newstate
		output[state]='{},'.format(pat[i])	
	for a in  {'C','T','A','G'}:
		while not g[(0,a)] :
			g[(0,a)]=0
	
	return g,output ,d
			
def failfunc(g, output ):
	fail=[0 for t in range(20)]
	
	queue=[]
	for a in {'C','T','A','G'}:
		if (g[(0,a)]!=0):
			queue.append(g[(0,a)])
			fail[g[(0,a)]]=0
	while    queue:
		r = queue.pop(0)
		for a in {'C','T','A','G'}:
			if (r,a) in g:
				s=g[(r,a)]
				
				queue.append(s)
				state=fail[r]
				while not((state,a) in g):
					state=fail[state]
					
				fail[s]=g[(state,a)]
				output[s]= '{}{}'.format(output[s],output[fail[s]])
	return fail , output

pat=['GAATG','CTA','CCGT','AC','ATG','TGT'] 
s='CTAATGTTGAATGGCCACTACCGTGAATGCCGTGTGAATGCTA'
g ,output,d= gotofunc(pat) #calling goto function
fail, output=failfunc(g,output) #calling failure function
state=0
skip_count=0
paterns_found=","
print 'The goto function is:\n'
print(g)
print 'The failure function is:\n'
print(fail)
#Pattern Matching Machine Algorithm
for i in range(0,len(s)):		
	while not((state,s[i]) in g):
		
		state=fail[state]
		if (not state): skip_count+=1 #counting skips
	state=g[(state,s[i])]				
	if output[state]:
		paterns_found= '{}{}'.format(paterns_found,output[state]) 
		#print output[state]
		#print i
print '\nNumber of compares {}\n'.format(i)		
print '\nWe skip {} compares\n'.format(skip_count)
print 'Paterns found :{}'.format(paterns_found)
#counting instances of each patern
for j in range(0,6):
        c=0
        pat_count=0
        while paterns_found.find(',{},'.format(pat[j]),c)>-1:
                pat_count+=1
                c=paterns_found.find(',{},'.format(pat[j]),c)+len(pat[j])
        print '{} patern is found {} times \n'.format(pat[j],pat_count)


