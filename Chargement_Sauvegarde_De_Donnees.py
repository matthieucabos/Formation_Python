
def Charger_Des_Donnees():
	"""
		Le chargement de donnée se fait via un lecteur de fichier. 

		Le lecteur de fichier est instancié par la méthode native **open(path,o)** où path est le chemin vers le fichier à lire et o l’option gérant les droits d’accès au fichiers (lecture, écriture,...) . 
		
		Le contenu est enregistré dans la variable file, instanciée selon la syntaxe suivante :
		
		**file = open(path,’r’)**
		
		Afin d’accéder au contenu du fichier, on passe par les méthodes **read** et **readlines**.

		Examples
		--------
		>>> file=open('./test.txt')
		>>> content=file.read()
		>>> print(content)
		ceci
		est un
		fichier
		exemple sur 
		plusieurs lignes

		Le contenu est alors interprétable dans Python. 
		Le type de résultat d’une lecture de fichier est par convention une chaîne de caractère qu’on peut réinterpréter via Transtypage afin de récupérer les valeurs par exemple.
	"""
	pass

def Exporter_Des_Donnees():
	"""
		L’exportation de données est calquée sur la lecture.
		
		On commence par instancier un fichier de sortie avec les droits en écriture : 
		
		**file_out=open(path,’w’)**
		
		Puis à partir d’un contenu déjà existant on peut écrire dans le fichiers en respectant la syntaxe suivante : 

		Examples
		--------
		>>> content='Ceci est un contenu exemple de fichier'
		>>> file_out=open('./test.txt','w')
		>>> for item in content:
		...     file_out.write(item)
		... 

		Le contenu est alors recopié à la suite du fichier ouvert. 
		Les types accessibles en écriture sous Python sont l’ensemble des formats textes éditables (csv,json,odt,excel, txt,…).
	"""
	pass
