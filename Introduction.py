# class Introduction:
# 	def __init__():
# 		pass

def Versions():
	"""
		La dernière version 3,9 sera la seule étudiée dans cette formation. 

		En effet les versions inférieures à la version 3 sont aujourd’hui considérées comme **obsolètes**. 

		Leur utilisation est peu recommandée compte tenu des différences de syntaxes apparues avec la version 3. 

		La communauté scientifique international s’est accordée à programmer avec la version 3.

		L’installeur est disponible sur le site https://www.python.org

		La version la plus récente sera choisie par default. 

		En effet il s’agit de la version actuellement mise à jour par l’équipe de développeur Python, les versions 1 et 2 ont étés abandonnées depuis des années et donc non mises à jour.

		On évitera d’utiliser les versions antérieurs à la version 3.0.
	"""
	pass

def Espace_De_Travail():
	"""
		L’espace de travail dans le cadre de la programmation Python s’organise autour de différents piliers :
			* l’installation **système** de python permettra d’utiliser Python en console et en IDE en spécifiant le chemin d’accès au dossier Python,
			* Les IDE Spyder, VisualStudio, etc permettent effectivement d’intégrer la console système dans un éditeur de texte : une configuration que certain préfèrent.
	
		Le choix sera laissé à l’étudiant en partant du principe que les lignes de commandes écrites sont rigoureusement indépendantes du logiciel de traitement de texte utilisé.

		Dans le cadre d’une utilisation console : 
			* sous Linux l’installation permet d’accéder aux fonctionnalités de python en tapant python ou python3 dans le terminal
			* sous Windows le chemin d’accès est à spécifier dans les variables d’environnement système.			
	"""
	pass

def Variables():
	"""
		Une variable est par définition un emplacement de mémoire RAM pré-réservé qui permet de stocker une information. 

		Elle est identifiée par un **nom unique** au sein du programme et peut être manipulée par des opérateurs et des variables de même type.
	
		Dans python on distingue plusieurs **types principaux** de variables :
			* Variables simples :
				* *str* : String, il s’agit de chaînes de caractères **dynamiques** que l’on peut manipuler et mettre à jour dans le code 
				* *int* : Integer, il s’agit d’une valeur numérique entière **signée** que l’on peut également manipuler et mettre à jour.
				* *Float* : Il s’agit d’une valeur numérique décimale **signée** que l’on peut également manipuler et mettre à jour.

			* Variables de structure :
				* *list* : Il s’agit d’une structure de donnée regroupant plusieurs éléments de même type ou de type différents reliés par un indexage mémoire rapide d’accès. Le type list possède des méthodes natives
				* *tuple* : De la même manière, il s’agit d’une structure de donnée prenant en compte deux ou plus éléments indexés. Le type tuple possède également des méthodes natives.
				* *Dictionnary* : Il s’agit d’une structure de donnée associant à chaque éléments utilisés en qualité de clé une valeurs de type choisie

		Une variable est définie selon les règles suivantes :
			* **Assignation et suppression**
				* L’assignation de variable est défini par l’opérateur **=**.
				* Le nom de la variable est à gauche de l’opérateur, la valeur assignée est positionnée à droite.
				* En Python, le typage des variables est **dynamique**, par conséquent, le type n’est pas à indiquer lors de l’initialisation.
				* On peut initialiser une variable à n’importe quel endroit du code.
				* Les initialisations de structures de données sont similaires. 

			* **Par convention les variable sont soumises aux Conventions de nommage :**
				* Le nom d’une variable est composé de caractères alpha-numériques
				* Le nom d’une fonction ne doit pas commencer par un chiffre ou un caractère spécial
				* Le nom d’une fonction est composé de caractères alpha-numériques

		Examples
		--------
		>>> # Exemple d'assignations
		>>> v=4
		>>> w=5.23
		>>> x="Une chaine de caractères"
		>>> # Exemple d'instanciation
		>>> x=[]
		>>> y=()
		>>> z={}
		>>> # Conventions de nommage
		>>> import sys
		>>> index=0
		>>> Pre_Cos_0=1.0
		>>> _sys_arg=sys.argv
	"""
	pass

def Commentaires():
	"""
		En python une ligne de commentaire est précédée du symbole **#**.
		Il peut être placé n’importe ou **a droite** des lignes de codes et doit être contenu sur une ligne.
		En cas de commentaires multiples, un symbole # sera placé devant chaque ligne.

		Examples
		--------
		>>> def maFonction(): # Une ligne de commentaire resumant le role de ma fonction
		...     pass
		... 
		>>> # Un commentaire
		>>> # Sur plusieurs lignes
		>>> # Pour expliquer une partie du code

	"""
	pass

