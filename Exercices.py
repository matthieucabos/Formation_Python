
############################
# Python : Les premiers pas#
############################

# Exercice 1

def Exercice1():
	"""
		**Affectez  les variables temps et distance par les valeurs 6.892 et 19.7.**

		Calculez et affichez la valeur de la vitesse.

		Améliorez l'affichage en imposant un chiffre après le point décimal

		Examples
		--------
		>>> La vitesse est de 2.8583865351131745
		>>> La vitesse est de 03e+00

		See Also
		--------
		Correction.Exercice1

	"""

# Exercice 2

def Exercice2():
	"""
		**Saisire un nom et un age en utilisant l'instruction input() et les afficher.**

		Examples
		--------
		>>> Veuillez entrer votre nom.Matthieu
		>>> Veuillez entrer votre age.33
		>>> Vous vous appellez Matthieu et vous avez 33 ans.

		See Also
		--------
		Correction.Exercice2

	"""

# Exercice 3

def Exercice3():
	"""
		**Saisissez un flottant.**

		S'il est positif ou nul, affichez sa racine, sinon affichez un message d'erreur.

		Examples
		--------
		>>> Veuillez entrer un flottant13.123
		>>> 3.622568149807537

		See Also
		--------
		Correction.Exercice3

	"""

# Exercice 4

def Exercice4():
	"""
		**Initialisez deux entiers : a = 0 et b = 10 .**

		Ecrire une boucle affichant et incrémentant la valeur de a tant qu'elle reste inferieure a celle de b.

		Ecrire une autre boucle decrementant la valeur de b et affichant sa valeur si elle est paire.

		Boucler tant que b n'est pas nul.

		Examples
		--------
		>>> a = 1
		>>> a = 2
		>>> a = 3
		>>> a = 4
		>>> a = 5
		>>> a = 6
		>>> a = 7
		>>> a = 8
		>>> a = 9
		>>> a = 10
		>>> b = 10
		>>> b = 8
		>>> b = 6
		>>> b = 4
		>>> b = 2

		See Also
		--------
		Correction.Exercice4


	"""

# Exercice 5

def Exercice5():
	"""
		**Affichez les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for et l'instruction range().**

		Examples
		--------
		>>> 0
		>>> 3
		>>> 6
		>>> 9
		>>> 12

		See Also
		--------
		Correction.Exercice5

	"""

# Exercice 6

def Exercice6():
	"""
		**Ecrire une fonction cube qui retourne le cube de son argument.**

		Examples
		--------
		>>> cube(5)
		>>> 125

		See Also
		--------
		Correction.Exercice6

	"""

# Exerice 7
def Exercice7():
	"""
		**Definir la liste : liste = [17,38,10,25,72], puis effectuez les actions suivantes :**
			* Triez et affichez la liste
			* Ajoutez l'élément 12 à la liste et affichez la liste
			* Renversez et affichez la liste
			* Affichez l'indice de l'élément 17
			* Enlevez l'élément 38 et affichez la liste
			* Affichez la sous-liste du 2eme élément exclus au 3eme élément inclus
			* Affichez la sous-liste du premier au deuxieme element inclus
			* Affichez la liste du 3eme élément exclus à la fin
			* Affichez le dernier élément en utilisant un indicage negatif

		Examples
		--------
		>>> [10, 17, 25, 38, 72]
		>>> [10, 17, 25, 38, 72, 12]
		>>> [12, 72, 38, 25, 17, 10]
		>>> 4
		>>> [12, 72, 25, 17, 10]
		>>> [25]
		>>> [12, 72]
		>>> [17, 10]
		>>> 10

		See Also
		--------
		Correction.Exercice7


	"""

# Exercice 8

def Exercice8():
	"""
		**Definir deux Ensemble A et B en utilisant les listes.**

		Soient X=[a,b,c,d] et Y=[s,b,d], affichez les Exemples suivants : 
			* Les ensembles initiaux
			* Le test d'appartenance de l'élément 'c' à X
			* Le test d'appartenance de l'élément 'a' à Y
			* L'ensemble d'union de X et Y (Union de Cantor)
			* L'ensemble d'intersection de X et Y (Intersection de Cantor)

		Examples
		--------
		>>> ['a', 'b', 'c', 'd']
		>>> ['s', 'b', 'd']
		>>> True
		>>> False
		>>> ['a', 'c', 's', 'b', 'd']
		>>> ['b', 'd']

		See Also
		--------
		Correction.Exercice8

	"""

