import math

def f(x):
    return (2 * x + 1) * (3 * x + 2) * math.cbrt(3 * x + 2)

a = -0.581
b = -0.557

accuracy = 0.001
v = (math.sqrt(5) - 1) / 2

print(
    f"{'':<14}"
    f"{'x1':<12}"
    f"{'x2':<12}"
    f"{'f(x1)':<14}"
    f"{'f(x2)':<14}"
    f"{'[a_k, b_k]':<24}"
    f"{'L_k':<10}"
)

print("-" * 100)

k = 0
print(
    f"{k:<14}"
    f"{'-':<12}"
    f"{'-':<12}"
    f"{'-':<14}"
    f"{'-':<14}"
    f"{f'[{a:.4f}, {b:.4f}]':<24}"
    f"{(b - a):<10.4f}"
)

k = 1

while (b - a) > accuracy:
    L = b - a

    x1 = b - v * L
    x2 = a + v * L

    f1 = f(x1)
    f2 = f(x2)

    if f1 <= f2:
        b = x2
    else:
        a = x1

    L = b - a
    x1 = b - v * L
    x2 = a + v * L
    f1 = f(x1)
    f2 = f(x2)

    print(
        f"{k:<14}"
        f"{x1:<12.4f}"
        f"{x2:<12.4f}"
        f"{f1:<14.4f}"
        f"{f2:<14.4f}"
        f"{f'[{a:.4f}, {b:.4f}]':<24}"
        f"{L:<10.4f}"
    )

    k += 1

result = (a + b) / 2

print(f"\nx* = {result:.4f}")
print(f"f(x*) = {f(result):.4f}")