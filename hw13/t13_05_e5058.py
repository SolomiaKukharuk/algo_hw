OPENING_BRACKETS = ("(", "[", "{")
CLOSING_BRACKETS = (")", "]", "}")


def check_brackets(brackets_list: list) -> bool:
    stack = []
    for bracket in brackets_list:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif stack:
            if OPENING_BRACKETS[CLOSING_BRACKETS.index(bracket)] != stack.pop():
                return False
        else:
            return False

    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        seq = str(f.readline())[:-1]
        brackets_list = list()
        for el in seq:
            brackets_list.append(el)

        if check_brackets(brackets_list):
            print('yes')
        else:
            print('no')