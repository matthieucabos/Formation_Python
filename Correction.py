def __init__(self):
	pass

def Exercice1():
	"""
		``Correction Exercice 1``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> temps = 6.892
			>>> distance = 19.7
			>>> vitesse = distance/temps
			>>> print("La vitesse est de " + str(vitesse))
			>>> print("La vitesse est de " + str('{:06.1}'.format(vitesse)))

	"""
	pass

# Exercice 2

def Exercice2():
	"""
		``Correction Exercice 2``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> nom = input("Veuillez entrer votre nom.")
			>>> age = input("Veuillez entrer votre age.")
			>>> print("Vous vous appellez "+nom+" et vous avez "+age+" ans.")

	"""
	pass
	

# Exercice 3

def Exercice3():
	"""
		``Correction Exercice 3``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> import numpy as np 
			>>> nombre = input("Veuillez entrer un flottant")
			>>> if(float(nombre) >=0):
			... 	print(str(np.sqrt(float(nombre))))


	"""
	pass

# Exercice 4

def Exercice4():
	"""
		``Correction Exercice 4``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> a = 0
			>>> b = 10
			>>> while(a<b):
			... 	a+=1
			... 	print("a = "+str(a))
			>>> while(b!=0):
			... 	if(b % 2 == 0):
			... 		print("b = "+str(b))
			... 	b-=1


	"""
	pass

# Exercice 5

def Exercice5():
	"""
		```Correction Exercice 5``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> for i in range(0,15,3):
			... 	print(i)

	"""
	pass

# Exercice 6

def Exercice6():
	"""
		``Correction Exercice 6``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> def cube(x):
			... 	return x*x*x
			>>> cube(5)
			>>> 25

	"""
	pass

# Exerice 7
def Exercice7():
	"""
		``Correction Exercice 7``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> liste = [17,38,10,25,72]
			>>> liste.sort()
			>>> print(liste)
			>>> liste.append(12)
			>>> print(liste)
			>>> liste.reverse()
			>>> print(liste)
			>>> print(liste.index(17))
			>>> liste.remove(38)
			>>> print(liste)
			>>> print(liste[2:3])
			>>> print(liste[:2])
			>>> print(liste [3:])
			>>> print(liste[:])
			>>> print(liste[-1])


	"""
	pass

# Exercice 8

def Exercice8():
	"""
		``Correction Exercice 8``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> X = ['a','b','c','d']
			>>> Y = ['s','b','d']
			>>> print(X)
			>>> print(Y)
			>>> print('c' in X)
			>>> print('a' in Y)
			>>> # Union
			>>> Z=[]
			>>> for element in X:
			... 	if not element in Y:
			... 		Z.append(element)
			>>> for element in Y:
			... 	if not element in Z:
			... 		Z.append(element)
			>>> print(Z)
			>>> # Intersection
			>>> Z=[]
			>>> for element in X:
			... 	if element in Y:
			... 		Z.append(element)
			>>> print(Z)

	"""
	pass

# Exercice 9
def Exercice9():
	"""
		``Correction Exercice 9``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> def compterMots(chaine):
			>>> 	dico={}
			>>> 	tmp=""
			>>> 	for char in chaine:
			... 		tmp+=char
			... 		if(char==" ") or (char=="."):
			... 			tmp=tmp[:-1]
			... 			if not tmp in dico:
			... 				dico[tmp]=1
			... 			else:
			... 				dico[tmp]+=1
			... 			tmp=""
			>>> 	return dico
			>>> test="Ceci est un exemple déstiné à tester notre fonction fonction fonction."
			>>> print(compterMots(test))


	"""
	pass

# Exercice 10

def Exercice10():
	"""
		``Correction Exercice 10``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> TVA=1.2
			>>> TTC=0
			>>> choix=1
			>>> while(choix!=0):
			... 	choix=float(input("Veuillez entrer un prix HT ou 0 pour quitter"))
			... 	TTC=choix*TVA
			... 	print(TTC)
	
	"""
	pass

# Exercice 11

def Exercice11():
	"""
		``Correction Exercice 11``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> n = int(input("Veuillez entrer un entier positif"))
			>>> if(n%2==0):
			... 	print("n est PAIR")
			>>> else : 
			... 	print("n est IMPAIR")
	"""
	pass

# Exercice 12

def Exercice12():
	"""
		``Correction Exercice 12``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> def hauteurparcourue(NbMarche,HtMarche):
			... 	Hauteur= NbMarche*HtMarche*7*5/100
			... 	print("Pour "+str(NbMarche)+" marches de "+str(HtMarche)+" cm, il parcourt "+str(Hauteur)+" m ")

			>>>	hauteurparcourue(150,7)
	"""
	pass

# Exercice 13

