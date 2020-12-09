def Listes():
	"""
		Les listes sont une structure de données native en Python. 

		On peut considérer le type List comme l’extension des types natifs de bases integer, float et str. 

		Le type list est constitué d’un tableau chaîné sur lequel certaines opérations sont permises.

		**L’extraction d’élément**

		Afin d’extraire des informations précises contenues dans une liste, on peut extraire une partie de la liste sous forme de sous-liste ou extraire un élément individuellement grâce à son indice.
		La syntaxe est la suivante.

		Le type du résultat d’une extraction est List, le type  lors de la lecture d’un élément simple est le même que ceux des éléments lors de l’instanciation.
		
		L’extraction indicée est effectuée de la manière suivante :
			* *liste[x:y]* va extraire tout les éléments de x **inclus** à y **exclus** (mathématiquement résumé à [x;y[)
			* *liste[x:]* va extraire tout les éléments de x **inclus** jusqu’à la fin de liste (noté [x,+inf[)
			* *liste[:y]* va extraire tout les éléments de 0 **inclus** à y **exclus** (noté [0;y[)

		**La modification de liste**

		Une liste peut bien évidemment être modifier pour mettre à jour les informations contenues dans la liste. 
		
		On noteras les modifications principales suivantes :
			* *Initialisation de liste* : L’initialisation d’une variable de type liste peut être effectuée de plusieurs manières : 
				* **L’initialisation à vide** se fait selon la syntaxe suivante : **l=[]**
				* **L’initialisation avec une valeur par default** : **l=[0]*256** : La liste est initialisée avec une suite de 256 zéros
				* **L’initialisation avec multiples valeurs** : **l=[1,2,3,4]** : La liste est initialisée avec les valeurs 1, 2, 3 et 4
				* **L’initialisation par compréhension de liste** est réalisé selon une syntaxe spéciale : On utilise les crochets pour définir une loi nous permettant de remplir automatiquement la liste avec la longueur désirée. Le premier élément entre crochets est l’opération mathématiques définissant la suite calculée, le second élément défini l’indice de suite et la longueur de la liste. Par exemple pour une liste des carrés d’entiers jusqu’à 10 on écrira : **[ x**2 for x in range(0,10)]** éuivaut à **[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]**
		
			* *Extension de liste*
				* **Simple** : L’extension de liste simple se fait via la commande **append()**.Lors de l’extension de liste, tous les éléments contenus dans la liste ne sont pas forcement de même type. Il est toutefois recommandé de standardiser le type de data qu’on traite dans un programme, par conséquent les listes à types multiples doivent être utilisé à bon escient et être évitées quand c’est possible. La syntaxe est la suivante : **list.append(item)**
				* **Multiple** : L’extension de liste avec de multiples éléments se fait via la commande **extend()**. Le paramètre attendu est également une liste, la méthode extend va concaténer la liste passée en argument à l’objet liste actuel. La syntaxe est la suivante : list.extend(list_of_items)
		
			* *opérations courantes*
				* **Length** : La longueur d’une liste peut être obtenue en utilisant la méthode **len()** retournant la valeur entière de longueur de liste. La méthode **len()** est utilisée selon la syntaxe suivante : **len(l)**
				* **Reverse** : La liste inverse peut être obtenue via la commande **reverse()** retournant la liste contenant les éléments inversés. La syntaxe est la suivante : **l.reverse()**
				* **Duplication** : La duplication de liste s’effectue selon la syntaxe suivante : **duplicate=l[:]**  (Littéralement : l ]-inf;+inf[)


		Le test d’appartenance à une liste est réalisé via le mot clé in.

		Examples
		--------
		>>> Exemple : Extraction d'éléments
		>>> test=[1,2,3,1,2,3,1,2,3]
		>>> test[0]
		1
		>>> test[2:5]
		[3, 1, 2]
		>>> # Exemple : Extension de liste simple
		>>> l=[1,2,3]
		>>> l.append(4)
		>>> print(l)
		[1, 2, 3, 4]
		>>> # Exemple : Extension de liste multiple
		>>> l=[1,2,3]
		>>> l.extend([4,5,6])
		>>> print(l)
		[1, 2, 3, 4, 5, 6]
		>>> # Exemple : Test d'apprtenance
		>>> liste=[1,2,3,4]
		>>> 2 in liste
		True
		>>> 5 in liste
		False
	"""
	pass

def Tuples():
	"""
		Les N-uplets représente un type de donnée constituer de deux ou plus valeurs liées et accessible via indice. 
		
		Le type N-uplet possède un ensemble de méthodes spécifiques. 
		
		Les éléments sont accessibles de la même manière qu’avec une liste. 
		
		Un Tuple possède une taille fixé au départ et peut subir des modification dynamique de structure (ex : **size**). 
		
		Seuls les éléments indicés sont modifiables.
	"""
	pass

def Ensembles():
	"""
		Un ensemble est, par définition, une collection non ordonnée d’éléments. 
		L’instanciation d’un set en Python est réalisée via les symboles **{}**.
		
		A la différence d’un dictionnaire qui associe des paires d’éléments, un ensemble peut contenir une collection non ordonnée d’éléments non corellés.
		
		Python propose une liste de méthodes implémentant l’algèbre de Cantor concernant les ensembles à savoir :
			* *l’Inclusion*
			* *l'Exclusion*
			* *l'Intersection*
			* *l'Union*

		Le test d’appartenance à un ensemble est réalisé via le mot clé in de manière similaire au test d’appartenance des listes.
		La compréhension d’ensemble permet une instanciation automatisé et condensé.

		Examples
		--------
		>>> # L'ensemble des nombres pairs
		>>> Pair={ x for x in range(0,10) if x%2==0 }
		>>> print(Pair)
		{0, 2, 4, 6, 8}

	"""
	pass

def Dictionnaires():
	"""
		Le dictionnaire (dictionnary en Python) représente un type de donnée liant à des clés des valeurs.
		A chaque clé du dictionnaire est associée une valeur de type indépendant auquel on accède en utilisant la clé comme indice.
		
		L’initialisation est réalisée via **{}** et peut être instancié avec un ou des couples clé,valeur.
		
		Le type dictionnaire possède des fonctions natives similaires aux listes telles que **append**, **extend** qui ont les mêmes propriétés d’extension de champs qu’avec les listes.
		
		De la même manière un dictionnaire peut être instancié via la compréhension de **dict** similaire aux listes.


		Le parcours de dictionnaire peut être optimisé en utilisant une paire d’indice dans une boucle **for**.
		En reprenant l’exemple précédent on obtient par exemple.

		Examples
		--------
		>>> # Exemple : Assignation de dictionnaire par compréhension
		>>> d={ x:x**2 for x in (3,6,9,12,15,18,21,24,27,30)}
		>>> print(d)
		{3: 9, 6: 36, 9: 81, 12: 144, 15: 225, 18: 324, 21: 441, 24: 576, 27: 729, 30: 900}
		>>> # Exemple : Parcours de Dictionnaire
		>>> for k,l in d.items():
		...     if (l == k*k):
		...             print(str(k)+"*"+str(k)+"="+str(l)+" : la propriété est vérifiée")
		... 
		3*3=9 : la propriété est vérifiée
		6*6=36 : la propriété est vérifiée
		9*9=81 : la propriété est vérifiée
		12*12=144 : la propriété est vérifiée
		15*15=225 : la propriété est vérifiée
		18*18=324 : la propriété est vérifiée
		21*21=441 : la propriété est vérifiée
		24*24=576 : la propriété est vérifiée
		27*27=729 : la propriété est vérifiée
		30*30=900 : la propriété est vérifiée

	"""
	pass
