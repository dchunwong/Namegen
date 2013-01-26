import random
import time
vowel=['a','e','i','o','u']
capvow=list('AEIOUY')
consonant=list('bcdfghjklmnprstvxyz')
capcon=list('BCDFGHJKLMNPRSTVWXYZ')
specialbeg=['tr','th','st','ph', 'nt', 'ch', 'qu', 'sh', 'nn']
specialend=['th','st','ph', 'nt', 'ch', 'sh']
capspec=['Tr', 'Th', 'St', 'Ph', 'Ch', 'Qu', 'Sh' ]
genders={'Male': 'M', 'male':'M', 'Female': 'F', 'F':'F', 'M':'M', 'female': 'f', 'm':'M', 'f':'F'}
commentary=1
def name():
	while True:
		length=input('HOW LONG IS YOUR NAME?  ')
		try:
			length=int(length)
		except ValueError:
			print('\nTHATS NOT A NUMBER PLEBIAN!\n')
			continue
		if length>13: #Names began losing pronouncability around 11 characters.
			print('\nTHE GODS ARE ANGERED BY SUCH A LONG NAME (Shorter than 13 please.)\n') 
			continue
		if length<2: #One letter names are so out of style.
			print('\nTHE GODS ARE ANGERED BY SUCH A SHORT NAME (Greater than 1 please.)\n')
			continue
		else:
			return length
def gen():
	while True:
		gen=input('\nWHAT GENDER DO YE IDENTIFY WITH? (M/F)  ')
		if gen in genders:
			return genders[gen]
		else:
			print("\nAYE THAT'S NOT ANYTHING I'VE HEARD OF!\n")
def make_name(n, g):
	if n>2:
		lettype=random.choice([capvow, capcon, capspec]) #Determines whether beginning is a vowel or consonant.
	else:
		lettype=random.choice([capvow, capcon])
	coolcoolcool=['', '']
	while (len(list(''.join(coolcoolcool))))<n: #Is the current list of letters longer than the desired length?
		if coolcoolcool[-1]=='y': #Ensures that 'y' is not repeated twice.
			letter=random.choice(list(filter(lambda x: x!='y', lettype)))
		if coolcoolcool[-1]=='Qu' or coolcoolcool[-1]=='qu': 
			letter=random.choice(list(filter(lambda x: x!='u', lettype)))
		else:	
			letter=random.choice(lettype)
		coolcoolcool.append(letter)
		if lettype==vowel or lettype==capvow:
			if len(coolcoolcool)>4:
				lettype=random.choice([consonant, specialbeg])
			else:
				lettype=consonant
		else:
			lettype=vowel
		if len(list(''.join(coolcoolcool)))+2==n:
			if lettype==vowel:
				if g=='M':
					coolcoolcool.append('io')
				if g=='F':
					coolcoolcool.append(random.choice(['ia', 'ie']))
			if lettype==specialbeg:
				coolcoolcool.append(random.choice(specialend))

		if (len(list(''.join(coolcoolcool))))+1==n and lettype==vowel:
			if g=='F':
				coolcoolcool.append(random.choice(list(filter(lambda x: x!='o', lettype))))
			if g=='M':
				coolcoolcool.append(random.choice(list(filter(lambda x: x!='a', lettype))))
	name =''.join(coolcoolcool)
	return name