# Exercice 9
def Exercice9():
	"""
		**Ecrire une fonction compterMots(chaine) ayant comme argument une chaine de caractères et qui renvoie un dictionnaire qui contient la frequence de tout les mots dans la chaine entrée.**
		
		Bonus : Exprimer cette fréquence en pourcentage.

		Examples
		--------
		>>> test="Ceci est un Examples déstiné à tester notre fonction fonction fonction."
		>>> print(compterMots(test))
		>>> {'Ceci': 1, 'est': 1, 'un': 1, 'Examples': 1, 'déstiné': 1, 'à': 1, 'tester': 1, 'notre': 1, 'fonction': 3}

		See Also
		--------
		Correction.Exercice9

	"""
# Exercice 10

def Exercice10():
	"""
		**Ecrivez une boucle while implementant le comportement suivant :**

		Entrer un prix HT (entrer 0 pour terminer) et afficher sa valeur TTC.

		Examples
		--------
		>>> Veuillez entrer un prix HT ou 0 pour quitter123.456
		>>> 148.1472
		>>> Veuillez entrer un prix HT ou 0 pour quitter456.123
		>>> 547.3475999999999
		>>> Veuillez entrer un prix HT ou 0 pour quitterq

		See Also
		--------
		Correction.Exercice10
	
	"""

# Exercice 11

def Exercice11():
	"""
		**Veuillez implementer le comportement suivant :**

		L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2 et IMPAIR sinon.

		Examples
		--------
		>>> Veuillez entrer un entier positif1
		>>> n est IMPAIR

		See Also
		--------
		Correction.Exercice11

	"""

# Exercice 12

def Exercice12():
	"""
		**Un gardien de phare va aux toilettes cinq fois par jour or les WC sont au rez-de-chaussée.**

		Ecrire une procedure (une fonction sans retour) hauteurParcourue qui recoit deux parametres : 
			* Le nombre de marches du phare
			* la hauteur de chaque marche (en cm)

		Le programme affichera en réponse : 
		Pour x marches de y cm, il parcourt z.zz m par semaine

		Pour information :
			* Une semaine comporte 7 jours
			* Une fois en bas le gardien doit remonter
			* Le resultat est à exprimer en m

		Examples
		--------
		>>> Pour 150 marches de 7 cm, il parcourt 367.5 m 

		See Also
		--------
		Correction.Exercice12
	"""

# Exercice 13

def Exercice13():
	"""
		**Je suis ligoté sur les rails en gare de Montpellier.**

		Ecrire un programme qui affiche un tableau me permettant de connaitre l'heure à laquelle je serai dechiqueté par le train parti de Toulouse à 9h (il y a 2470km entre la gare de Montpellier et Toulouse).

		Le tableau prédira les différentes heures possibles pour toutes les vitesse allant de 100km/h à 300km/h par pas de 10 km/h.

		Les Examples seront arrondis à la minute inférieure.

		* Ecrire une procedure tchacatchac qui reçoit la vitesse du train et qui affiche l'heure du drame
		* Ecrire le programme principal qui affiche le tableau demandé.

		Examples
		--------
		>>> tchacatchac(290)
		>>> Le dechiquetage est prévu pour 9 h 49

		See Also
		--------
		Correction.Exercice13

	"""

#########################
# Python : Les fonctions#
#########################

def isnum(char):
	"""
		**Definissez une fonction determinant si le contenu d'une variable de type character contient une valeure numérique.**

		============== ========== ========================
		**Parametre**   **Type**   **Descripion**
		*char*          str        Le charactère à tester
		============== ========== ========================


		Examples
		--------
		>>> char='5'
		>>> isnum(char)
		True
		>>> char='S'
		>>> isnum(char)
		False

	"""

