**Support Intéractif de Formation Python**
==========================================

*Author* : **CABOS Matthieu**

*Date* : **10/12/2020**

Générateur de documentation pour une Formation Python

Prerequires
-----------

* Python v3.9
* Sphinx v4.0
* Miktex v20.11

Edition De Contenu
------------------

Afin de modifier le contenu du document généré, il faut procéder de la façon suivante.
Le texte brut est contenu dans les fichiers sources .py disponibles dans le repertoire.
La modification d'un contenu déja existant est prise en compte lors de la compilation.
Les fichiers de structure sont placés dans le repertoire source sous la nomenclature **.rst**

Pour l'ajout d'un article il est necessaire de modifier deux fichiers :
  * ``Le fichier Python .py`` où la nomenclature utilisée pour la conception d'un article est la definition de fonction standard de type **def monArticle():** L'article est rédigé en RestructuredText en tant que docstring.
  * ``Le fichier source .rst`` présent dans le repertoire source où l'on souhaite rajouter l'article. L'article est automatiquement ajouté au contenu en utilisant la commande **.. autofunction:: NomDuFichier.NomDeLaFonction** déja utilisée pour la structure.
  
 Pour des modifications d'articles plus importantes, on utilisera une arborescence résumant la structure du document sous divers fichiers .rst à placer dans le dossier source. On pourra prendre exemple sur la structure utilisée ici.
 Les docstrings se résument à des instructions ReSt **simples** afin de rédiger des documents scientifiques standardisés.
 
 Pour plus de détail sur la syntaxe du RestructuredText, une documentation est disponible ici : https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

Compilation
-----------

La compilation des documents se fait via les commandes suivantes :

``Compilation Html``

**./make html**

*Le fichier index.html généré se trouve dans le dossier build/html*

``Compilation Pdf``

**./make latex**

**cd ./build/latex/**

**./make**

*Le fichier Pdf généré se trouve dans le dossier build/latex*
