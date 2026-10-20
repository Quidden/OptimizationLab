import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3*x + 2)

def df(x):
    return (14*x + 8) * math.cbrt(3*x + 2)

def ddf(x):
    return (56*x + 36) / math.cbrt(3*x + 2)**2

x1 = -0.581
accuracy = 0.0001
k = 0
r = 0.5

header = (
    "{:<5} {:>12} {:>7} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}"
    .format("k", "xk", "alpha", "f(xk)", "f'(xk)",
            "f''(xk)", "xt", "f(xt)", "f'(xt)")
)

print(header)
print("-" * len(header))

print(
    f"{k:<5} {x1:>12.8f} {'-':>7} {f(x1):>12.8f} "
    f"{df(x1):>12.8f} {ddf(x1):>12.8f} "
    f"{'-':>12} {'-':>12} {'-':>12}"
)

while True:
    a = 1
    df_temp = df(x1)
    dff_temp = ddf(x1)
    fx = f(x1)

    if abs(df_temp) <= accuracy:
        break

    k += 1

    while True:
        x1_temp = x1 - a * df_temp / dff_temp
        fxt = f(x1_temp)
        dfxt = df(x1_temp)

        left = fxt - fx
        right = -r * a * (df_temp**2 / dff_temp)

        print(
            f"{k:<5} {x1:>12.8f} {a:>7.3f} {fx:>12.8f} "
            f"{df_temp:>12.8f} {dff_temp:>12.8f} "
            f"{x1_temp:>12.8f} {fxt:>12.8f} {dfxt:>12.8f}"
        )

        if abs(dfxt) <= accuracy or left <= right:
            x1 = x1_temp
            break
        else:
            a = a / 2

            if a < 1e-12:
                raise RuntimeError("Step is too small")

print("x* =", x1)
print("f(x*) =", f(x1))