def Exercice13():
	"""
		``Correction Exercice 13``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> def Tableau():
			... 	res=[]
			... 	for i in range(100,300,10):
			... 		heure=9+240/i
			... 		res.append((i,heure))
			... 	return res 
			>>> def tchacatchac(vitesse):
			... 	tab=Tableau()
			... 	heure=9
			... 	for element in tab:
			... 		if (element[0]==vitesse):
			... 			heure=element[1]
			... 	minute=(heure-int(heure))*60
			... 	print("Le dechiquetage est prévu pour "+str(int(heure))+" h "+ str(int(minute)))
			... 	return heure
			>>> tchacatchac(290)

	"""
	pass


#########################
# Python : Les fonctions#
#########################

def isnum(char):
	"""
		``Correction Isnum``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> return (char in ['1','2','3','4','5','6','7','8','9'])

	"""
	pass

def switch(x,*arg):
	"""
		``Correction Switch``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> dic ={}
			>>> for i in range (0,int(len(arg)-1)):
			... 	dic[arg[i]]=arg[i+1]
			>>> return dic.get(x,'default')

	"""
	pass

def reverse(liste):
	"""
		``Correction Reverse``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> res=[]
			>>> for i in range(0,len(liste)):
			... 	res.append(liste[len(liste)-i-1])
			>>> return res
	"""
	pass
def abs(x):
	"""
		``Correction Abs``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> if(x<0):
			... 	return -x 
			>>> else:
			... 	return x

	"""
	pass

def swap(a,b):
	"""
		``Correction Swap``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> b+=a
			>>> a=b-a 
			>>> b=b-a 
			>>> return(a,b)
	"""
	pass

def string2int(str):
	"""
		``Correction String2int``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> tmp=0
			>>> for i in range(0,len(str)):
			... 	tmp+=int(str[i])
			... 	tmp*=10
			>>> return tmp

	"""
	pass

def convert(val,base):
	"""
		``Correction Convert``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> res=''
			>>> sgn= 1 if val<0 else 0
			>>> if(sgn):
			... 	val=abs(val)
			... 	res='-'
			>>> while(val>0):
			... 	res=str(val%base)+res
			... 	val=int(val/base)
			>>> return res

	"""
	pass

def int2list(val,base):
	"""
		``Correction Int2list``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> res=[]
			>>> while val>0:
			... 	res.append(val%base)
			... 	val=int(val/base)
			>>> return reverse(res)

	"""
	pass

def complement_at(x,base=2):
	"""
		``Correction Complement_at``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> return (base-1-x)


	"""
	pass

#################################################
# Projet : Mise en application des connaissances#
#################################################


def arg_build(args):
	"""
		``Correction Arg_build``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> res=[]
			>>> if(args[0]=='i'):
			... 	tmp=0
			... 	for item in args[1:]:
			... 		if item != " ":  #Integer reconstruction since Horner Scheme
			... 			tmp*=10
			... 			tmp+=int(item)
			... 		else:
			... 			res.append(tmp)
			... 			tmp=0
			... 	res.append(tmp)
			>>> elif (args[0]=='s'):
			... 	tmp=""
			... 	for item in args[1:]:
			... 		if item!=" ":
			... 			tmp+=item
			... 		else:
			... 			tmp+=" "
			... 			res.append(tmp)
			... 			tmp=""
			... 	res.append(tmp)
			>>> elif (args[0]=='f'):
			... 	tmp=0.0
			... 	decimal=False
			... 	index=1
			... 	for item in args[1:]:
			... 		if item!=" " and item!=".":
			... 			tmp*=10
			... 			tmp+=float(item)
			... 		elif item=="." :
			... 			decimale=True
			... 		elif item == " ":
			... 			res.append(tmp)
			... 			tmp=0.0
			... 			decimal=False
			... 		elif decimale:
			... 			item=float(item)/10**index
			... 			tmp+=item
			... 			index*=10
			... 	res.append(tmp)
			>>> return res
	"""
	pass

def test(func):
	"""
		``Correction Test``

		**Vous trouverez en exemple le code source verifiant l'énoncé.**

		.. highlight:: python
		.. code-block:: python

			>>> class Decorator(object):
			... 	def __init__(self,func):
			... 		self.func=func
			... 	def __call__(self,*args,**kwargs):
			... 		real_arg=switch(self.func.__name__,
			... 			'summ','i10 5',
			... 			'divv','f20 2',
			... 			'concat','sCeci est un test')
			... 		real_res=switch(self.func.__name__,
			... 			'summ',15,
			... 			'divv',10,
			... 			'concat','Ceci est un test')
			... 		#Asserting return values from parameters values (testing procedure)
			... 		if(self.func(arg_build(real_arg),**kwargs)==real_res): #self.func implicitely convert args to tuple :(
			... 			print ("Test passed, congratulations !")
			... 			return self.func(arg_build(real_arg),**kwargs)
			... 		else:
			... 			print ("Error occured, go back to work lazy dev !")
			>>> return Decorator
	"""
	pass