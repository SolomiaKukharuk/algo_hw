def convert(number: int, to_base: int) -> str:
    stack = []
    while number > 0:
        d = number % to_base
        number //= to_base
        stack.append(d)

    result = ""
    while stack:
        result += get_char(stack.pop())
    return result


def get_char(d: int):
    if d < 10:
        return str(d)
    else:
        return f"[{d}]"


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        A = int(f.readline())
        P = int(f.readline())
        result = convert(A, P)
        print(result)
