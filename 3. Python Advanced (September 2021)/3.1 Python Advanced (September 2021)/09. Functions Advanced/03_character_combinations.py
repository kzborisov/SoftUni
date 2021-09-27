def permute(values, idx = 0):
    if idx == len(values):
        print(''.join(values))
        return

    for i in range(idx, len(values)):
        values[i], values[idx] = values[idx], values[i]
        permute(values, idx + 1)
        values[i], values[idx] = values[idx], values[i]


permute(list(input()))
