n, m = [int(x) for x in input().split()]

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}
result = n_set.intersection(m_set)
[print(el) for el in result]
