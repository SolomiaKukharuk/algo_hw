import math

def parse_time(time_str: str) -> int:
    hours, mins = map(int, time_str.split(':'))
    return hours * 60 + mins

def format_time(minutes: int) -> str:
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def can_finish(v_max, d, dandelions, total_time):
    current_time = 0.0
    prev_x = 0

    for x, t in dandelions:
        distance = x - prev_x
        travel_time = distance / v_max
        arrival = current_time + travel_time
        start_eat = max(arrival, t)

        # Якщо черепаха не встигає з'їсти кульбабку до заданого часу
        if start_eat + d > total_time:
            return False

        current_time = start_eat + d
        prev_x = x

    return_time = prev_x / v_max  # Час повернення додому
    return current_time + return_time <= total_time

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    v_max, d = map(int, lines[0].split())  # Максимальна швидкість та час поїдання
    n = int(lines[1])  # Кількість кульбабок

    if n == 0:
        with open("output.txt", "w") as f:
            f.write("00:00\n")
        return

    dandelions = []
    for i in range(2, 2 + n):
        x_str, t_str = lines[i].split()
        x = int(x_str)
        t = parse_time(t_str)
        dandelions.append((x, t))


    low = 0
    high = 24 * 60

    while high - low > 1e-6:
        mid = (low + high) / 2
        if can_finish(v_max, d, dandelions, mid):
            high = mid
        else:
            low = mid

    total_ceil = math.ceil(high)
    result = format_time(total_ceil)


    with open("output.txt", "w") as f:
        f.write(result + "\n")

main()

