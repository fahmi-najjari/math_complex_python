# ============================================================
# 03 - abs() : MODULE D'UN NOMBRE COMPLEXE
# ============================================================
#
# abs(z) retourne le module du nombre complexe.
#
# Pour :
#     z = a + bj
#
# le module est :
#     sqrt(a^2 + b^2)
#
# ============================================================

z = 3 + 4j

print("z =", z)

module = abs(z)

print("abs(z) =", module)


# Exemple 2

z2 = -5 + 12j

print("\nz2 =", z2)
print("abs(z2) =", abs(z2))


# abs() fonctionne aussi avec les nombres reels

x = -7

print("\nabs(-7) =", abs(x))


# ------------------------------------------------------------
# Comparer des complexes par leur module
# ------------------------------------------------------------
#
# Python ne permet pas :
#     z1 < z2
#
# Mais on peut comparer leurs modules.

z1 = 3 + 4j
z2 = 1 + 1j

print("\nabs(z1) =", abs(z1))
print("abs(z2) =", abs(z2))
print("abs(z1) > abs(z2) =", abs(z1) > abs(z2))


# ============================================================
# A RETENIR
# ============================================================
#
# abs(z) -> module de z
#
# Exemple :
# abs(3 + 4j) -> 5.0
# ============================================================
