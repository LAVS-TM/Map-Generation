Implémentation
==============

Génération de la carte
----------------------

* Include :file:`<src/area.py>`
* Include :file:`<src/city.py>`

.. function:: generate_regions(regions_size)

   Génere les régions globales

   :param regions_size: La taille donnée pour calculer le diagramme de **Voronoi**
   :type regions_size: ``Integer``
   :rtype: Une liste de ``Polygon`` correspondant aux régions


La génération de la carte est la premiere étape dans nos algorithmes.
Elle prend en paramètre une taille qui est prédéfinie grâce à la population donnée au début du programme.
L'algorithme place des points répartis linéairement sur une certaine surface, puis les déplaces dans une direction aléatoire.
Il calcule ensuite un diagramme de **Voronoi** dans lequel nous récupérons les régions qui nous intéresse pour la suite.

Découpage des districts
-----------------------

* Include :file:`<src/city.py>`
* Include :file:`<src/map.py>`
* Include :file:`<src/city_areas/district.py>`



.. function:: split_region(regions, road_size)

   Découpe les régions avec une route nouvellement crée

   :param regions: L'ensemble des ``Polygon`` calculés précédemment
   :param road_size: La taille des routes entre les districts
   :type road_size: ``Integer``
   :return: Une liste des ``Polygon`` représentant les districts et un ``Polygon`` ou ``MultiPolgon`` représentant les routes


Une fois les régions généré, il nous faut les découper pour obtenir des districts séparés.
Par une suite d'intersection et de différence de ``Polygon``, l'algorithmes découpe les régions et crée des routes entre elles.
Nous récupérons donc en sortie toutes les régions ainsi que les routes.

Génération des murs
-------------------

* Include :file:`<src/city_areas/wall.py>`
* Include :file:`<src/city.py>`

La génération des murs se fait assez facilement en retracant un contour de toute nos régions.
Les murs nous servent également dans la suite de nos algorithmes, notamment pour retrouver le centre de la ville et placer nos bâtiments en conséquences.


Génération des bâtiments
------------------------

* Include :file:`<src/city.py>`
* Include :file:`<src/map.py>`

.. function:: generate_buildings(regions_size, district)

   Génere un découpage de zones pour un district donné

   :param regions_size: La taille des séparation entre les zones
   :param district: Une des régions de notre carte
   :return: Une liste des ``Polygon`` représentant les zones découpés dans un district


L'objectif ici est de découper les différents districts de notre carte pour pouvoir y placer des bâtiments.
Uniquement les zones contenant des maisons ainsi que des bâtiments du centre ville, par rapport au éléments extérieurs comme les champs et fermes qui eux, ne sont pas découpés.

De nouveaux points sont donc placés linéairement dans le district, ainsi que sur ses bords, pour calculer un nouveau diagramme de **Voronoi** et y extraire nos zones.


Génération du Château
---------------------

* Include :file:`<src/downtown/castle.py>`
* Include :file:`<src/city.py>`

La génération du ``Castle`` peut se faire selon différentes heuristiques.
Il a besoin d'être centré dans notre ville, et d'occuper une zone qui est assez grande.

Nous parcourons donc les 10% des bâtiments les plus au centre dans notre ville et nous choisissons le plus grand emplacement parmis ceux-ci.


Assignement des zones
---------------------

* Include :file:`<src/downtown/*>`
* Include :file:`<src/countrysides/*>`
* Include :file:`<src/map.py>`
* Include :file:`<src/city.py>`


.. function:: build_map(district, map_elements, city_elements, nb_houses)

   Assigne un certain type de bâtiments aux zones de notre ville.

   :param district: L'ensemble des districts de notre ville
   :param map_elements: Toutes les zones de notre ville
   :param city_elements: Les zones de notre ville découpée pour accueillir une maison ou un bâtiments de centre-ville
   :param nb_houses: Le nombre de parcelles découpées pouvant accueillir une maison ou un bâtiments de centre-ville
   :return: Les districts avec les batiments ajoutés à leur aires


Une fois que la totalité de notre ville a été découpé, il nous faut maintenant assigner un certains types de bâtiments à toutes ces zones.
Nous assignons en premier les bâtiments du centre-ville sur les zones découpés, puis les types de campagnes sur les zones au bord de notre ville.
L'assignation se fait selon une certaine distribution, selon si l'on veut plus ou moins de ce type de bâtiments dans notre ville.

Une fois le processus terminé, nous avons donc obtenu notre ville finale !

Types de zones
--------------

Voici les différentes formes que peuvent prendre les zones de la ville:

* ``Castle``
* ``Cathedral``
* ``Church``
* ``Farm``
* ``Field``
* ``Forest``
* ``Fort``
* ``Garden``
* ``House``
* ``Lake``
* ``Land``
* ``Mansion``
* ``Market``
* ``Monastry``
* ``Park``
* ``Townhall``
* ``University``

Pour `House` et `Mansion`, le polygone représentatif est composé d'un `Garden` en son centre.
Les autres zones restent pleines mais changent de couleur lors de la visualisation.