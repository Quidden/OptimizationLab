import math

def f(x):
    return (2 * x + 1) * (3 * x + 2) * math.cbrt(3 * x + 2)

a = -0.581
b = -0.557

accuracy = 0.001

L = b - a

fib = [1, 1]

while fib[-1] < L / accuracy:
    fib.append(fib[-1] + fib[-2])

m = len(fib) - 1
n = m - 1

v = fib[-2] / fib[-1]

x2 = a + v * L
x1 = a + b - x2

f1 = f(x1)
f2 = f(x2)

print(
    f"{'k':<5}"
    f"{'x1':<12}"
    f"{'x2':<12}"
    f"{'f(x1)':<14}"
    f"{'f(x2)':<14}"
    f"{'[a_k, b_k]':<24}"
    f"{'L_k':<12}"
)

print("-" * 93)

print(
    f"{0:<5}"
    f"{'':<12}"
    f"{'':<12}"
    f"{'':<14}"
    f"{'':<14}"
    f"{f'[{a:.4f}, {b:.4f}]':<24}"
    f"{L:<12.4f}"
)

i = 1

while True:

    if f1 < f2:
        b = x2

        x2 = x1
        f2 = f1

        x1 = a + b - x2
        f1 = f(x1)

    else:
        a = x1

        x1 = x2
        f1 = f2

        x2 = a + b - x1
        f2 = f(x2)

    L = b - a

    print(
        f"{i:<5}"
        f"{x1:<12.4f}"
        f"{x2:<12.4f}"
        f"{f1:<14.4f}"
        f"{f2:<14.4f}"
        f"{f'[{a:.4f}, {b:.4f}]':<24}"
        f"{L:<12.4f}"
    )

    if i >= n:
        break

    i += 1

result = (a + b) / 2

print()
print(f"x* = {result:.4f}")
print(f"f(x*) = {f(result):.4f}")