import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3*x + 2)

def df(x):
    return (14*x + 8) * math.cbrt(3*x + 2)

def ddf(x):
    return (56*x + 36) / math.cbrt(3*x + 2)**2

x = -0.581
accuracy = 0.0001
k = 0

header = (
    "{:<2}  {:>12}  {:>12}  {:>12}  {:>12}  {:>12}"
    .format("k", "xk", "f(xk)", "f'(xk)",
            "|f'(xk)|", "f''(xk)")
)

print(header)
print("-" * len(header))

while True:
    fx = f(x)
    dfx = df(x)
    ddfx = ddf(x)

    print(
        f"{k:<2}  {x:>12.6f}  {fx:>12.6f}  "
        f"{dfx:>12.6f}  {abs(dfx):>12.6f}  {ddfx:>12.6f}"
    )

    if abs(dfx) <= accuracy:
        print(f"x* = {x:.6f}")
        print(f"f(x*) = {fx:.6f}")
        break

    x = x - dfx / ddfx
    k += 1