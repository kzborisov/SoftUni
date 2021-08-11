sequence = input()
bomb_strength = 0
new_sequence = ""
j = 0

for i in range(len(sequence)):
    if not sequence[i] == ">" and bomb_strength > 0:
        bomb_strength -= 1
    elif sequence[i] == ">":
        bomb_strength += int(sequence[i+1])
        new_sequence += sequence[i]
    else:
        new_sequence += sequence[i]

print(new_sequence)

















#
# while j < len(sequence):
#
#     for i in range(len(sequence)):
#         if not sequence[i] == ">" and bomb_strength > 0:
#             bomb_strength -= 1
#         elif sequence[i] == ">":
#             bomb_strength += int(sequence[i + 1])
#             new_sequence += sequence[i]
#         else:
#             new_sequence += sequence[i]
#         j += 1
# print(new_sequence)