def Modules_Et_Packages():
	"""
		En programmation Python les modules et packages sont les indispensables d’un travail de qualité.

		Que ce soit des modules écrits par le programmeur ou des packages installés depuis les serveurs Python, ils vont conférer à Python une extension du domaine de travail non négligeable (ex : les bibliothèques numpy et scipy regroupant l’ensemble des opérations scientifiques de précision).
		Un module est une bibliothèque écrite en Python que l’on peut importer dans un projet plus conséquent. 

		Les modules les plus utilisées sont achevés sous forme de package que l’on peut utiliser via la commande d’installation de package Python pip.

		De nombreux modules et packages sont disponibles gratuitement sur divers serveurs tels que Pypi. 

		Ils permettent de greffer des fonctionnalités telles que la mise au point d’une interface GUI (Graphique User Interface), l’utilisation de structures de données optimisées, etc.

		Un package est une version distribué d’un module attesté par l’équipe de développement Python.
		Afin d’installer un package Python, on utilise la commande pip dans l’invite de commande en utilisant la syntaxe suivante :

		**pip install nom_de_la_librairie**

		Une fois la librairie installé dans l’arborescence du système, on peut la charger dans un code Python depuis n’importe quel emplacement du disque dur. Pour cela on utilisera le mot clé import associé ou non aux mots clés from et as.

		Examples
		--------
		>>> import numpy              # Les méthodes numpy sont accessibles via numpy.method
		>>> import numpy as np        # Les méthodes numpy sont accessibles via np.method
		>>> from numpy import complex # La classe complex est disponible dans le code
		>>> from numpy import *       # L'ensemble des classes et méthodes numpy sont importées

		Bien évidemment, on peut écrire et réaliser ses modules soit même. Pour cela, on réalise le code d’une bibliothèque sans programme principal main (on n’implémente que les classes, méthodes et fonctions nécessaires). Une fois le module réalisé et sauvegardé (par ex sous le nom mon_module.py), son utilisation reste identique, on peut l’intégrer à un autre fichier source via la commande 

		*from mon_module import **
	"""
	pass

def Aide():
	"""
		La documentation officielle de Python est disponible sur le site https://docs.python.org/

		Elle contient l'intégralité des éléments de connaissances nécessaires à la bonne utilisation du langage :
		    * Syntaxe
		    * Règles de programmation
		    * Description des classes et méthodes
		    * Etc

		Chaque module ou package possède également une documentation propre disponible sur https://readthedocs.org/ . 
		Le lien vers la documentation est généralement associé aux plateformes de distribution du code.
	"""
	pass
  
# class Python_Theorie:
# 	def __init__():
# 		pass

# 	class Chaines_De_Caracteres:
# 		def __init__():
# 			pass

# 		def Concatenation():
# 			"""
# 				La concaténation de chaîne de caractère est réalisée par l’opérateur +. 
# 				La concaténation est l’opération de liaison de deux variables de type Str A et B indépendantes l’une de l’autre. Elle est donc définie par A + B .
# 				Il s’agit de concaténer deux variables de type str, sans quoi la concaténation générera un message d’erreur.

# 				Examples
# 				--------
# 				>>> a="Je m'appelle "
# 				>>> b="Arthur"
# 				>>> c=a+b
# 				>>> print(c+" et j'ai plus de "+str(250)+" ans.")
# 				Je m'appelle Arthur et j'ai plus de 250 ans.

# 			"""
# 			pass

# 		def Indexation_Extraction():
# 			"""
# 				L’indexation des chaînes de caractères en Python est réalisée par le biais des symboles [] accolés au nom de la variable.
				
# 				L’extraction d’une sous-chaine de caractères est réalisée en utilisant les mêmes symboles et en utilisant l’index de début de chaîne inclus et l’index de fin de chaîne exclus séparés par le symbole : .
			
# 				Examples
# 				--------
# 				>>> # Exemple : Indexation
# 				>>> test="blablabla"
# 				>>> test[0]
# 				'b'
# 				>>> # Exemple : Extraction
# 				>>> test="blablabla"
# 				>>> test[2:5]
# 				'abl'

# 			"""
# 			pass

# 		def Conversion_Majuscules_Minuscules():
# 			pass

# 		def Recherche_De_Chaines():
# 			"""
# 				Afin de rechercher une sous-chaine de caractères dans une chaîne de caractères existante on utilise le mot clé **in** en plaçant la sous-chaine à rechercher comme premier opérande et la chaîne principale comme deuxième opérande.
# 				Le résultat du test est égal à la valeur booléenne « True » si la sous chaîne est présent, False sinon.

# 				Examples
# 				--------
# 				>>> test="blablabla"
# 				>>> "bla" in test
# 				True
# 				>>> "cla" in test
# 				False				
# 			"""
# 			pass

# 		def Decoupage_De_Sous_Chaines():
# 			"""
# 				Afin de découper en sous chaîne une chaîne de caractère instancié, on peut utiliser plusieurs méthodes :
# 					* la méthode de l’indexage et de l’extraction. En effet, en extrayant des tronçons de mêmes taille, on découpe la chaîne aisément.
# 					* la méthode native split à laquelle on passe en argument un séparateur de sous-chaine.

