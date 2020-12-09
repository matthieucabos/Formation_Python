
def Graphiques_Avec_Matplotlib():
	"""
		Matplotlib est une librairie scientifique de traitement graphique de données.

		Ce traitement peut prendre plusieurs formes dont nous etudierons les principales :
			* **Courbes**

			* **Distribution de Points**

			* **Histogramme**

		Pour chaque point du chapitre, nous partirons du principe qu'il existe les vecteurs x et y contenant respectivement des données en abscisse et en ordonnée à traiter.

		De la même manière l'import de module **import matplotlib.pyplot as plt** aura été effectué en en-tête du fichier source


		``Courbes avec MatPlotLib``


		Après identification des vecteurs à traiter, on va instancier un objet de type figure via la commande

		**plt.figure()**

		Afin d'alimenter le graphique, il est necessaire de l'instancier avec les vecteur x et y.
		La syntaxe est la suivante :

		**plt.plot(x,y,color='r',label="label du graphique")**

		On peut :
			* **Ajouter un titre** : on utiliseras la commande **plt.title("Titre du graphique")**
			
			* **Ajouter un label à l'axe des abscisses** : on utiliseras la commande **plt.xlabel("Abscisses")**
			
			* **ajouter un label à l'axe des ordonnées** : on utiliseras la commande **plt.ylabel("Ordonnées")**
			
			* **Ajouter une grille au graphique** : on utiliseras la commande **plt.grid(True)**

		Afin de finaliser l'affichage, on utiliseras les commandes :

		**plt.legend()** : Affiche la ou les légendes spécifiées lors de l'initialisation

		**plt.show()** : Affiche le graphique dans une nouvelle fenêtre

		
		``Distribution de Points avec MatPlotLib``


		En utilisant les vecteurs x et y, on va instancier un objet de type figure via **plt.figure()**.

		Afin d'alimenter la distribution, il est necessaire de l'instancier avec les vecteurs x et y.
		La syntaxe est la sivante :

		**plt.scatter(x,y,label='Label du graphique')**

		La finalisation de l'affichage est effectuée de la même manière qu'avec l'affichage des courbes :

		**plt.legend()** : Affiche la ou les légendes spécifiées lors de l'initialisation

		**plt.show()** : Affiche le graphique dans une nouvelle fenêtre

		
		``Histogrammes avec MatPlotLib``


		En utilisant les mêmes vecteurs data x et y, On va instancier un objet de type figure via **plt.figure()**

		Afin d'alimenter l'histogramme, il est necessaire de l'instancier avec les vecteurs x et y.
		La syntaxe est la suivante :

		**plt.hist(x,y,normed=True,label='Label du graphique')**

		Ici, l'argument **normed** permet de normaliser l'histogramme (non indispensable)

		La finalisation de l'affichage est effectuée de la même manière qu'avec l'affichage des courbes :

		**plt.legend()** : Affiche la ou les légendes spécifiées lors de l'initialisation

		**plt.show()** : Affiche le graphique dans une nouvelle fenêtre


	"""
	pass

def Graphiques_Avec_Seaborn():
	"""
		La librairie graphique seaborn s'installe via la commande 

		**pip install seaborn**

		Une fois installée, la librairie est importée dans Python via la commande

		**import seaborn as sns**

		Le format data de seaborn est légérement différent de celui de MatplotLib : Les vecteurs x et y vont être **convertis** en format data seaborn. 

		Cette conversion passe par la lecture d'un fichier csv via la méthode **sns.load_dataset**

		Pour cela, on écrit les vecteurs data dans un fichier csv que l'on charge via seaborn.

		Une fois le dataset écrit dans une variable 

		Data=sns.load_dataset("Nom du data file") , 
		
		on va instancier une courbe seaborn via la commande :

		**sns.lineplot(x='label de x',y='label de y',hue='legende',data=Data)**
	"""
	pass

def Pour_Aller_Plus_Loin():
	"""
		Pour ceux qui souhaiterais approfondir l'apprentissage Python, vous trouverez ci dessous deux bibliothèque mathématiques Python :
			* **Vectorial lib** : Il s'agit d'une bibliothèque vectorielle inspirée de l'architecture PyQt
			* **cmatrix lib**   : Il s'agit d'une librairie de calculs matriciels scientifiques

		Ces bibliothèques de calcul puissantes permettent de construire des programmes robustes en stabilité.

		**Bonne continuation !!!**

		https://vectorial-lib.readthedocs.io/en/latest/
		
		https://matrix-lib-v20.readthedocs.io/en/latest/


	"""
	pass