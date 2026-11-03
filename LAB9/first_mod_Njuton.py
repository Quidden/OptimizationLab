
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
DFF = ddf(x1)
tempx = x1

header = "{:<5} {:>12} {:>14}".format("k", "xk", "f'(xk)")

print(header)
print("-" * len(header))

while True:

    df_temp = df(tempx)
    fx = f(tempx)

    print(f"{k:<5} {tempx:>12.6f} {df_temp:>14.6f}")

    if abs(df_temp) <= accuracy:
        break

    tempx = tempx - df_temp / DFF
    k += 1

print(f"x* = {tempx:.6f}")
print(f"f(x*) = {f(tempx):.6f}")