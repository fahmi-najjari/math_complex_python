# ============================================================
# 05 - LE MODULE cmath
# ============================================================
#
# Le module cmath contient les fonctions mathematiques
# adaptees aux nombres complexes.
#
# Pour l'utiliser :
#
#     import cmath
#
# ============================================================

import cmath


# ------------------------------------------------------------
# cmath.sqrt()
# ------------------------------------------------------------
#
# Calcule une racine carree, y compris pour les nombres negatifs.

print("sqrt(-1) =", cmath.sqrt(-1))
print("sqrt(-4) =", cmath.sqrt(-4))
print("sqrt(-16) =", cmath.sqrt(-16))


# Racine d'un nombre complexe

z = 3 + 4j

print("\nz =", z)
print("sqrt(z) =", cmath.sqrt(z))


# ------------------------------------------------------------
# Difference avec math.sqrt()
# ------------------------------------------------------------
#
# math.sqrt() est surtout fait pour les nombres reels.
#
# Ceci provoque une erreur :
#
# import math
# math.sqrt(-4)
#
# Alors que :
#
# cmath.sqrt(-4)
#
# fonctionne.
