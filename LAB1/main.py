import math

def f(x):
    return (2*x + 1) * (3*x + 2) * math.cbrt(3 * x + 2)

x = -0.55
delta = 0.001

direction = 1
k = 0

prev_x = None
points = []

print(
    f"{'k':<5}"
    f"{'delta':<12}"
    f"{'x_k':<12}"
    f"{'f(x_k)':<14}"
    f"{'f(x_k) < f(x_k-1)':<22}"
    f"{'[a0, b0]':<24}"
)

print("-" * 90)

while True:
    fx = f(x)
    points.append(x)

    if prev_x is None:
        condition = "-"
    else:
        condition = "Yes" if fx < f(prev_x) else "No"

    # Пока конечный интервал ещё не найден,
    # показываем текущий охваченный диапазон
    current_a = min(points)
    current_b = max(points)

    print(
        f"{k:<5}"
        f"{delta:<12.6f}"
        f"{x:<12.6f}"
        f"{fx:<14.6f}"
        f"{condition:<22}"
        f"{f'[{current_a:.6f}, {current_b:.6f}]':<24}"
    )

    next_x = x + direction * delta
    next_fx = f(next_x)

    # Если функция начала расти — минимум уже окружён
    if fx < next_fx:
        if k == 0:
            direction *= -1
            points.clear()
            prev_x = None
            continue
        else:
            points.append(next_x)

            a0 = min(prev_x, next_x)
            b0 = max(prev_x, next_x)

            k += 1
            delta *= 2

            print(
                f"{k:<5}"
                f"{delta:<12.6f}"
                f"{next_x:<12.6f}"
                f"{next_fx:<14.6f}"
                f"{'No':<22}"
                f"{f'[{a0:.6f}, {b0:.6f}]':<24}"
            )
            break

    prev_x = x
    x = next_x
    delta *= 2
    k += 1

print()
print(f"Initial uncertainty interval: [{a0:.6f}, {b0:.6f}]")