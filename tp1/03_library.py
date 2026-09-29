# ============================================================
# RACINE CARREE : SANS ET AVEC LA BIBLIOTHEQUE math
# ============================================================


# 1. SANS LA BIBLIOTHEQUE math
# On cree nous-memes une fonction.

def racine_carree(nombre):
    return nombre ** 0.5

x=racine_carree(25)
print(f"x est {x}")


# ------------------------------------------------------------


# 2. AVEC LA BIBLIOTHEQUE math
# La fonction existe deja : pas besoin de la programmer.

import math

y=math.sqrt(100)
print(f"y est {y}")


# ============================================================
# RESULTAT
# ============================================================
#
# 5.0
# 5.0
#
# La bibliotheque math nous donne directement sqrt().
# Nous pouvons donc reutiliser une fonction deja programmee.
# ============================================================