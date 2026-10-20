import math

def f(x):
    return (2 * x + 1) * (3 * x + 2) * math.cbrt(3 * x + 2)

a = -0.5810
b = -0.5570

i = 0
accuracy = 0.001

print(
    f"{'k':<4}"
    f"{'x1':<11}"
    f"{'xm':<11}"
    f"{'x2':<11}"
    f"{'f(x1)':<13}"
    f"{'f(xm)':<13}"
    f"{'f(x2)':<13}"
    f"{'[ak, bk]':<23}"
    f"{'Lk':<10}"
)

print("-" * 110)

while True:
    L = b - a

    mid = (a + b) / 2
    x1 = a + L / 4
    x2 = b - L / 4

    f1 = f(x1)
    fm = f(mid)
    f2 = f(x2)

    interval = f"[{a:.4f}, {b:.4f}]"

    print(
        f"{i:<4}"
        f"{x1:<11.4f}"
        f"{mid:<11.4f}"
        f"{x2:<11.4f}"
        f"{f1:<13.4f}"
        f"{fm:<13.4f}"
        f"{f2:<13.4f}"
        f"{interval:<23}"
        f"{L:<10.4f}"
    )

    if L <= accuracy:
        break

    if f1 < fm:
        b = mid

    elif f2 < fm:
        a = mid

    else:
        a = x1
        b = x2

    i += 1


mid = (a + b) / 2

print(f"\nx* = {mid:.4f}")
print(f"f(x*) = {f(mid):.4f}")