# 				Examples
# 				--------
# 				>>> # Exemple : Decoupage de sous-chaines par extraction
# 				>>> test="blablabla"
# 				>>> splitted=[]
# 				>>> splitted.append(test[0:3])
# 				>>> splitted.append(test[3:6])
# 				>>> splitted.append(test[6:9])
# 				>>> print(splitted)
# 				['bla', 'bla', 'bla']
# 				>>> # Exemple : Utilisation de la méthode split
# 				>>> test="blablabla"
# 				>>> test="bla,bla,bla"
# 				>>> splitted=test.split(',')
# 				>>> print(splitted)
# 				['bla', 'bla', 'bla']

# 			"""

# 			pass

# 		def Nettoyage_Completion():
# 			"""
# 				Le nettoyage ou la complétion d’une chaîne de caractère peut être réalisé en effectuant des remplacement de caractères et des suppression (par exemple suppression des caractères \n, remplacement des Majuscule par des minuscules, etc).
# 				Il existe un nombre important d’opérateurs de chaînes de caractères en Python, dont la documentation détaillée est disponible sur le site officiel de documentation de Python.
# 				Par exemple, la suppression des caractère de saut de lignes dans le contenu d’un fichier sous forme de chaîne de caractères est réalisé par le code suivant.

# 				Examples
# 				--------
# 				>>> res=""                           # Le résultat instancié de type Str
# 				>>> file=open("./test.txt")          # Le fichier est ouvert
# 				>>> content=file.read()              # On lit le contenu du fichier
# 				>>> for item in content:
# 				...     if (item != "\n"):
# 				...             res+=" "+item        # On reconstruit le contenu du fichier
# 				... 
# 				>>> print(res)
# 				 c e c i e s t   u n f i c h i e r e x e m p l e   s u r   p l u s i e u r s   l i g n e s

# 			"""
# 			pass

# 		def Conversion_En_Chaine_De_Caracteres():
# 			"""
# 				La conversion de la valeur d’une variable en chaîne de caractères est toujours possible. 
# 				On utilisera l’opérateur de trans-typage str() en donnant comme argument la variable à convertir.
			
# 				Examples
# 				--------
# 				>>> test=123.456
# 				>>> type(test)
# 				<class 'float'>
# 				>>> str(test)
# 				'123.456'
# 				>>> type(test)
# 				<class 'float'>
# 				>>> type(str(test))
# 				<class 'str'>

# 				La variable convertie n’est plus utilisable dans son contexte d’origine : une variable Float convertie en Str **ne pourra pas** être réutilisée telle quel dans une opération mathématiques.
# 				La conversion inverse est nécessaire (cf Conversion).

# 			"""
# 			pass

# 	class Valeurs_Numeriques:
# 		def __init__():
# 			pass

# 		def Entiers():
# 			"""
# 				Les Integer sont monnaie courante en programmation : compteur, index, etc
# 				Ils représentent l’ensemble des entiers naturels N.
# 				En Python l’instanciation d’une variable peut se faire à n’importe quel endroit du code. L’assignation défini le type de la variable. Une variable integer sera donc instanciée en utilisant la syntaxe suivante :
				
# 				**x=0**
				
# 				où x est le nom de la variable et 0 la valeur instanciée. 
# 				Étant donné que la valeur 0 est considérée comme integer, la variable sera instancié de type integer. Python passe par une déclaration implicite des types.
# 				L’ensemble des opérations définies avec les Integer est répertorié dans la documentation officielle de Python.
# 			"""
# 			pass

# 		def Nombres_A_Virgules_Flottante():
# 			"""
# 				Les Nombre à virgules flottante (ou Float en anglais) représentent l’ensemble des réels R.
# 				Ce sont les variables les plus gourmandes en mémoire : attention donc à les utiliser à bon escient.
# 				On les utilisera dans des calculs nécessitant une précision décimale, hors de question d’instancier un compteur ou un index avec une variable flottante.
# 				Les opérations natives sont héritées du type integer et regroupe l’ensemble des opérateurs usuels de maths.
# 				En Python ils existent les bibliothèques natives numpy et scipy implémentant grand nombre de calculs et lois scientifiques utilisant les nombres flottants.
# 			"""
# 			pass

# 		def Nombres_Complexes():
# 			"""
# 				Les nombres complexes sont constitués d’une partie réel et imaginaire dont la définition est résumé à la formule suivante.
# 				Pour tout nombre z appartenant à l’ensemble C des nombres complexes, il existe les nombres a et b appartenant à l’ensemble R des nombres réels tels que z s’exprime par :

# 				**z = aj + b**

# 				L’arithmétique des nombres complexes, considérée acquise, ne sera pas abordé dans ce chapitre. 
# 				Python permet de manipuler aisément ces valeurs via le module intégré cmath.
# 				L’instanciation se fait selon la syntaxe suivante :

# 				**z = aj+b**

# 				où a et j sont deux réels définis par l’utilisateur.
# 				Les opérations arithmétiques standards ne nécessitent pas l’importation du module cmath. Ainsi l’expression suivante sera correctement interprété depuis la console.

# 				Examples
# 				--------
# 				>>> z=3j+2
# 				>>> z2=1j+5
# 				>>> print(z+z2)
# 				(7+4j)

