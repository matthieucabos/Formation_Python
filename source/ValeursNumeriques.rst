Valeurs numériques
==================

En Python les variables numériques sont un incontournable du bon déroulement d’un programme.
Un ordinateur n’est rien d’autre qu’une machine à calculer, les valeurs numériques et l’exactitude mathématique et logique des opérations utilisées consituent la base incontournable d’un programme **fiable**. 

En effet, en informatique, les signaux sont numérisés sous forme de longue (très longues) suites de valeurs représentant une image, un texte, un son, etc ..

La manipulation **exacte** de ce contenu passe par une rigueur mathématiques des intervalles utilisés, des domaines de définition des fonction, répondant à la structure interne des fichiers ( une image .png peut être par exemple définie sur 255 niveaux de gris définis entre 0 et 127. 

Une sortie des intervalles de définition (respectivement *[0,255]* et *[0,127]*) engendre un bug.

 On distingue plusieurs types de variables numériques :
    * *Integer* : Il s’agit d’une valeur entière signée ou non
    * *Float* : Il s’agit d’une valeur flottante signée ou non
    * *Complex* : Il s’agit d’une valeur complexe définie par x et y (les valeurs réelles et imaginaires du nombre)

.. autofunction:: Valeurs_Numeriques.Entiers
.. autofunction:: Valeurs_Numeriques.Nombres_A_Virgules_Flottante
.. autofunction:: Valeurs_Numeriques.Nombres_Complexes
.. autofunction:: Valeurs_Numeriques.Conversions
.. autofunction:: Valeurs_Numeriques.Booleens
.. autofunction:: Valeurs_Numeriques.ObjetVide
.. autofunction:: Valeurs_Numeriques.Date_Et_Temps