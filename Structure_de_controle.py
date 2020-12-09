def Conditions():
	"""
		Le test de condition fait parti des **structures de contrôle** du code Python. 
		Il s’agit de mots clés du langage **immuables** permettant de réaliser des embranchements dans la liste d’exécution des instructions.
		Le test de condition s’effectue en Python via les mots clés if, then, else et elif. 
		
		La syntaxe de la commande est définie par ces quelques règles :
			* Un test de condition commence toujours par le mot clé if suivit de la condition et de deux points.
				.. highlight:: python
   				.. code-block:: python

					if (condition) :
						instruction

				où condition est un test à valeur booléenne **fixe** (**True** ou **False** ).
				L’action de instruction est effectuée si et seulement si la condition est vérifiée (le test a valeur booléenne **True**)

			* Un test de conditions peut avoir plusieurs issues que l’on peut paramétrer.
				.. highlight:: python
   				.. code-block:: python

					if (condition) :
						instruction1
					else :
						instruction2

				où condition est un test à valeur booléenne **fixe** (**True** ou **False** ).
				L’action de instruction1 est effectuée si et seulement si la condition est vérifiée (le test a valeur booléenne **True**) sinon c’est instruction2 qui est exécutée.

			* Le test de conditions multiples est une extension naturelle du test de condition. On peut imbriquer des tests.
				.. highlight:: python
   				.. code-block:: python

					if (condition1) :
						instruction1
					else :
						if (condition2) :
							instruction2
						else :
							instruction3

				peut être remplacé par le code suivant :

				.. highlight:: python
   				.. code-block:: python

					if (condition1) :
						instruction1
					elif (condition2) :
						instruction2
					else :
						instruction3

				Où elif est une contraction des mots clés else et if permettant un test conditionnel aiguillé par les différentes conditions. Instruction1 est exécutée si et seulement si condition1 est vérifiée ; dans le cas contraire, condition2 est évaluée et ainsi de suite. On peut imbriquer des tests conditionnels sans limites de syntaxe.	

	"""

def Boucles():
	"""
		L’utilisation des boucles est un **incontournable** dans la programmation. 
		En effet afin d’automatiser une ou plusieurs instructions un nombre de fois déterminé et/ou selon une condition prédéterminé on passe par les structures de contrôles de boucles. 
		
		Les boucles sont réalisables en Python selon deux mots clés principaux : 
			* **while**

			* **for**

		**La boucle While**

		La boucle **while** est un format de boucle prenant en paramètre une condition booléenne évaluée à chaque tour de boucle. 
		Elle détermine la fin de la boucle, en effet quand la condition est vérifiée, la boucle s’arrête et on passe à l’instruction suivante. 
		Tant que la condition n’est pas vérifiée, on exécute le corps de la boucle autant de fois que nécessaire.


		**La boucle For**

		La boucle **for** peut être considérée comme une version de la boucle **while** étudiée pour les variables incrémentales. 
		Elle est constituée d’une variable incrémentée ou décrémentée et d’un seuil déterminant la fin de la boucle. 
		En Python, la fonction native **range()** permet de dresser une liste automatique d’entiers croissants qu’on peut parcourir avec a variable incrémentale i.

		La boucle **for** n’est pas réservée aux boucles incrémentales indicées mais peut être utilisée pour parcourir d’autres types de données tels que les chaînes de caractères, les listes et structures, etc

		Examples
		--------
		>>> # Exemple : Boucle While
		>>> n=0
		>>> m=10
		>>> while(n!=m):
		...     n+=1
		... 
		>>> # Exemple : Boucle For
		>>> res=[]
		>>> for i in range(0,10):
		...     res.append(i*i)
		... 
		>>> # Exemple : Utilisation de boucle for
		>>> test="Ceci est une chaine de caractère"
		>>> res=[]
		>>> for item in test:
		...     res.append(item)
		... 
		>>> print(res)
		['C', 'e', 'c', 'i', ' ', 'e', 's', 't', ' ', 'u', 'n', 'e', ' ', 'c', 'h', 'a', 'i', 'n', 'e', ' ', 'd', 'e', ' ', 'c', 'a', 'r', 'a', 'c', 't', 'è', 'r', 'e']
		>>> tmp=""
		>>> for item in res:
		...     tmp+=item
		... 
		>>> print(tmp)
		Ceci est une chaine de caractère
	"""

def Fonctions():
	"""
		Une fonction est définie en Python par le mot clé **def**.
		La syntaxe est la suivante :

		def nom_de_la_fonction(argument1 , argument 2 , … argument N) :
			Corps_De_La_Fonction

		où :
			* Le **nom de la fonction** est défini par le programmeur

			* Les **arguments** constituent le passage de valeurs à l’appel de la fonction
			
			* Le **corps de la fonction** représente la s séquence d’instructions définissant la fonction

		Dans une fonction en Python, si une variable est passée en argument, sa valeur est recopiée **localement** en mémoire . 
		Par conséquent toute modification de sa valeur dans le corps de la fonction **ne modifiera pas sa valeur dans son contexte d’origine**.
		
		De la même manière une variable déclarée localement dans le corps de la fonction n’existe que dans le contexte de définition de la fonction.
		Le retour de valeur permet de récupérer un ou des résultats issus de l’algorithme implémenté dans la fonction. 
		
		Le mot clé **return** est alors utilisé pour retourner le contenu de la variable spécifiée en argument de return.

		Une fonction peut être déclarée au sein d’une fonction : on parle de *définition locale*. 
		Dans ce cas la fonction définie localement ne peut être utilisé que dans le corps de la fonction d’ordre supérieure.

		En Python, le polymorphisme est implémenté. 
		Il s’agit de redéfinition de fonctions selon le type d’appel (valeurs de types différents, nombre de valeurs variables, etc).
		
		Le polymorphisme est défini dés la définition de fonction. 
		En effet, l’absence de type des arguments permet une définition multiples selon le type (qu’on recoupera en utilisant la fonction native **isinstance()**.
		
		Le nombre variables d’arguments est défini par la syntaxe (**\*arg**) ou **\*arg** représente une liste de longueur variable d’arguments qu’on parcourra avec une boucle for.
		
		Examples
		--------
		>>> def Poly_sum(*arg):
		...     res=0.0
		...     for i in arg:
		...             res+=i
		...     return res
		... 
		>>> Poly_sum(5.1,18.2,0.2)
		23.499999999999996

	"""