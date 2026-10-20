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

header = (
    f"{'k':<5}  {'xk':>12}  {'f(xk)':>12}  "
    f"{'f\'(xk)':>12}  {'|f\'(xk)|':>12}  {'f\'\'(xk)':>12}"
)

print("Таблиця 4.8 - Результати пошуку методом Ньютона")
print(header)
print("-" * len(header))

while True:
    df_temp = df(x1)
    dff_temp = ddf(x1)
    fx = f(x1)

    print(
        f"{k:<5}  {x1:>12.8f}  {fx:>12.8f}  "
        f"{df_temp:>12.8f}  {abs(df_temp):>12.8f}  "
        f"{dff_temp:>12.8f}"
    )

    if abs(df_temp) <= accuracy:
        break

    x1 = x1 - df_temp / dff_temp
    k += 1

print("x* =", x1)
print("f(x*) =", f(x1))
