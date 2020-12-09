def Structures():
	"""
		Une série est définie par un vecteur de taille variables de valeurs.
		Les types accéptés sont integer, float et les types natifs numpy.
		
		L'instanciation d'une série se fait via la méthode 

		**s=pandas.Series(liste)**

		où liste est une liste de valeurs définnissant le vecteur
		
		La taille de la série peut être obtenu via la méthode redéfinie **len(s)**
		La copie de la serie peut être réalisée via la méthode **s.copy()**
		
		Les valeurs statistiques d'une série sont obtenue via la méthode **s.describe()**
		L'indexation et le tri répondent aux standards Python (cf **liste**)

		Une dataFrame est définie par par un tableau dynamique de valeurs indexées.
		
		La dataframe est instanciée via la méthode **d=pandas.dataframe(content)** où content peut prendre différentes formes :
			* un dictionnaire de la forme :

				**{'nom de champ 1':[v1,v2,v3,...,vn],'nom de champ 2':[v11,v12,v13...]}**

   			 où les nom de champs vont définir les noms de colonnes et où le dernier élément du ditionnaire va définir les noms de ligne

			* un tableau numpy suivi des noms de lignes et de colonnes sous la forme suivantes :
				* **array=numpy.array(l1,l2,l3)**
				* **dataframe=pandas.DataFrame(array,index=['a1','a2','a3'],columns=['A','B','C','D'])**

	"""
	pass

def Selection_Serie_Et_Dataframes():
	"""
		La séléction et le parcours des structures se fait de manière itérative.
		Le parcours par boucle est réalisé avec la syntaxe exemple : 

		L'accés par colonne se fait en spécifiant l'index de colonne :
		**print(df['A'])**

		L'accés aux valeurs est similaire aux liste :
		**print(df['A'][1:3])**

		L'accés par ligne se fait en spécifiant l'indice de ligne :
		**print(df.loc['a2'])**

		L'accés par indices matriciels est réalisé par la syntaxe :
		**print(df.iat[i,j])**

		Examples
		--------

		>>> df=pandas.DataFrame(args)
		>>> s=pandas.Series(arg)
		>>> for item in df :
		... print(item)
		...
		>>> for item in s :
		... print(item)
		...

	"""
	pass

def Renommage_Des_Colonnes():
	"""
		Le rennomage des colonnes se fait via les commandes

		**df.columns=['a','b']**

		ou 

		**df.rename(columns={'A':'a','B':'b'}**

	"""
	pass

def Filtrage():
	"""
		Le filtrage se fait dans Pandas via la méthode associé à l'objet **DataFrame filter**.
		
		La méthode **filter** est utilisé selon la syntaxe suivante.

		Examples
		--------
		>>> df.filter(items=['A','B']) # Filtre par nom de colonne
		>>> df.filter(regex=e$,axis=1) # Filtre par expression régulière
		>>> df.filter(like='a',axis=0) # filtre par appartenance (tout les éléments possédent un a dans le nom))

	"""
	pass

def Valeurs_Manquantes():
	pass

def Suppression():
	pass

def Remplacement_De_Valeurs():
	"""
		La modification des valeurs de la Dataframe peut être réalisée via la méthode **apply** utilisée selon la syntaxe exemple.
		
		On pourra également utiliser la méthode **replace** utilisée comme suit.
	
		Examples
		--------

		>>> df.apply(lambda x: 0 if x!=2 else x) # Littéralemnt remplacement des 2 par des 0
		>>> df.replace(1,5)                      # Littéralement remplacer les 1 par des 5
		>>> df.replace([1,5],[5,7])              # Littéralement une permutation signée (les 1 remplacés par des 5, les 5 remplacés par des 7, ...)	
	"""
	pass

def Ajout_De_Valeurs():
	"""		
		L'ajout de valeurs se fait par instanciation de colonne.
		L'ajout de colonne à une **dataframe** est réalisée via la syntaxe Python native :
		
		**df['E']=pandas.Series([1,0,1],index=['a1','a2','a3'])**
		
		où E est la nouvelle colonne à instancier et les arguments sont respectivement les valeurs suivies des indices de lignes.
	"""
	pass

def Retrait_Des_Valeurs_Dupliquees():
	"""
		Le retrait des valeurs dupliquées se fait via la méthode **drop_duplicates()**
		
		Sans arguments, la fonction supprime les valeurs redondantes, avec l'argument **subset** on définie	les colonnes sur lesquelles la modification va être effectuée. 

	"""
	pass

def Operations():
	"""

		Les opérations implémentées dans Pandas sur les dataframes sont les suivantes :
			* **+** : Addition de dataframes
			* ***** : multiplication de dataframes
			* **/** : Division élement par élément
			* ****** : Carré de chaque élément
			* **df1.eq(df2)** : Test d'égalité
			* **df1.ne(df2)** : Test de différence
			* **df1.lt(df2)** : Test d'infériorité stricte
			* **df1.le(df2)** : Test d'infériorité relative
			* **df1.gt(df2)** : Test de supériorité stricte
			* **df1.ge(df2)** : Test de supériorité relative

		En particulier pour lesdataframes de type booléens on retrouvera les operateurs suivants:
			* **-df** : non logique
			* **df1 & df2** : *ET* logique
			* **df1 | df2** : *OU* logique
			* **df1 ^ df2** : *OU* exclusif
	"""
	pass

def Exportation_Importation_De_Donnees():
	pass
