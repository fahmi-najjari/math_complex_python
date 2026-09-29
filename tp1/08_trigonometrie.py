# ============================================================
# 07 - TRIGONOMETRIE EN PYTHON
# ============================================================

import math


# ------------------------------------------------------------
# IMPORTANT : PYTHON UTILISE LES RADIANS
# ------------------------------------------------------------


# sin(pi/2)

print("sin(pi/2) =", math.sin(math.pi / 2))


# cos(0)

print("cos(0) =", math.cos(0))


# tan(pi/4)

print("tan(pi/4) =", math.tan(math.pi / 4))


# ------------------------------------------------------------
# DEGRES -> RADIANS
# ------------------------------------------------------------

angle_deg = 60

angle_rad = math.radians(angle_deg)

print("60 degres en radians =", angle_rad)


# Maintenant on peut calculer le sinus.

print("sin(60 degres) =", math.sin(angle_rad))


# ------------------------------------------------------------
# RADIANS -> DEGRES
# ------------------------------------------------------------

x = math.pi / 3

print("pi/3 en degres =", math.degrees(x))


# ------------------------------------------------------------
# QUESTION POUR LA CLASSE
# ------------------------------------------------------------
#
# Calculer :
#
# sin(30 degres)
# cos(60 degres)
# tan(45 degres)
#
# Conseil :
# utiliser math.radians()
#
# ============================================================
