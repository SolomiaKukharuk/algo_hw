OPERATORS = '+-*/'

def prefix_to_infix(prefix_list: list) -> str:
    prefix_list = prefix_list[::-1] # prefix -> postfix
    stack = list()
    for token in prefix_list:
        # print(stack)
        if token in OPERATORS:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append([f"{a[0]}+{b[0]}", token])
            elif token == "-":
                if b[1] in "+-" :
                    stack.append([f"{a[0]}-({b[0]})",token])
                else:
                    stack.append([f"{a[0]}-{b[0]}",token])
            elif token == "*":
                if b[1] in "+-" and a[1] in "+-":
                    stack.append([f"({a[0]})*({b[0]})", token])
                elif b[1] in "+-":
                    stack.append([f"{a[0]}*({b[0]})", token])
                elif a[1] in "+-":
                    stack.append([f"({a[0]})*{b[0]}", token])
                else:
                    stack.append([f"{a[0]}*{b[0]}", token])
            else:
                if b[1] in "+-*/" and a[1] in "+-":
                    stack.append([f"({a[0]})/({b[0]})", token])
                elif b[1] in "+-*/":
                    stack.append([f"{a[0]}/({b[0]})", token])
                elif a[1] in "+-":
                    stack.append([f"({a[0]})/{b[0]}", token])
                else:
                    stack.append([f"{a[0]}/{b[0]}", token])
        else:
            stack.append([token,'0'])

    return stack[0][0]


if __name__=="__main__":
    prefix = input()
    prefix_list = list()
    for el in prefix:
        prefix_list.append(el)

    result = prefix_to_infix(prefix_list)
    print(result)