def switch(x,*arg):
	"""

		**Ecrivez une fonction reprenant le switch des langages C et C++ en utilisant la structure de donnée étudiée Dictionnary.**

		============== ========== ======================================
		**Parametre**   **Type**   **Description**
		*x*             Generic    La variable/valeure à tester
		*arg*           Str        Les differents aiguillages du switch
		============== ========== ======================================

		Vous pourrez également utiliser la boucle de votre choix pour finaliser l'algorithme.

		La fonction devra être utilisé selon la syntaxe ci dessous.

		Examples
		--------
		>>> test=True
		>>> Ex=switch(test,
		... True,'Le switch n° 1',
		... False,'Le switch n° 2')
		>>> print(Ex)
		Le switch n° 1
		>>> test=False
		>>> Ex=switch(test,
		... True,'Le switch n° 1',
		... False,'Le switch n° 2')
		>>> print(Ex)
		Le switch n° 2

	"""

def reverse(liste):
	"""
		**Ecrivez une fonction prenant en argument une liste et retournant la liste inverse.**

		============== ========= ======================
		**Parametre**   **Type**   **Description**
		*liste*         list       La liste à inverser  
		============== ========= ======================


		La fonction devra utiliser les propriétées de liste étudiées.

		Vous pourrez également utiliser la boucle de votre choix pour finaliser l'algorithme.

		Examples
		--------
		>>> liste=[1,2,3,4,5,6,7,8,9]
		>>> print(reverse(liste))
		[9, 8, 7, 6, 5, 4, 3, 2, 1]

	"""

def abs(x):
	"""
		**Ecrivez la fonction native abs de Python en utilisant la structure de contrôle if-the-else étudiée.**

		============== ========== ======================
		**Parametre**   **Type**   **Description**
		*x*             int/float  La valeure à traiter
		============== ========== ======================


		Examples
		--------
		>>> x=123
		>>> abs(x)
		123
		>>> x=-456
		>>> abs(x)
		456

	"""

def swap(a,b):
	"""
		**Ecrivez une fonction inversant la valeure de ses parametres a et b et retournant le resultat sous forme d'un tuple.** 

		============== ========== =========================
		**Parametre**   **Type**   **Description**
		*a*             int/float  La valeure a a inverser
		*b*             int/float  La valeure b a inverser
		============== ========== =========================

		La fonction **ne doit pas utiliser de variables supplementaires**.

		Examples
		--------
		>>> a=52
		>>> b=25
		>>> print(a,b)
		52 25
		>>> print(swap(a,b))
		(25, 52)
	"""

def string2int(str):
	"""
		**Ecrivez une fonction prenant en paramètre une chaine de charactere representant un nombre et retournant l'integer correspondant.**

		============== ========== ================================================================
		**Parametre**   **Type**   **Description**
		*str*           str        Une chaine de caractères représentant un nombre (ex : 123456)
		============== ========== ================================================================

		Vous utiliserez les fonctions natives de transtypage.

		Examples
		--------
		>>> x='123456'
		>>> x*10
		'123456123456123456123456123456123456123456123456123456123456'
		>>> string2int(x)*10
		12345600

	"""

def convert(val,base):
	"""
		**Ecrire une fonction qui converti une valeure dans une base determinée par parametre.**

		================ ========== =======================
		**Parametres**   **Type**   **Description**
		*val*            int        La valeure à convertir
		*base*           int        La base de conversion
		================ ========== =======================

		La base devra être inférieur à 10.

		Examples
		--------
		>>> val=123
		>>> for i in range(2,10):
		...     print(str(val)+" converti en base "+str(i)+" s'ecrit : "+str(convert(val,i)))
		... 
		123 converti en base 2 s'ecrit : 1111011
		123 converti en base 3 s'ecrit : 11120
		123 converti en base 4 s'ecrit : 1323
		123 converti en base 5 s'ecrit : 443
		123 converti en base 6 s'ecrit : 323
		123 converti en base 7 s'ecrit : 234
		123 converti en base 8 s'ecrit : 173
		123 converti en base 9 s'ecrit : 146

	"""