# 				Les fonctions évoquées dans ce chapitre sont les suivantes :
# 				    * *phase* : Il s’agit de calculer la phase d’un nombre polaire z fourni en argument. La syntaxe d’appel est la suivante : cmath.phase(z)
# 				    * *polar* : Il s’agit de calculer les coordonnées polaires d’un nombre complexe z fourni en argument. La syntaxe d’appel est la suivante : cmath.polar(z)
# 				    * *rect* : Il s’agit de calculer les coordonnées rectangulaire d’un nombre complexe sous forme polaire déterminé par ses coefficient r et phi ou phi est la phase du nombre complexe et r le module du nombre complexe. La syntaxe d’appel est la suivante : cmath.rect(r,phi)

# 			"""
# 			pass

# 		def Conversions():
# 			"""
# 				Les conversions de types sont très largement utilisées en python, on parle de Transtypage.
# 				Le trans-typage est utilisé dans presque tous les langages informatiques typés. 
# 				Il s’agit d’une opération de base permettant de convertir la valeur d’une variable typée vers la valeur la représentant dans un autre type.
# 				Par exemple un coefficient entier utilisé dans une opération flottante sera implicitement convertie dans sa valeur flottante correspondante. De la même manière une valeur flottante saura être tronquée à la virgule lors d’un conversion integer.
			
# 				Examples
# 				--------
# 				>>> x=10      # x est de type integer
# 				>>> y=float(x)
# 				>>> print(y)  # y est maintenant de type float
# 				10.0
# 				>>> print("J'espère avoir au moins "+str(y)+" de moyenne au cours Python cette année !")
# 				J'espère avoir au moins 10.0 de moyenne au cours Python cette année !
# 				>>>           # La variable transtypée str(y) est maintenant de type Str

# 			"""
# 			pass

# 		def Booleens():
# 			"""
# 				L’algèbre de Boole définie les standard de la logique informatique. 
# 				Il est impensable pour un langage de ne pas implémenter les valeurs booléennes et leurs opérateurs associés.
# 				Une variable booléenne a pour valeur True ou False, implémentée en utilisant des Integer, la notation est parfois simplifiée par les valeurs 1 et 0 représentant respectivement les valeurs True et False.
			
# 				Les opérateurs courant sont :
# 					* *Logic And*: Réalise le ET logique entre deux booléens            (noté A and B)
# 					* *Logic Or*: Réalise le Ou logique entre deux booléens             (noté A or B)
# 					* *Logic Not* : Réalise le Non Logique d’une valeur booléenne       (noté not A)
# 					* *Logic Nand* : Réalise Le Non logique du résultat d’un Et logique (noté not ( A and B ))
# 					* *Logic Nor* : Réalise le Non logique d’un Ou logique              (noté not ( A or B ))

# 				Les autres opérateurs et lois booléennes sont dérivées de l’utilisation de ces opérateurs de base.
# 			"""
# 			pass

# 		def ObjetVide():
# 			"""
# 				L’objet vide est dénommé None est représente l’absence de valeur dans une variable. 
# 				Il est par définition non-typé et peut s’utiliser en comparaison de n’importe quel type.
			
# 				Examples
# 				--------
# 				>>> import random
# 				>>> tab=[]
# 				>>> for i in range(0,10):
# 				...     tab.append(random.randint(0,100))
# 				... 
# 				>>> tab.append(None)
# 				>>> while(tab[i]!=None):
# 				...     i+=1
# 				... 
# 				>>> while(tab[i]!=None):
# 				...     i+=1
# 				...     print(tab[i])
# 				... 
# 				>>> i=0
# 				>>> while(tab[i]!=None):
# 				...     print(tab[i])
# 				...     i+=1
# 				... 
# 				100
# 				70
# 				25
# 				38
# 				42
# 				35
# 				74
# 				85
# 				98
# 				10

# 			"""
# 			pass

# 		def Date_Et_Temps():
# 			"""
# 				Le module datetime de Python nous sert à récupérer des informations concernant la date et l’heure depuis les informations système.
# 				Il possède des méthodes natives dont on étudiera uniquement les principales : 
# 				    * *date* : Permet de récupérer la date au format standardisé
# 				    * *time* : Permet de récupérer l’heure au format standardisé
# 				    * *datetime* : Permet de récupérer la date et l’heure au format standardisé
			
# 				Les données datetime sont de même type et donc les opérations d’addition, de soustraction, multiplication, division et modulo sont disponibles ainsi que les méthodes abs(), str() et repr().

# 			"""
# 			pass

# 	class Structures:
# 		def __init__():
# 			pass

# 		def Listes():
# 			"""
# 				Les listes sont une structure de données native en Python. 
# 				On peut considérer le type List comme l’extension des types natifs de bases integer, float et str. 
# 				Le type list est constitué d’un tableau chaîné sur lequel certaines opérations sont permises.

# 				L’extraction d’élément
# 				----------------------

# 				Afin d’extraire des informations précises contenues dans une liste, on peut extraire une partie de la liste sous forme de sous-liste ou extraire un élément individuellement grâce à son indice.
# 				La syntaxe est la suivante.

