expr = input()

parenthesis_index = []

for idx, ch in enumerate(expr):
    if ch not in ["(", ")"]:
        continue
    if ch == "(":
        parenthesis_index.append(idx)
    elif ch == ")":
        start_index = parenthesis_index.pop()
        end_index = idx
        print(expr[start_index:end_index+1])
