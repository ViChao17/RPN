priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '(': 0
}

input_string = input()


def is_number(num):
    for c in num:
        if c in '1234567890.':
            continue
        return False
    return True


def parse_input_string(input_str: str) -> list[str]:
    number = ''
    output: list[str] = []
    for c in input_str:
        if c.isdigit() or c == '.':
            number += c
            continue
        if len(number) > 0:
            output.append(number)
            number = ''
        output.append(c)
    if len(number) != 0:
        output.append(number)

    return output


def to_polish_notation(input_list: list[str]):
    stack: list = []
    output = []
    for el in input_list:
        if is_number(el):
            output.append(float(el))
            continue
        if len(stack) == 0:
            stack.append(el)
            continue
        elif el in '*/+-^':
            stack_top = stack[-1]
            if priority[el] <= priority[stack_top]:
                output.append(stack.pop())
                stack.append(el)
            else:
                stack.append(el)
            continue
        elif el == '(':
            stack.append('(')
        elif el == ')':
            stack_top = stack.pop()
            while stack_top != '(':
                output.append(stack_top)
                stack_top = stack.pop()

    while len(stack) > 0:
        output.append(stack.pop())

    return output


def calc(rpn: list) -> float:
    stack = []
    for el in rpn:
        if type(el) == float:
            stack.append(el)
        else:
            right: float = stack.pop()
            left: float = stack.pop()
            if el == '/':
                stack.append(left/right)
            if el == '*':
                stack.append(left*right)
            if el == '-':
                stack.append(left-right)
            if el == '+':
                stack.append(left+right)
            if el == '^':
                stack.append(left**right)
    return stack[0]


parsed_input_string = parse_input_string(input_string)
rpn_list = to_polish_notation(parsed_input_string)
result = calc(rpn_list)
print(result)
