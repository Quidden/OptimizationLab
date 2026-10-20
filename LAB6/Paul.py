
import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3*x + 2)

x1 = -0.581
step = 0.001
accuracy = 0.00001
accuracy_f = 0.00001

x2 = x1 + step
fx1 = f(x1)
fx2 = f(x2)

if fx1 > fx2:
    x3 = x2 + step
else:
    x3 = x1 - step

header = (
    f"{'k':<4}  {'x1':>11}  {'x2':>11}  {'x3':>11}  "
    f"{'f(x1)':>12}  {'f(x2)':>12}  {'f(x3)':>12}  "
    f"{'xt':>11}  {'f(xt)':>12}"
)

print("Таблиця 4.7 - Результати пошуку методом Пауелла")
print(header)
print("-" * len(header))

k = 1

while True:
    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)

    fmin = min(fx1, fx2, fx3)
    fmax = max(fx1, fx2, fx3)

    if fmin == fx1:
        xmin = x1
    elif fmin == fx2:
        xmin = x2
    else:
        xmin = x3

    if fmax == fx1:
        xmax = x1
    elif fmax == fx2:
        xmax = x2
    else:
        xmax = x3

    a1 = (fx2 - fx1) / (x2 - x1)
    a2 = ((fx3 - fx1) / (x3 - x1) - a1) / (x3 - x2)

    if a2 > 0:
        xt = (x1 + x2) / 2 - a1 / (2 * a2)
    elif a2 < 0:
        xt = 2 * xmin - xmax

    fxt = f(xt)

    print(
        f"{k:<4}  {x1:>11.6f}  {x2:>11.6f}  {x3:>11.6f}  "
        f"{fx1:>12.8f}  {fx2:>12.8f}  {fx3:>12.8f}  "
        f"{xt:>11.6f}  {fxt:>12.8f}"
    )

    if abs(xt - xmin) <= accuracy and abs(fxt - fmin) <= accuracy_f:
        break

    if xmax == x1:
        x1 = xt
    elif xmax == x2:
        x2 = xt
    else:
        x3 = xt

    k += 1

print("x* =", xt,
      "f(x*) =", fxt)
