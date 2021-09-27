def gen_combinations(values, count, comb=[], index=0):
    if len(comb) == count:
        print(*comb, sep=", ")
        return

    for i in range(index, len(values)):
        comb.append(values[i])
        gen_combinations(values, count, comb, i + 1)
        comb.pop()


names = input().split(", ")
chairs_count = int(input())
gen_combinations(names, chairs_count)
