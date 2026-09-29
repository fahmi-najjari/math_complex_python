# ============================================================
# 11 - ARGUMENT ET FORME POLAIRE
# ============================================================

import math
import cmath


z = 3 + 4j

print("z =", z)


# ------------------------------------------------------------
# ARGUMENT
# ------------------------------------------------------------
#
# cmath.phase(z)
#
# retourne l'argument en radians.
# ------------------------------------------------------------

theta = cmath.phase(z)

print("Argument en radians =", theta)


# Conversion en degres :

print("Argument en degres =", math.degrees(theta))


# ------------------------------------------------------------
# FORME POLAIRE
# ------------------------------------------------------------
#
# cmath.polar(z)
#
# retourne deux valeurs :
#
# module, argument
# ------------------------------------------------------------

r, theta = cmath.polar(z)

print("Module =", r)

print("Argument =", theta)


# ------------------------------------------------------------
# RECONSTRUIRE UN COMPLEXE
# ------------------------------------------------------------
#
# cmath.rect(module, argument)
# ------------------------------------------------------------

z2 = cmath.rect(r, theta)

print("Complexe reconstruit =", z2)


# ------------------------------------------------------------
# EXEMPLE
# ------------------------------------------------------------
#
# Construire un complexe de :
#
# module = 10
# angle = 30 degres
# ------------------------------------------------------------

r = 10

angle_deg = 30

angle_rad = math.radians(angle_deg)

z3 = cmath.rect(r, angle_rad)

print("Complexe =", z3)


# ------------------------------------------------------------
# QUESTION POUR LA CLASSE
# ------------------------------------------------------------
#
# Construire un complexe de :
#
# module = 5
# angle = 45 degres
#
# ============================================================
