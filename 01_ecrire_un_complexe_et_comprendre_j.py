# ============================================================
# 01 - ECRIRE UN NOMBRE COMPLEXE EN PYTHON
# ============================================================
#
# En mathematiques, on ecrit souvent :
#     z = 3 + 4i
#
# En Python, on doit ecrire :
#     z = 3 + 4j
#
# Python utilise la lettre j pour representer l'unite imaginaire.
# Donc :
#     j correspond a sqrt(-1)
#
# ATTENTION :
# La lettre j toute seule n'a rien de special.
# Si vous ecrivez :
#     j = 10
# alors j devient simplement une variable normale.
#
# L'unite imaginaire s'ecrit avec un nombre juste devant j :
#     1j
#     2j
#     4j
#
# ============================================================


# Exemple simple
z = 3 + 4j

print("z =", z)
print("type(z) =", type(z))


# L'unite imaginaire
i_python = 1j

print("\n1j =", i_python)
print("(1j)^2 =", (1j) ** 2)


# IMPORTANT :
# j tout seul n'est pas reconnu comme l'unite imaginaire.

j = 10

print("\nApres j = 10 :")
print("j =", j)

# Ici Python utilise la variable j qui vaut 10
print("3 + 4*j =", 3 + 4 * j)


# Mais 4j reste un nombre imaginaire.
z2 = 3 + 4j

print("3 + 4j =", z2)


# Autres facons de creer des complexes

z3 = -2 - 5j
z4 = 7j
z5 = 6 + 0j

print("\nz3 =", z3)
print("z4 =", z4)
print("z5 =", z5)


# La fonction complex()
#
# complex(partie_reelle, partie_imaginaire)

z6 = complex(3, 4)
z7 = complex(-2, 5)

print("\ncomplex(3, 4) =", z6)
print("complex(-2, 5) =", z7)


# Creer un complexe a partir d'une chaine de caracteres

z8 = complex("3+4j")

print('\ncomplex("3+4j") =', z8)


# ============================================================
# A RETENIR
# ============================================================
#
# 3 + 4i   -> faux en Python
# 3 + 4j   -> correct
#
# j = 10   -> j devient une variable normale
#
# 1j       -> unite imaginaire
#
# complex(3, 4) -> 3 + 4j
# ============================================================
