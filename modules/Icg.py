def generate_code(tree):
    stack = []
    quadruples = []
    temp_count = 1
    for node in tree:
        if node != "PLUS" and node != "MUL":
            stack.append(node[11:])
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"T{temp_count}"
            temp_count += 1
            quadruples.append((temp, op1, node, op2))
            stack.append(temp)
    while len(stack) > 1:
        op2 = stack.pop()
        op1 = stack.pop()
        temp = f"T{temp_count}"
        temp_count += 1
        quadruples.append((temp, op1, "PLUS", op2))
        stack.append(temp)
    return quadruples

tree = ('IDENTIFIER:x', 'INT:10', 'IDENTIFIER:y', 'INT:5', 'KEYWORD:IF', ('IDENTIFIER:x', 'GT', 'IDENTIFIER:y'), 'KEYWORD:THEN', ('IDENTIFIER:PRINT', 'LPAREN:', 
((('IDENTIFIER:x', 'PLUS', 'IDENTIFIER:y'),), 'RPAREN:')), 'KEYWORD:ELSE', (('IDENTIFIER:PRINT', 'LPAREN:', ((('IDENTIFIER:x', 'MINUS', 'IDENTIFIER:y'),), 'RPAREN:')), 'True'))
quadruples = generate_code(tree)

for quadruple in quadruples:
    op1 = quadruple[1]
    op2 = quadruple[3]
    operator = quadruple[2]
    print(f"{quadruple[0]} = {op1} {operator} {op2}")