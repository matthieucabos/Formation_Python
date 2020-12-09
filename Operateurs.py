
def Operateurs_Arithmetiques():
	"""
		En Python les opérateurs arithmétiques sont similaires à ceux déjà rencontrés dans d’autres langages. 

		Prenons le temps de les identifier et d’analyser leurs caractéristiques.

		Tout d’abord les opérateurs arithmétiques en Python sont soumis à un **ordre de priorité** respectant la priorité mathématiques des opérations :

		**()  < ** < * / % < + -** 

		Ils s’utilisent le plus naturellement du monde en reprenant la syntaxe mathématique courante.

		Examples
		--------
		>>> x=10
		>>> 3*x**2+5*x+(10+5)
		365

		Nous allons décomposer l’ordre d’exécution des opérations sous Python en représentation mémoire
			* **(10+5) = 15** L’expression est évaluée puis substituée par sa valeur : 3*x**2+5*x+ **15**
			* **x**2=100** L’expression est évaluée puis substituée par sa valeur : 3* **100** +5*x+15
			* **3*100=300** **5*10=50**. Les expressions sont calculées : **300** + **50** +15
			* La somme finale est évaluée puis substituée par sa valeurs : **365**

	"""
	pass

def Operateurs_De_Comparaison():
	"""
		Les opérateurs de comparaison ne sont pas soumis à un ordre de priorité. 

		Ils s’utilisent couramment avec les opérateurs logiques.
		
		Ils sont répertorié comme suit :
			* **==** : il s’agit du test d’ **égalité rigoureuse** de contenu des variables

			* **!=** : il s’agit du test de **différence** de contenu des variables

			* **>**  : Il s’agit du test de **supériorité numérique strict**

			* **>=**  : Il s’agit du test de **supériorité ou d’égalité numérique**  

			* **<**  : Il s’agit du test d’ **infériorité numérique strict**

			* **<=**  : Il s’agit du test d’ **infériorité ou d’égalité numérique**

			* **in** : Il s’agit du test d’ **appartenance**

			* **is** : Il s’agit du test d’ **égalité d’ Id** (égal à **True** quand les **deux variables pointent la même adresse mémoire**)

	"""
	pass

def Operateurs_Logiques():
	"""
		Les opérateurs logiques sont défini par les symboles suivants :
			* **&**   : Il s’agit de l’opérateur **And** bit à bit
			* **^**   : Il s’agit de l’opérateur **Ou exclusif** bit à bit
			* **|**   : Il s’agit de l’opérateur **Ou** bit à bit
			* **not** : Il s’agit de la **Négation booléenne** (à placer devant une expression) 
			* **and** : Il s’agit du **Et booléen** reliant deux expressions (évalué à **True** si et seulement si les deux expressions sont évaluées à **True**) 
			* **or**  : Il s’agit du **Ou booléen** reliant deux expressions (évalué à **True** si et seulement si l’une ou les deux expressions sont évaluées à **True**)
	"""
	pass
