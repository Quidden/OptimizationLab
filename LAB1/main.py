import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3 * x + 2)

stepx = -0.55
stepdelta = 1
check = True
k = 0

print(f"x = {stepx}")
print(f"delta = {stepdelta}")

while True:

    if check:
        next_step = stepx + stepdelta
    else:
        next_step = stepx - stepdelta

    if f(stepx) < f(next_step):
        if k == 0:
            check = False
            continue
        else:
            break

    print(
        f"k = {k} "
        f"x{k} = {stepx} "
        f"x{k + 1} = {next_step} "
        f"f(x{k}) = {f(stepx)} "
        f"f(x{k + 1}) = {f(next_step)}"
    )
    stepx = next_step
    stepdelta *= 2
    k += 1