# 				Le type du résultat d’une extraction est List, le type  lors de la lecture d’un élément simple est le même que ceux des éléments lors de l’instanciation.
# 				L’extraction indicée est effectuée de la manière suivante :
# 					* *liste[x:y]* va extraire tout les éléments de x INCLUS à y EXCLUS (mathématiquement résumé à [x;y[)
# 					* *liste[x:]* va extraire tout les éléments de x INCLUS jusqu’à la fin de liste (noté [x,+inf[)
# 					* *liste[:y]* va extraire tout les éléments de 0 INCLUS à y EXCLUS (noté [0;y[)

# 				La modification de liste
# 				------------------------
# 				Une liste peut bien évidemment être modifier pour mettre à jour les informations contenues dans la liste. 
# 				On noteras les modifications principales suivantes :
# 					* *Initialisation de liste* : L’initialisation d’une variable de type liste peut être effectuée de plusieurs manières : 
# 				        * **L’initialisation à vide** se fait selon la syntaxe suivante : **l=[]**
# 					    * **L’initialisation avec une valeur par default** : **l=[0]*256** : La liste est initialisée avec une suite de 256 zéros
# 					    * **L’initialisation avec multiples valeurs** : **l=[1,2,3,4]** : La liste est initialisée avec les valeurs 1, 2, 3 et 4
# 					    * **L’initialisation par compréhension de liste** est réalisé selon une syntaxe spéciale : On utilise les crochets pour définir une loi nous permettant de remplir automatiquement la liste avec la longueur désirée. Le premier élément entre crochets est l’opération mathématiques définissant la suite calculée, le second élément défini l’indice de suite et la longueur de la liste. Par exemple pour une liste des carrés d’entiers jusqu’à 10 on écrira : **l=[ x**2 for x in range(0,10)]** éuivaut à **[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]**
# 					* *Extension de liste*
# 						* **Simple** : L’extension de liste simple se fait via la commande append().Lors de l’extension de liste, tous les éléments contenus dans la liste ne sont pas forcement de même type. Il est toutefois recommandé de standardiser le type de data qu’on traite dans un programme, par conséquent les listes à types multiples doivent être utilisé à bon escient et être évitées quand c’est possible. La syntaxe est la suivante :
# 						* **Multiple** : L’extension de liste avec de multiples éléments se fait via la commande extend(). Le paramètre attendu est également une liste, la méthode extend va concaténer la liste passée en argument à l’objet liste actuel. La syntaxe est la suivante :
# 					* *opérations courantes*
# 						* **Length** : La longueur d’une liste peut être obtenue en utilisant la méthode len() retournant la valeur entière de longueur de liste. La méthode len() est utilisée selon la syntaxe suivante : **len(l)**
# 						* **Reverse** : La liste inverse peut être obtenue via la commande reverse() retournant la liste contenant les éléments inversés. La syntaxe est la suivante : **l.reverse()**
# 						* **Duplication** : La duplication de liste s’effectue selon la syntaxe suivante : **duplicate=l[:]**  (Littéralement : l ]-inf;+inf[)


# 				Le test d’appartenance à une liste est réalisé via le mot clé in.

# 				Examples
# 				--------
# 				>>> Exemple : Extraction d'éléments
# 				>>> test=[1,2,3,1,2,3,1,2,3]
# 				>>> test[0]
# 				1
# 				>>> test[2:5]
# 				[3, 1, 2]
# 				>>> # Exemple : Extension de liste simple
# 				>>> l=[1,2,3]
# 				>>> l.append(4)
# 				>>> print(l)
# 				[1, 2, 3, 4]
# 				>>> # Exemple : Extension de liste multiple
# 				>>> l=[1,2,3]
# 				>>> l.extend([4,5,6])
# 				>>> print(l)
# 				[1, 2, 3, 4, 5, 6]
# 				>>> # Exemple : Test d'apprtenance
# 				>>> liste=[1,2,3,4]
# 				>>> 2 in liste
# 				True
# 				>>> 5 in liste
# 				False
# 			"""
# 			pass

# 		def Tuples():
# 			"""
# 				Les N-uplets représente un type de donnée constituer de deux ou plus valeurs liées et accessible via indice. 
# 				Le type N-uplet possède un ensemble de méthodes spécifiques. 
# 				Les éléments sont accessibles de la même manière qu’avec une liste. 
# 				Un Tuple possède une taille fixé au départ et peut subir des modification dynamique de structure (ex : size). 
# 				Seuls les éléments indicés sont modifiables.
# 			"""
# 			pass

# 		def Ensembles():
# 			"""
# 				Un ensemble est, par définition, une collection non ordonnée d’éléments. 
# 				L’instanciation d’un set en Python est réalisée via les symboles {}.
# 				A la différence d’un dictionnaire qui associe des paires d’éléments, un ensemble peut contenir une collection non ordonnée d’éléments non corellés.
# 				Python propose une liste de méthodes implémentant l’algèbre de Cantor concernant les ensembles à savoir :
# 					* *l’Inclusion*
# 					* *l'Exclusion*
# 					* *l'Intersection*
# 					* *l'Union*

