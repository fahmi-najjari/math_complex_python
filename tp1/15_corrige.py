# ============================================================
# 14 - CORRIGE DES EXERCICES
# ============================================================

import math
import cmath


print("=== EXERCICE 1 ===")

a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)


print("\n=== EXERCICE 2 ===")

print(math.pi)
print(math.sqrt(144))
print(math.gcd(84, 30))
print(math.lcm(12, 18))


print("\n=== EXERCICE 3 ===")

print(abs(-25))
print(round(3.141592, 3))
print(math.floor(8.9))
print(math.ceil(8.1))


print("\n=== EXERCICE 4 ===")

print(math.log(10))
print(math.log10(1000))
print(math.exp(2))


print("\n=== EXERCICE 5 ===")

print(math.sin(math.radians(30)))
print(math.cos(math.radians(60)))
print(math.tan(math.radians(45)))


print("\n=== EXERCICE 6 ===")

z = 5 - 12j

print(z)
print(type(z))
print(z.real)
print(z.imag)
print(abs(z))
print(z.conjugate())


print("\n=== EXERCICE 7 ===")

print(cmath.sqrt(-25))


print("\n=== EXERCICE 8 ===")

z = -3 + 4j

theta = cmath.phase(z)

print(theta)
print(math.degrees(theta))
print(cmath.polar(z))


print("\n=== EXERCICE 9 ===")

r = 10

angle_deg = 60

angle_rad = math.radians(angle_deg)

z = cmath.rect(r, angle_rad)

print(z)
