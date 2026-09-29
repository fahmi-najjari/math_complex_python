# ============================================================
# 02 - PARTIE REELLE, PARTIE IMAGINAIRE ET CONJUGUE
# ============================================================

z = 3 + 4j

print("z =", z)


# ------------------------------------------------------------
# .real
# ------------------------------------------------------------
#
# Retourne la partie reelle du nombre complexe.

print("\nPartie reelle :")
print(z.real)


# ------------------------------------------------------------
# .imag
# ------------------------------------------------------------
#
# Retourne la partie imaginaire.

print("\nPartie imaginaire :")
print(z.imag)


# ------------------------------------------------------------
# .conjugate()
# ------------------------------------------------------------
#
# Retourne le conjugue du nombre complexe.
#
# Exemple :
#     3 + 4j  ->  3 - 4j

print("\nConjugue :")
print(z.conjugate())


# ------------------------------------------------------------
# Exemple complet
# ------------------------------------------------------------

z2 = -5 + 2j

print("\nz2 =", z2)
print("Re(z2) =", z2.real)
print("Im(z2) =", z2.imag)
print("Conjugue(z2) =", z2.conjugate())


# ============================================================
# A RETENIR
# ============================================================
#
# z.real
# z.imag
# z.conjugate()
#
# real et imag sont des attributs :
#     on ne met PAS de parentheses.
#
# conjugate est une methode :
#     on met des parentheses.
# ============================================================
