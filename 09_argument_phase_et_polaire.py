# ============================================================
# 09 - ARGUMENT, PHASE ET FORME POLAIRE
# ============================================================

import cmath
import math

z = 3 + 4j

print("z =", z)


# ------------------------------------------------------------
# cmath.phase(z)
# ------------------------------------------------------------
#
# Retourne l'argument du complexe en radians.

theta = cmath.phase(z)

print("\nArgument en radians :")
print(theta)


# Convertir radians -> degres

theta_deg = math.degrees(theta)

print("\nArgument en degres :")
print(theta_deg)


# ------------------------------------------------------------
# cmath.polar(z)
# ------------------------------------------------------------
#
# Retourne :
#     (module, argument)
#
# Sous forme d'un tuple.

r, theta = cmath.polar(z)

print("\nForme polaire :")
print("r =", r)
print("theta =", theta)


# ------------------------------------------------------------
# cmath.rect(r, theta)
# ------------------------------------------------------------
#
# Fait l'operation inverse.
#
# A partir d'un module r et d'un angle theta,
# reconstruit le nombre complexe.

z2 = cmath.rect(r, theta)

print("\nRetour en forme cartesienne :")
print(z2)


# Exemple avec angle en degres

r = 10
angle_deg = 30

angle_rad = math.radians(angle_deg)

z3 = cmath.rect(r, angle_rad)

print("\nModule = 10, angle = 30 degres")
print(z3)


# ============================================================
# A RETENIR
# ============================================================
#
# cmath.phase(z)
# cmath.polar(z)
# cmath.rect(r, theta)
#
# math.degrees(radians)
# math.radians(degres)
# ============================================================