# 				Le test d’appartenance à un ensemble est réalisé via le mot clé in de manière similaire au test d’appartenance des listes.
# 				La compréhension d’ensemble permet une instanciation automatisé et condensé.

# 				Examples
# 				--------
# 				>>> # L'ensemble des nombres pairs
# 				>>> Pair={ x for x in range(0,10) if x%2==0 }
# 				>>> print(Pair)
# 				{0, 2, 4, 6, 8}

# 			"""
# 			pass

# 		def Dictionnaires():
# 			"""
# 				Le dictionnaire (dictionnary en Python) représente un type de donnée liant à des clés des valeurs.
# 				A chaque clé du dictionnaire est associée une valeur de type indépendant auquel on accède en utilisant la clé comme indice.
# 				L’initialisation est réalisée via {} et peut être instancié avec un ou des couples clé,valeur.
# 				Le type dictionnaire possède des fonctions natives similaires aux listes telles que append, extend qui ont les mêmes propriétés d’extension de champs qu’avec les listes.
# 				De la même manière un dictionnaire peut être instancié via la compréhension de dict similaire aux listes.


# 				Le parcours de dictionnaire peut être optimisé en utilisant une paire d’indice dans une boucle for.
# 				En reprenant l’exemple précédent on obtient par exemple.

# 				Examples
# 				--------
# 				>>> # Exemple : Assignation de dictionnaire par compréhension
# 				>>> d={ x:x**2 for x in (3,6,9,12,15,18,21,24,27,30)}
# 				>>> print(d)
# 				{3: 9, 6: 36, 9: 81, 12: 144, 15: 225, 18: 324, 21: 441, 24: 576, 27: 729, 30: 900}
# 				>>> # Exemple : Parcours de Dictionnaire
# 				>>> for k,l in d.items():
# 				...     if (l == k*k):
# 				...             print(str(k)+"*"+str(k)+"="+str(l)+" : la propriété est vérifiée")
# 				... 
# 				3*3=9 : la propriété est vérifiée
# 				6*6=36 : la propriété est vérifiée
# 				9*9=81 : la propriété est vérifiée
# 				12*12=144 : la propriété est vérifiée
# 				15*15=225 : la propriété est vérifiée
# 				18*18=324 : la propriété est vérifiée
# 				21*21=441 : la propriété est vérifiée
# 				24*24=576 : la propriété est vérifiée
# 				27*27=729 : la propriété est vérifiée
# 				30*30=900 : la propriété est vérifiée

# 			"""
# 			pass

# 	class Operateurs:
# 		def __init__():
# 			pass

# 		def Operateurs_Arithmetiques():
# 			"""
# 				En Python les opérateurs arithmétiques sont similaires à ceux déjà rencontrés dans d’autres langages. Prenons le temps de les identifier et d’analyser leur caractéristique.
# 				Tout d’abord les opérateurs arithmétiques en Python sont soumis à un **ordre de priorité** respectant la priorité mathématiques des opérations :
# 				()  < ** < * / % < + - 
# 				Ils s’utilisent le plus naturellement du monde en reprenant la syntaxe mathématique courante.

# 				Examples
# 				--------
# 				>>> x=10
# 				>>> 3*x**2+5*x+(10+5)
# 				365

# 				Nous allons décomposer l’ordre d’exécution des opérations sous Python en représentation mémoire
# 					* (10+5) = 15 L’expression est évaluée puis substituée par sa valeur : 3*x**2+5*x+15
# 					* x**2=100 L’expression est évaluée puis substituée par sa valeur : 3*100+5*x+15
# 					* 3*100=300 5*10=50. Les expressions sont calculées : 300+50+15
# 					* La somme finale est évaluée puis substituée par sa valeurs : 365

# 			"""
# 			pass

# 		def Operateurs_De_Comparaison():
# 			"""
# 				Les opérateurs de comparaison ne sont pas soumis à un ordre de priorité. Ils s’utilisent couramment avec les opérateurs logiques.
# 				Ils sont répertorié comme suit :
# 					* *==* : il s’agit du test d’égalité rigoureuse de contenu des variables
# 					* *!=* : il s’agit du test de différence de contenu des variables
# 					* *>*  : Il s’agit du test de supériorité numérique strict
# 					* *≥*  : Il s’agit du test de supériorité ou d’égalité numérique  
# 					* *<*  : Il s’agit du test d’infériorité numérique strict
# 					* *≤*  : Il s’agit du test d’infériorité ou d’égalité numérique
# 					* *in* : Il s’agit du test d’appartenance
# 					* *is* : Il s’agit du test d’égalité d’ Id (égal à True quand les deux variables pointent la même adresse mémoire)

# 			"""
# 			pass

# 		def Operateurs_Logiques():
# 			"""
# 				Les opérateurs logiques sont défini par les symboles suivants :
# 					* *&*   : Il s’agit de l’opérateur and bit à bit
# 					* *^*   : Il s’agit de l’opérateur ou exclusif bit à bit
# 					* *|*   : Il s’agit de l’opérateur ou bit à bit
# 					* *not* : Il s’agit de la négation booléenne (à placer devant une expression) 
# 					* *and* : Il s’agit du ET booléen reliant deux expressions (évalué à True si et seulement si les deux expressions sont évaluées à True) 
# 					* *or*  : Il s’agit du OU booléen reliant deux expressions (évalué à True si et seulement si l’une ou les deux expressions sont évaluées à True)
# 			"""
# 			pass

