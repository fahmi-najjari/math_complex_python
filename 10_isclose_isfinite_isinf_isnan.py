# ============================================================
# 10 - TESTS UTILES POUR LES NOMBRES COMPLEXES
# ============================================================

import cmath


# ------------------------------------------------------------
# cmath.isclose()
# ------------------------------------------------------------
#
# Compare deux nombres en tenant compte des petites erreurs
# d'arrondi des nombres flottants.

z1 = 0.1 + 0.2j
z2 = 0.10000000001 + 0.20000000001j

print("z1 == z2 :", z1 == z2)

print("cmath.isclose(z1, z2) :")
print(cmath.isclose(z1, z2))


# On peut choisir une tolerance :

print("\nAvec tolerance :")
print(
    cmath.isclose(
        z1,
        z2,
        rel_tol=1e-8,
        abs_tol=1e-12
    )
)


# ------------------------------------------------------------
# cmath.isfinite()
# ------------------------------------------------------------

z3 = 3 + 4j

print("\nisfinite :", cmath.isfinite(z3))


# ------------------------------------------------------------
# cmath.isinf()
# ------------------------------------------------------------

z_inf = complex(float("inf"), 2)

print("isinf :", cmath.isinf(z_inf))


# ------------------------------------------------------------
# cmath.isnan()
# ------------------------------------------------------------

z_nan = complex(float("nan"), 2)

print("isnan :", cmath.isnan(z_nan))


# ============================================================
# A RETENIR
# ============================================================
#
# cmath.isclose(z1, z2)
# cmath.isfinite(z)
# cmath.isinf(z)
# cmath.isnan(z)
# ============================================================
