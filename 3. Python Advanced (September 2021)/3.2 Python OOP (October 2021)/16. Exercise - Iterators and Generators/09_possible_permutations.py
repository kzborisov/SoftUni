from itertools import permutations


def possible_permutations(input_list):
    return (list(p) for p in permutations(input_list))

# Solved with Recursion
# def possible_permutations(input_list):
#     if len(input_list) == 1:
#         yield input_list
#     else:
#         for i in range(len(input_list)):
#             for perm in possible_permutations(input_list[:i] + input_list[i + 1:]):
#                 yield [input_list[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