# 	class Chargement_Sauvegarde_De_Donnees:
# 		def __init__():
# 			pass

# 		def Charger_Des_Donnees():
# 			"""
# 				Le chargement de donnée se fait via un lecteur de fichier. Le lecteur de fichier est instancié par la méthode native « open(path,o) » où path est le chemin vers le fichier à lire et o l’option gérant les droits d’accès au fichiers (lecture, écriture,...) . 
# 				Le contenu est enregistré dans la variable file, instanciée selon la syntaxe suivante :
				
# 				**file = open(path,’r’)**
				
# 				Afin d’accéder au contenu du fichier, on passe par les méthodes read et readlines.

# 				Examples
# 				--------
# 				>>> file=open('./test.txt')
# 				>>> content=file.read()
# 				>>> print(content)
# 				ceci
# 				est un
# 				fichier
# 				exemple sur 
# 				plusieurs lignes

# 				Le contenu est alors interprétable dans Python. 
# 				Le type de résultat d’une lecture de fichier est par convention une chaîne de caractère qu’on peut réinterpréter via Transtypage afin de récupérer les valeurs par exemple.
# 			"""
# 			pass

# 		def Exporter_Des_Donnees():
# 			"""
# 				L’exportation de données est calquée sur la lecture.
# 				On commence par instancier un fichier de sortie avec les droits en écriture : 
				
# 				**file_out=open(path,’w’)**
				
# 				Puis à partir d’un contenu déjà existant on peut écrire dans le fichiers en respectant la syntaxe suivante : 

# 				Examples
# 				--------
# 				>>> content='Ceci est un contenu exemple de fichier'
# 				>>> file_out=open('./test.txt','w')
# 				>>> for item in content:
# 				...     file_out.write(item)
# 				... 

# 				Le contenu est alors recopié à la suite du fichier ouvert. 
# 				Les types accessibles en écriture sous Python sont l’ensemble des formats textes éditables (csv,json,odt,excel, txt,…).
# 			"""
# 			pass

# 	def Conditions():
# 		"""
# 			Le test de condition fait parti des **structures de contrôle** du code Python. 
# 			Il s’agit de mots clés du langage **immuables** permettant de réaliser des embranchements dans la liste d’exécution des instructions.
# 			Le test de condition s’effectue en Python via les mots clés if, then, else et elif. 
# 			La syntaxe de la commande est définie par ces quelques règles :
# 			    * Un test de condition commence toujours par le mot clé if suivit de la condition et de deux points. La syntaxe est la suivante :
# 			        **if (condition) :**
# 			        	**instruction**
			              
# 			        où condition est un test à valeur booléenne **fixe** (True ou False ).
# 			        L’action de instruction est effectuée si et seulement si la condition est vérifiée (le test a valeur booléenne True)
# 			    * Un test de conditions peut avoir plusieurs issues que l’on peut paramétrer. La syntaxe est la suivante :
# 					**if (condition) :**
# 						**instruction1**
# 					**else :**
# 						**instruction2**
# 					où condition est un test à valeur booléenne FIXE (True ou False ).
# 					L’action de instruction1 est effectuée si et seulement si la condition est vérifiée (le test a valeur booléenne True) sinon c’est instruction2 qui est exécutée.
# 			    * Le test de conditions multiples est une extension naturelle du test de condition. On peut imbriqué des tests conditionnels les uns dans les autres, ainsi le code suivant :
# 					**if (condition1) :**
# 						**instruction1**
# 					**else :**
# 						**if (condition2) :**
# 							**instruction2**
# 						**else :**
# 							**instruction3**
# 					Peut être remplacé par le code suivant :
# 					**if (condition1) :**
# 						**instruction1**
# 					**elif (condition2) :**
# 						**instruction2**
# 					**else :**
# 						**instruction3**
# 					Où elif est une contraction des mots clés else et if permettant un test conditionnel aiguillé par les différentes conditions. Instruction1 est exécutée si et seulement si condition1 est vérifiée ; dans le cas contraire, condition2 est évaluée et ainsi de suite. On peut imbriquer des tests conditionnels sans limites de syntaxe.	
# 		"""

# 	def Boucles():
# 		"""
# 			L’utilisation des boucles est un **incontournable** dans la programmation. 
# 			En effet afin d’automatiser une ou plusieurs instructions un nombre de fois déterminé et/ou selon une condition prédéterminé on passe par les structures de contrôles de boucles. 
# 			Les boucles sont réalisables en Python selon deux mots clés principaux : 
# 				* while
# 				* for

# 			La boucle While
# 			---------------

