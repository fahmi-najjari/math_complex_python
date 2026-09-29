# ============================================================
# 03 - LE MODULE math
# ============================================================
#
# Python contient des fonctions mathematiques supplementaires.
#
# Pour les utiliser, on importe le module math.
# ============================================================

import math


# ------------------------------------------------------------
# PI
# ------------------------------------------------------------
pi=math.pi
print("Pi =", pi)
print(f"PI = {pi}")


# Resultat :
# 3.141592653589793
#
# Python affiche beaucoup de chiffres apres la virgule.
#
# Mais parfois, nous ne voulons afficher que quelques
# chiffres apres la virgule.
#
# Par exemple :
#
# 3.14
# 3.1416
# 3.141593
#
# Nous pouvons controler l'affichage avec une f-string.

print(f"{pi:.4f}")

# Résultat :
# 3.1416

# :.4f
# : indique le début du formatage
# . indique que nous allons formater les décimales
# 4 signifie qu'il y aura exactement 4 chiffres après la virgule
# f signifie "fixed" (fixe) : le nombre est affiché avec un nombre fixe
# de chiffres après la virgule.
# Ici, f ne signifie pas "float". 










# ------------------------------------------------------------
# e : CONSTANTE D'EULER
# ------------------------------------------------------------
#
# math.e represente la constante mathematique e.
#
# e ≈ 2.71828
# ------------------------------------------------------------




print("e =", math.e)


# ------------------------------------------------------------
# COMMENT LIRE math.pi ?
# ------------------------------------------------------------
#
# math      -> le module
# .         -> acceder a quelque chose dans le module
# pi        -> la constante pi
#
# De la meme facon :
#
# math.sqrt
# math.log
# math.sin
#
# ------------------------------------------------------------


# Exemple :

rayon = 3

aire = math.pi * rayon ** 2

print("Aire du cercle =", aire)


# ============================================================
# NOTATION SCIENTIFIQUE EN PYTHON
# ============================================================
#
# ATTENTION :
#
# Dans un nombre comme :
#
#     3e2
#
# la lettre "e" NE represente PAS la constante d'Euler math.e.
#
# Ici, "e" signifie :
#
#     x 10 puissance ...
#
# ------------------------------------------------------------


# Trois ecritures de la meme valeur

x = 3.25

y = 325 / 100

# 0.325e1 = 0.325 x 10^1 = 3.25
z = 0.325e1


print("\nx =", x)
print("y =", y)
print("z =", z)


# Les trois valeurs sont egales

print("x == y :", x == y)
print("y == z :", y == z)


# ------------------------------------------------------------
# AUTRES EXEMPLES DE NOTATION SCIENTIFIQUE
# ------------------------------------------------------------


# 3e2 = 3 x 10^2 = 300

a = 3e2

print("\n3e2 =", a)


# 4.5e3 = 4.5 x 10^3 = 4500

b = 4.5e3

print("4.5e3 =", b)


# 2.5e-2 = 2.5 x 10^-2 = 0.025

c = 2.5e-2

print("2.5e-2 =", c)


# ------------------------------------------------------------
# IMPORTANT : NE PAS CONFONDRE
# ------------------------------------------------------------
#
# math.e
#     -> constante d'Euler
#     -> environ 2.71828
#
# 3e2
#     -> notation scientifique
#     -> 3 x 10^2
#     -> 300
#
# 3e-2
#     -> 3 x 10^-2
#     -> 0.03
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# QUESTION POUR LA CLASSE
# ------------------------------------------------------------
#
# Avant d'executer, donner le resultat de :
#
# 5e2
# 7.5e3
# 4e-2
# 1.2e-3
#
# Puis verifier les reponses avec Python.
#
# ============================================================