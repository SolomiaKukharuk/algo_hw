import sys


def can_marshall(n, order):
    stack = []
    expected = 1

    for coach in order:

        while expected <= n and (not stack or stack[-1] != coach):
            stack.append(expected)
            expected += 1


        if stack and stack[-1] == coach:
            stack.pop()
        else:
            return "No"

    return "Yes"


def process_trains():
    result = []
    first_block = True

    input_data = sys.stdin.read().strip().split("\n")
    index = 0

    while index < len(input_data):
        n = int(input_data[index].strip())
        index += 1
        if n == 0:
            break

        if not first_block:
            result.append("")
        first_block = False

        while index < len(input_data):
            order = list(map(int, input_data[index].strip().split()))
            index += 1
            if order == [0]:
                break
            result.append(can_marshall(n, order))

    print("\n".join(result))


if __name__ == "__main__":
    process_trains()
