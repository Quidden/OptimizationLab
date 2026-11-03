import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3*x + 2)

def df(x):
    return (14*x + 8) * math.cbrt(3*x + 2)

x1 = -0.581
x2 = -0.557
df1 = df(x1)
df2 = df(x2)
accuracy = 0.0001
k = 0

header = (
    "{:<2} {:>12} {:>15} {:>12} {:>12} {:>12} {:>15}"
    .format("№ k", "x(k-1)", "f'(x(k-1))", "xk",
            "f'(xk)", "x(k+1)", "f'(x(k+1))")
)

print(header)
print("-" * len(header))

print(
    f"{k:<2} {x1:>12.6f} {df1:>15.6f} "
    f"{x2:>12.6f} {df2:>12.6f} "
    f"{'-':>12} {'-':>15}"
)

while True:

    x3 = x2 - df2 * (x2 - x1) / (df2 - df1)
    df_temp = df(x3)

    print(
        f"{k + 1:<2} {x1:>12.6f} {df1:>15.6f} "
        f"{x2:>12.6f} {df2:>12.6f} "
        f"{x3:>12.6f} {df_temp:>15.6f}"
    )

    if abs(df_temp) <= accuracy:
        print(f"\nx* = {x3:.6f}")
        print(f"f(x*) = {f(x3):.6f}")
        break

    if df_temp < 0:
        x1 = x3
        df1 = df_temp
    else:
        x2 = x3
        df2 = df_temp

    k += 1