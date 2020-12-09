
def Concatenation():
	"""
		La concaténation de chaîne de caractère est réalisée par l’opérateur +. 

		La concaténation est l’opération de liaison de deux variables de type Str A et B indépendantes l’une de l’autre. Elle est donc définie par A + B .

		Il s’agit de concaténer deux variables de type str, sans quoi la concaténation générera un message d’erreur.

		Examples
		--------
		>>> a="Je m'appelle "
		>>> b="Arthur"
		>>> c=a+b
		>>> print(c+" et j'ai plus de "+str(250)+" ans.")
		Je m'appelle Arthur et j'ai plus de 250 ans.

	"""
	pass

def Indexation_Extraction():
	"""
		L’indexation des chaînes de caractères en Python est réalisée par le biais des symboles [] accolés au nom de la variable.
		
		L’extraction d’une sous-chaine de caractères est réalisée en utilisant les mêmes symboles et en utilisant l’index de début de chaîne inclus et l’index de fin de chaîne exclus séparés par le symbole : .
	
		Examples
		--------
		>>> # Exemple : Indexation
		>>> test="blablabla"
		>>> test[0]
		'b'
		>>> # Exemple : Extraction
		>>> test="blablabla"
		>>> test[2:5]
		'abl'

	"""
	pass

def Conversion_Majuscules_Minuscules():
	"""
		La conversion de chaine de caractères en majuscules ou en minuscules s'effectue via deux méthodes natives Python :
			* **lower** : La méthode permet de convertir l'intégralité d'une chaine de caractères en minuscules.
			* **upper** : La méthode permet de convertir l'intégralité d'une chaine de caractères en majuscules.
			
		La méthode est associée à l'objet String, par conséquent sa syntaxe d'appel est la suivante :

		**MyString.lower()**

		**MyString.upper()**

		Examples
		--------
		>>> test="un truc comme CA"
		>>> test.lower()
		'un truc comme ca'
		>>> test.upper()
		'UN TRUC COMME CA'

	"""
	pass

def Recherche_De_Chaines():
	"""
		Afin de rechercher une sous-chaine de caractères dans une chaîne de caractères existante on utilise le mot clé **in** en plaçant la sous-chaine à rechercher comme premier opérande et la chaîne principale comme deuxième opérande.
		
		Le résultat du test est égal à la valeur booléenne « True » si la sous chaîne est présent, False sinon.

		Examples
		--------
		>>> test="blablabla"
		>>> "bla" in test
		True
		>>> "cla" in test
		False				
	"""
	pass

def Decoupage_De_Sous_Chaines():
	"""
		Afin de découper en sous chaîne une chaîne de caractère instancié, on peut utiliser plusieurs méthodes :
			* la méthode de l’indexage et de l’extraction. En effet, en extrayant des tronçons de mêmes taille, on découpe la chaîne aisément.
			* la méthode native split à laquelle on passe en argument un séparateur de sous-chaine.

		Examples
		--------
		>>> # Exemple : Decoupage de sous-chaines par extraction
		>>> test="blablabla"
		>>> splitted=[]
		>>> splitted.append(test[0:3])
		>>> splitted.append(test[3:6])
		>>> splitted.append(test[6:9])
		>>> print(splitted)
		['bla', 'bla', 'bla']
		>>> # Exemple : Utilisation de la méthode split
		>>> test="bla,bla,bla"
		>>> splitted=test.split(',')
		>>> print(splitted)
		['bla', 'bla', 'bla']

	"""

	pass

def Nettoyage_Completion():
	"""
		Le nettoyage ou la complétion d’une chaîne de caractère peut être réalisé en effectuant des remplacement de caractères et des suppression (par exemple suppression des caractères \\n, remplacement des Majuscule par des minuscules, etc).
		
		Il existe un nombre important d’opérateurs de chaînes de caractères en Python, dont la documentation détaillée est disponible sur le site officiel de documentation de Python.
		Par exemple, la suppression des caractère de saut de lignes dans le contenu d’un fichier sous forme de chaîne de caractères est réalisé par le code suivant.

		Examples
		--------
		>>> res=""                           # Le résultat instancié de type Str
		>>> file=open("./test.txt")          # Le fichier est ouvert
		>>> content=file.read()              # On lit le contenu du fichier
		>>> for item in content:
		...     if (item != "\\n"):
		...             res+=" "+item        # On reconstruit le contenu du fichier
		... 
		>>> print(res)
		 c e c i e s t   u n f i c h i e r e x e m p l e   s u r   p l u s i e u r s   l i g n e s

	"""
	pass

def Conversion_En_Chaine_De_Caracteres():
	"""
		La conversion de la valeur d’une variable en chaîne de caractères est toujours possible. 
		On utilisera l’opérateur de trans-typage str() en donnant comme argument la variable à convertir.
	
		Examples
		--------
		>>> test=123.456
		>>> type(test)
		<class 'float'>
		>>> str(test)
		'123.456'
		>>> type(test)
		<class 'float'>
		>>> type(str(test))
		<class 'str'>

		La variable convertie n’est plus utilisable dans son contexte d’origine : une variable Float convertie en Str **ne pourra pas** être réutilisée telle quelle dans une opération mathématiques.
		La conversion inverse est nécessaire (cf Conversion).

	"""
	pass
