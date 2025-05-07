def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output = []
    stack = []

    # Helper to determine if token is operand (number/variable)
    def is_operand(c):
        return c.isalnum()

    for token in expression:
        if is_operand(token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:  # operator
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ''.join(output)
