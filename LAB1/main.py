import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3 * x + 2)

stepx = -0.55
stepdelta = 0.001
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
            print(
                f"k = {k} "
                f"x{k} = {stepx:.4f} "
                f"x{k + 1} = {next_step:.4f} "
                f"f(x{k}) = {f(stepx):.4f} "
                f"f(x{k + 1}) = {f(next_step):.4f}"
            )
            break

    print(
        f"k = {k} "
        f"x{k} = {stepx:.4f} "
        f"x{k + 1} = {next_step:.4f} "
        f"f(x{k}) = {f(stepx):.4f} "
        f"f(x{k + 1}) = {f(next_step):.4f}"
    )

    stepx = next_step
    stepdelta *= 2
    k += 1
