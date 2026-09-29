# ============================================================
# 04 - OPERATIONS SUR LES NOMBRES COMPLEXES
# ============================================================

z1 = 3 + 4j
z2 = 2 - 1j

print("z1 =", z1)
print("z2 =", z2)


# Addition
print("\nAddition :")
print(z1 + z2)


# Soustraction
print("\nSoustraction :")
print(z1 - z2)


# Multiplication
print("\nMultiplication :")
print(z1 * z2)


# Division
print("\nDivision :")
print(z1 / z2)


# Puissance
print("\nPuissances :")
print("z1**2 =", z1 ** 2)
print("z1**3 =", z1 ** 3)


# Oppose
print("\nOppose :")
print(-z1)


# Egalite
print("\nComparaison d'egalite :")
print("z1 == z2 :", z1 == z2)
print("z1 != z2 :", z1 != z2)


# ------------------------------------------------------------
# ATTENTION
# ------------------------------------------------------------
#
# Les comparaisons d'ordre ne sont pas permises :
#
# z1 < z2
# z1 > z2
#
# Cela produit une erreur TypeError.
#
# Pour comparer la taille, on compare souvent les modules :
#
print("\nComparaison par module :")
print(abs(z1) > abs(z2))