def make_face(g):
	hat1= lambda: print('\t                  ________\n\t              {__/        \__}\n\t                |__________|')
	hat2= lambda: print('\t                ____________\n\t                |==========|\n \t              __|__________|__')
	hat3= lambda: print('\t                  ________\n\t                 /        \ \n\t                |__________|')
	hat4= lambda: print('\t                  ________\n\t                 /        \ \n\t             \__|==========|__/ ')
	hat5= lambda: print('\n\t                ||||||||||||\n \t                ||||||||||||')
	hat6= lambda: print('\t                ____________\n\t                |          |\n \t                |          |')
	hat7= lambda: print('\n\t                |VVVVVVVVVV|\n \t                |VVVVVVVVVV|')
	bangs1= lambda: print('\t                |          |')
	bangs2= lambda: print('\t                |------^---|')
	bangs3= lambda: print('\t                |VVVVVVVVVV|')
	bangs4= lambda: print('\t                |^^^^^VVVVV|')
	bangs5= lambda: print('\t                |^-^-^-^-^-|')
	eye1= lambda: print('\t                |  |    |  |\n\t                |  |    |  |')
	eye2= lambda: print('\t                |=[|]==[|]=|\n\t                |          |')
	eye3= lambda: print('\t                |  = o  =  |\n\t                |          |')
	eye4= lambda: print('\t                |  _    _  |\n\t                |  |    |  |')
	eye5= lambda: print('\t                |  \    /  |\n\t                |  |    |  |')
	mouth1= lambda: print('\t                |   ----   |\n\t                |__________|')
	mouth2= lambda: print('\t                |  ======  |\n\t               ',random.choice(['|_{|____|}_|', ' \{|____|}/']))
	mouth3= lambda: print('\t                |#  ----  #|\n\t               ',random.choice(['|##______##|',' \#______#/']) )
	mouth4= lambda: print('\t                |&& ---- &&|\n\t               ',random.choice(['|&&&&&&&&&&|',' \&&&&&&&&/']))
	mouth5= lambda: print('\t                |   /--\   |\n\t               ',random.choice(['|__|____|__|', ' \_|____|_/']))
	mouth6= lambda: print('\t                |   )--(   |\n\t                |__________|')
	mouth7= lambda: print('\t                |   \__/   |\n\t                 \________/')
	ghats=[hat1, hat2, hat3, hat4, hat5, hat6, hat7] #lists for when more things are added...
	geyes=[eye1, eye2, eye3, eye4, eye5]
	gmouth=[mouth1, mouth2, mouth3, mouth4, mouth5, mouth6, mouth7]
	gbangs=[bangs1, bangs2, bangs3, bangs4, bangs5]
	fhair1=lambda: print('\t                 __________\n\t                /          \ \n\t               /            \ ')
	fhair2=lambda: print('\t                 __________\n\t                <          > \n\t               <            > ')
	fhair3=lambda: print('\t                 __________\n\t                {          } \n\t               {            } ')
	fbangs1=lambda: print('\t              /  /\/\/\/\/\  \ ')
	fbangs2=lambda: print('\t              <  /\/\/\/\/\  > ')
	fbangs3=lambda: print('\t              {  __________  } ')
	feyes1=lambda: print('\t              / |  |    |  | \ \n\t             /\/|  |    |  |\/\ ')
	feyes2=lambda: print('\t              < |  |    |  | > \n\t              < |  |    |  | > ')
	feyes3=lambda: print('\t              { |=[|]==[|]=| }\n\t              { |          | }')
	feyes4=lambda: print('\t              { | =  o  =  | }\n\t              { |          | }')
	fmouth1=lambda: print('\t                |   ----   |')
	fmouth2=lambda: print('\t                |   \__/   |')
	fmouth3=lambda: print('\t                |   )--(   |')
	fchin1=lambda: print('\t                |__________|')
	fchin2=lambda: print('\t                 \________/')
	fhair=[fhair1, fhair2, fhair3]
	fbangs=[fbangs1, fbangs2, fbangs3]
	feyes=[feyes1, feyes2, feyes3, feyes4]
	fmouth=[fmouth1, fmouth2, fmouth3]
	fchin=[fchin1, fchin2]
	if g=='F':
		random.choice(fhair)()
		random.choice(fbangs)()
		random.choice(feyes)()
		random.choice(fmouth)()
		random.choice(fchin)()			
	else:
		random.choice(ghats)()
		random.choice(gbangs)()
		random.choice(geyes)()
		random.choice(gmouth)()
def choice():
	while True:
		ch=input('\n\t\t    READY TO START? Y/N  ')
		if ch=='Y' or ch=='N':
			return ch
		else:
			print('\nWRONG ANSWER PLEBIAN')
def testnamegender(x):
	k=0
	commentary=0
	while k<x:

		print(make_name(random.randrange(2, 13), random.choice(['M', 'F'])))
		k+=1
def testallnames(x, length, g):
	k=0
	commentary=0
	while k<x:
		print(make_name(length, g))
		k+=1
def testface(x, g):
	k=0
	while k<x:
		make_face(g)
		k+=1
def namegen():
	if commentary:
        	print('\n\n\n\n 	~~~~~~~WELCOME TO YE OLDE NAME GENERATOR~~~~~~~\n 	|                                             |\n 	|    FIND THE NAME OF YOUR ALTER-EGO TODAY    |\n 	|                                             |\n 	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        	print('                          \\\_____//   ')
        	print('                          /  \ /  \   ')
        	print('                         |   0 0   |   ')
        	print('       |------------\    |{       }|    /------------|')
        	print('    )==|------------->   |    "    |   <-------------|==(    ')
        	print('       |------------/     \       /     \------------|')
        	print('                           \VvvvV/  ')
        	print('                           *88888*  ')
        	print('                            *88* ')
        	print('                    *8    *8 88*      8*')
        	print('                      88  *88  88*  88')
        	print('                    *888888      888888* ')
	ch=choice()
	while ch=='Y':
		print('\n')
		n=name()
		if commentary:
			print('\nARGH...\n')
		g=gen()
		if commentary:
			print('\nOKAY... LET THE GODS THINK\n...')
			time.sleep(1)
		print('\n\t\t        YOUR NAME IS\n\t\t        -->', make_name(n, g), '<--')
		if commentary:
			print('\n\t      ~~~~NOW GO OUT AND ADVENTURE~~~~\n')
			make_face(g)
		ch=choice()
	if ch=='N':
		print("      COME BACK WHEN YOU'RE READY FOR SOME ADVENTURE!  ")
		time.sleep(2)
namegen()

