test_input = list(input())

opening_parantheses_stack = []
is_balanced = True

for ch in test_input:
    if ch in "{([":
        opening_parantheses_stack.append(ch)
    else:
        if not opening_parantheses_stack:
            is_balanced = False
            break

        last_opening = opening_parantheses_stack.pop()
        last_closing = ch
        pair = f"{last_opening}{last_closing}"
        if pair not in "{}[]()":
            is_balanced = False
            break

if is_balanced and not opening_parantheses_stack:
    print("YES")
else:
    print("NO")
