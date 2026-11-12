Ce dessin a été réalisé en utilisant la bibliothèque turtle de Python. Il met en pratique plusieurs concepts de programmation :
• Le ciel et le sol : Le ciel est un fond coloré (bgcolor) et le sol est dessiné grâce à une succession d'avancées (forward) et de virages à angle droit (right(90)), le tout rempli de couleur verte grâce à la fonction begin_fill() et end_fill().
• Le soleil : Il est simplement constitué d'un cercle jaune rempli, placé en haut à gauche grâce à la fonction de positionnement goto().
• La modularité : Le dessin des fleurs est divisé en trois fonctions. aller() pour se déplacer sans dessiner, petale() pour dessiner une forme unique, et fleur() pour assembler la tige, les pétales et le cœur.
• La répétition : La fonction petale() est appelée dans une boucle for. En tournant de 45 degrés à chaque fois (8 x 45 = 360), la tortue dessine les 8 pétales de manière parfaitement répartie.
• Les listes et les boucles : Pour planter les 5 fleurs, le programme utilise deux listes (positions et couleurs). Une boucle finale parcourt ces listes pour placer chaque fleur au bon endroit, avec la bonne couleur, et une taille qui augmente grâce au calcul 30 + i * 3.
