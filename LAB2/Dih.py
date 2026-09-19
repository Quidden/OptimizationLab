import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3 * x + 2)

a = -0.581
b = -0.557
sigma = 0.001
epsilon = 0.0001

k = 0

print(
    f"{'k':<5}"
    f"{'x1':<12}"
    f"{'x2':<12}"
    f"{'f(x1)':<14}"
    f"{'f(x2)':<14}"
    f"{'[a_k, b_k]':<24}"
    f"{'L_k':<10}"
)

print("-" * 90)

print(
    f"{k:<5}"
    f"{'':<12}"
    f"{'':<12}"
    f"{'':<14}"
    f"{'':<14}"
    f"{f'[{a:.6f}, {b:.6f}]':<24}"
    f"{abs(b - a):<10.6f}"
)

while True:
    x1 = (a + b) / 2 - epsilon / 2
    x2 = (a + b) / 2 + epsilon / 2

    fx1 = f(x1)
    fx2 = f(x2)

    if fx1 < fx2:
        b = x2
    elif fx1 > fx2:
        a = x1
    else:
        a = x1
        b = x2

    k += 1

    length = abs(b - a)

    print(
        f"{k:<5}"
        f"{x1:<12.6f}"
        f"{x2:<12.6f}"
        f"{fx1:<14.6f}"
        f"{fx2:<14.6f}"
        f"{f'[{a:.6f}, {b:.6f}]':<24}"
        f"{length:<10.6f}"
    )

    if length <= sigma:
        break

x_min = (a + b) / 2

print()
print(f"x* = {x_min:.6f}")
print(f"f(x*) = {f(x_min):.6f}")