# ============================================================
# 08 - NOMBRES COMPLEXES EN PYTHON
# ============================================================
#
# Les etudiants connaissent deja les nombres complexes.
#
# Ici, nous apprenons uniquement comment Python les represente.
# ============================================================


# ------------------------------------------------------------
# EN MATHEMATIQUES
# ------------------------------------------------------------
#
# z = 3 + 4i
#
#
# EN PYTHON
#
# z = 3 + 4j
#
# Python utilise j au lieu de i.
# ------------------------------------------------------------

z = 3 + 4j

print("z =", z)

print("type(z) =", type(z))


# ------------------------------------------------------------
# L'UNITE IMAGINAIRE
# ------------------------------------------------------------
#
# En Python :
#
# 1j
#
# represente sqrt(-1).
# ------------------------------------------------------------

print("1j =", 1j)

print("(1j)^2 =", (1j) ** 2)


# ------------------------------------------------------------
# ATTENTION : j TOUT SEUL
# ------------------------------------------------------------
#
# j tout seul n'est PAS un symbole special de Python.
#
# Si on ecrit :
#
# j = 10
#
# alors j devient une variable normale.
# ------------------------------------------------------------

j = 10

print("Variable j =", j)


# Ici, Python utilise la variable j :

print("3 + 4 * j =", 3 + 4 * j)


# Mais 4j reste une notation complexe :

z2 = 3 + 4j

print("3 + 4j =", z2)


# ------------------------------------------------------------
# AUTRE FACON : complex()
# ------------------------------------------------------------

z3 = complex(3, 4)

print("complex(3, 4) =", z3)


# Premier argument  -> partie reelle
# Deuxieme argument -> partie imaginaire


# ------------------------------------------------------------
# QUESTION POUR LA CLASSE
# ------------------------------------------------------------
#
# Creer en Python :
#
# z1 = 5 - 2i
# z2 = -3 + 7i
# z3 = -6i
#
# ============================================================