def int2list(val,base):
	"""
		**Ecrivez une fonction prenant en argument une valeure et la convertissant en une liste de nombre représentant cette même valeure.**

		============= ========== ==========================
		**Parametre**   **Type**   **Descripion**
		*val*           int        La valeur à convertir
		*base*          int        L'indice de base
		============= ========== ==========================


		Examples
		--------
		>>> val=123
		>>> int2list(val,10)
		[1, 2, 3]
		>>> int2list(val,2)
		[1, 1, 1, 1, 0, 1, 1]

	"""

def complement_at(x,base=2):
	"""
		**Ecrivez en une seule ligne le corps de la fonction de complement de base.**

		============== ========== ======================================
		**Parametre**   **Type**   **Description**
		*x*             int        La valeure à traiter (entre 0 et 9)
		*base*          int        L'indice de base
		============== ========== ======================================

		Le complément est une opération mathématiques visant à donner, dans la base numérique spécifiée, la valeure complémentaire à cette base.
			* Le complément de la valeur 0 en base 2 est 1
			* Le complément de la valeur 0 en base 3 est 2
			* ...				
			* Le complément de la valeur 0 en base 10 est 9


		Examples
		--------
		>>> x=0
		>>> for i in range(2,10):
		...     print(complement_at(0,i))
		... 
		1
		2
		3
		4
		5
		6
		7
		8


	"""

#################################################
# Projet : Mise en application des connaissances#
#################################################


def arg_build(args):
	"""
		**Ecrire une fonction prenant en compte une chaine de charactères contenant une liste d'arguments générique (dont le type n'est pad déterminé à l'avance).**

		=============== =========== ======================================================================
		**Parametre**     **Type**   **Description**
		*args*            String     La chaine de charactères contenant la liste d'arguments à convertir
		=============== =========== ======================================================================


		La fonction reconstruira une liste des arguments convertis dans le bon type.

		La chaine de charctère respecte le format suivant :
			* 'i10 5 2'             : la lettre i spécifie le type d'entrée (Integer) suivi des valeurs à traiter
			* 'f10.32 5.12 2.14'    : la lettre f spécifie le type d'entrée (Float) suivi des valeurs à traiter
			* 'sFirst Second Third' : la lettre s spécifie le type d'entrée (String) suivi des champs à traiter

		Vous utiliserez les structures de contrôles suivantes : 
			* If-then-else
			* Boucle for

		Le resultat doit prendre la forme d'une liste d'arguments de bon type.

		Examples
		--------
	"""

def test(func):
	"""
		**Ecrire une fonction de type decorateur.**

		Un decorateur est defini en Python ici : https://www.python.org/dev/peps/pep-0318/

		Vous prendrez le temps d'effectuer une recherche documentaire sur les decorateurs pour en comprendre le principe de base.

		Vous définirez dans une fonction 'test' un décorateur de test prenant en argument le nom d'une fonction et réalisant un test unitaire avec un jeu de données de test.

		Vous trouverez les fonctions définies ci dessous à tester avec les valeures de votre choix :

		Examples
		--------
		>>> @test('func')
		>>> def summ(args):
		... 	summ=0
		... 	for item in args:
		... 		summ+=item
		... 	return summ

		>>> @test('divv')
		>>> def divv(args):
		... 	return args[0]/args[1]

		>>> @test('concat')
		>>> def concat(args):
		... 	res=""
		... 	for item in args:
		... 		res+=item
		... 	return res

		Pour réaliser ceci, vous utiliserez la fonction precedemment définie 'arg_build' et la fonction switch de l'exercice 2 du chapitre des fonctions.
		Afin de redefinir un decorateur, on passera par une définition de classe interne 'Decorator' via les fonctions natives __init__ et __call__
		Vous trouverez la documentation associée aux classes ici :https://docs.python.org/3/tutorial/classes.html

		La fonction de test devra afficher :
			* 'Test passed' si le resultat vérifié est le bon
			* 'Error occured' sinon
	"""

# @test()
# def summ(self,args):
# 	summ=0
# 	for item in args:
# 		summ+=item
# 	return summ

# @test()
# def divv(self,args):
# 	return args[0]/args[1]

# @test()
# def concat(self,args):
# 	res=""
# 	for item in args:
# 		res+=item
# 	return res