# 			La boucle while est un format de boucle prenant en paramètre une condition booléenne évaluée à chaque tour de boucle. 
# 			Elle détermine la fin de la boucle, en effet quand la condition est vérifiée, la boucle s’arrête et on passe à l’instruction suivante. 
# 			Tant que la condition n’est pas vérifiée, on exécute le corps de la boucle autant de fois que nécessaire.


# 			La boucle For
# 			-------------

# 			La boucle for peut être considérée comme une version de la boucle while étudiée pour les variables incrémentales. 
# 			Elle est constituée d’une variable incrémentée ou décrémentée et d’un seuil déterminant la fin de la boucle. 
# 			En Python, la fonction native range() permet de dresser une liste automatique d’entiers croissants qu’on peut parcourir avec a variable incrémentale i.

# 			La boucle for n’est pas réservée aux boucles incrémentales indicées mais peut être utilisée pour parcourir d’autres types de données tels que les chaînes de caractères, les listes et structures, etc

# 			Examples
# 			--------
# 			>>> # Exemple : Boucle While
# 			>>> n=0
# 			>>> m=10
# 			>>> while(n!=m):
# 			...     n+=1
# 			... 
# 			>>> # Exemple : Boucle For
# 			>>> res=[]
# 			>>> for i in range(0,10):
# 			...     res.append(i*i)
# 			... 
# 			>>> # Exemple : Utilisation de boucle for
# 			>>> test="Ceci est une chaine de caractère"
# 			>>> res=[]
# 			>>> for item in test:
# 			...     res.append(item)
# 			... 
# 			>>> print(res)
# 			['C', 'e', 'c', 'i', ' ', 'e', 's', 't', ' ', 'u', 'n', 'e', ' ', 'c', 'h', 'a', 'i', 'n', 'e', ' ', 'd', 'e', ' ', 'c', 'a', 'r', 'a', 'c', 't', 'è', 'r', 'e']
# 			>>> tmp=""
# 			>>> for item in res:
# 			...     tmp+=item
# 			... 
# 			>>> print(tmp)
# 			Ceci est une chaine de caractère


# 		"""

# 	def Fonctions():
# 		"""
# 			Une fonction est définie en Python par le mot clé **def**.
# 			La syntaxe est la suivante :

# 			**def nom_de_la_fonction(argument1 , argument 2 , … argument N) :**
# 				**Corps_De_La_Fonction**

# 			où :
# 				* Le nom de la fonction est défini par le programmeur
# 				* Les arguments constituent le passage de valeurs à l’appel de la fonction
# 				* Le corps de la fonction représente la s séquence d’instructions définissant la fonction

# 			Dans une fonction en Python, si une variable est passée en argument, sa valeur est recopiée **localement** en mémoire . 
# 			Par conséquent toute modification de sa valeur dans le corps de la fonction ne modifiera pas sa valeur dans son contexte d’origine.
# 			De la même manière une variable déclarée localement dans le corps de la fonction n’existe que dans le contexte de définition de la fonction.
# 			Le retour de valeur permet de récupérer un ou des résultats issus de l’algorithme implémenté dans la fonction. 
# 			Le mot clé return est alors utilisé pour retourner le contenu de la variable spécifiée en argument de return.

# 			Une fonction peut être déclarée au sein d’une fonction : on parle de *définition locale*. 
# 			Dans ce cas la fonction définie localement ne peut être utilisé que dans le corps de la fonction d’ordre supérieure.

# 			En Python, le polymorphisme est implémenté. 
# 			Il s’agit de redéfinition de fonctions selon le type d’appel (valeurs de types différents, nombre de valeurs variables, etc).
# 			Le polymorphisme est défini dés la définition de fonction. 
# 			En effet, l’absence de type des arguments permet une définition multiples selon le type (qu’on recoupera en utilisant la fonction native (isinstance()).
# 			Le nombre variables d’arguments est défini par la syntaxe (**arg) ou **arg représente une liste de longueur variable d’arguments qu’on parcourra avec une boucle for.	

# 			Examples
# 			--------
# 			>>> def Poly_sum(*arg):
# 			...     res=0.0
# 			...     for i in arg:
# 			...             res+=i
# 			...     return res
# 			... 
# 			>>> Poly_sum(5.1,18.2,0.2)
# 			23.499999999999996

# 		"""

# 	class Manipulation_De_Donnees_Avec_Pandas:
# 		def __init():
# 			pass

# 		def Structures():
# 			pass

# 		def Selection_Serie_Et_Dataframes():
# 			pass

# 		def Renommage_Des_Colonnes():
# 			pass

# 		def Filtrage():
# 			pass

# 		def Valeurs_Manquantes():
# 			pass

# 		def Suppression():
# 			pass

# 		def Remplacement_De_Valeurs():
# 			pass

# 		def Ajout_De_Valeurs():
# 			pass

# 		def Retrait_Des_Valeurs_Dupliquees():
# 			pass

# 		def Operations():
# 			pass

# 		def Exportation_Importation_De_Donnees():
# 			pass

# 	class Visualisation_De_Donnees:
# 		def __init__():
# 			pass

# 		def Graphiques_Avec_Matplotlib():
# 			pass

# 		def Graphiques_Avec_Seaborn():
# 			pass


