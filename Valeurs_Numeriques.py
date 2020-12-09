def Entiers():
	"""
		Les Integer sont monnaie courante en programmation : compteur, index, etc
		Ils représentent l’ensemble des entiers naturels N.

		En Python l’instanciation d’une variable peut se faire à n’importe quel endroit du code. 
		L’assignation défini le type de la variable. 
		Une variable integer sera donc instanciée en utilisant la syntaxe suivante :
		
		**x=0**
		
		où x est le nom de la variable et 0 la valeur instanciée. 

		Étant donné que la valeur 0 est considérée comme integer, la variable sera instancié de type integer. Python passe par une déclaration implicite des types.
		
		L’ensemble des opérations définies avec les Integer est répertorié dans la documentation officielle de Python.
	"""
	pass

def Nombres_A_Virgules_Flottante():
	"""
		Les Nombre à virgules flottante (ou Float en anglais) représentent l’ensemble des réels R.
		Ce sont les variables les plus gourmandes en mémoire : attention donc à les utiliser à bon escient.
		
		On les utilisera dans des calculs nécessitant une précision décimale, hors de question d’instancier un compteur ou un index avec une variable flottante.
		
		Les opérations natives sont héritées du type integer et regroupe l’ensemble des opérateurs usuels de maths.
		
		En Python ils existent les bibliothèques natives numpy et scipy implémentant grand nombre de calculs et lois scientifiques utilisant les nombres flottants.
	"""
	pass

def Nombres_Complexes():
	"""
		Les nombres complexes sont constitués d’une partie réel et imaginaire dont la définition est résumé à la formule suivante.
		Pour tout nombre z appartenant à l’ensemble C des nombres complexes, il existe les nombres a et b appartenant à l’ensemble R des nombres réels tels que z s’exprime par :

		**z = aj + b**

		L’arithmétique des nombres complexes, considérée acquise, ne sera pas abordé dans ce chapitre. 
		Python permet de manipuler aisément ces valeurs via le module intégré cmath.
		
		L’instanciation se fait selon la syntaxe suivante :

		**z = aj+b**

		où a et j sont deux réels définis par l’utilisateur.
		Les opérations arithmétiques standards ne nécessitent pas l’importation du module cmath. 

		Ainsi l’expression suivante sera correctement interprété depuis la console.

		Examples
		--------
		>>> z=3j+2
		>>> z2=1j+5
		>>> print(z+z2)
		(7+4j)

		Les fonctions évoquées dans ce chapitre sont les suivantes :
		    * *phase* : Il s’agit de calculer la phase d’un nombre polaire z fourni en argument. La syntaxe d’appel est la suivante : **cmath.phase(z)**
		    * *polar* : Il s’agit de calculer les coordonnées polaires d’un nombre complexe z fourni en argument. La syntaxe d’appel est la suivante : **cmath.polar(z)**
		    * *rect* : Il s’agit de calculer les coordonnées rectangulaire d’un nombre complexe sous forme polaire déterminé par ses coefficient r et phi ou phi est la phase du nombre complexe et r le module du nombre complexe. La syntaxe d’appel est la suivante : **cmath.rect(r,phi)**

	"""
	pass

def Conversions():
	"""
		Les conversions de types sont très largement utilisées en python, on parle de Transtypage.
		Le trans-typage est utilisé dans presque tous les langages informatiques typés. 
		
		Il s’agit d’une opération de base permettant de convertir la valeur d’une variable typée vers la valeur la représentant dans un autre type.
		
		Par exemple un coefficient entier utilisé dans une opération flottante sera implicitement convertie dans sa valeur flottante correspondante. 

		De la même manière une valeur flottante saura être tronquée à la virgule lors d’un conversion integer.
	
		Examples
		--------
		>>> x=10      # x est de type integer
		>>> y=float(x)
		>>> print(y)  # y est maintenant de type float
		10.0
		>>> print("J'espère avoir au moins "+str(y)+" de moyenne au cours Python cette année !")
		J'espère avoir au moins 10.0 de moyenne au cours Python cette année !
		>>>           # La variable transtypée str(y) est maintenant de type Str

	"""
	pass

def Booleens():
	"""
		L’algèbre de Boole définie les standard de la logique informatique. 
		Il est impensable pour un langage de ne pas implémenter les valeurs booléennes et leurs opérateurs associés.
		
		Une variable booléenne a pour valeur True ou False, implémentée en utilisant des Integer, la notation est parfois simplifiée par les valeurs 1 et 0 représentant respectivement les valeurs True et False.
	
		Les opérateurs courant sont :
			* *Logic And*: Réalise le Et logique entre deux booléens            (noté A and B)
			* *Logic Or*: Réalise le Ou logique entre deux booléens             (noté A or B)
			* *Logic Not* : Réalise le Non Logique d’une valeur booléenne       (noté not A)
			* *Logic Nand* : Réalise Le Non logique du résultat d’un Et logique (noté not ( A and B ))
			* *Logic Nor* : Réalise le Non logique d’un Ou logique              (noté not ( A or B ))

		Les autres opérateurs et lois booléennes sont dérivées de l’utilisation de ces opérateurs de base.
	"""
	pass

def ObjetVide():
	"""
		L’objet vide est dénommé None et représente l’absence de valeur dans une variable. 
		
		Il est par définition non-typé et peut s’utiliser en comparaison de n’importe quel type.
	
		Examples
		--------
		>>> import random
		>>> tab=[]
		>>> for i in range(0,10):
		...     tab.append(random.randint(0,100))
		... 
		>>> tab.append(None)
		>>> i=0
		>>> while(tab[i]!=None):
		...     print(tab[i])
		...     i+=1
		... 
		100
		70
		25
		38
		42
		35
		74
		85
		98
		10

	"""
	pass

def Date_Et_Temps():
	"""
		Le module datetime de Python nous sert à récupérer des informations concernant la date et l’heure depuis les informations système.
		
		Il possède des méthodes natives dont on étudiera uniquement les principales : 
		    * *date* : Permet de récupérer la date au format standardisé
		    * *time* : Permet de récupérer l’heure au format standardisé
		    * *datetime* : Permet de récupérer la date et l’heure au format standardisé
	
		Les données datetime sont de même type et donc les opérations d’addition, de soustraction, multiplication, division et modulo sont disponibles ainsi que les méthodes abs(), str() et repr().

	"""
	pass
