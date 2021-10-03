def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    for i in range(2, n):
        next_row = [1] * (i + 1)
        magic_triangle.append(next_row)
        for j in range(len(magic_triangle) - 1):
            last_element = magic_triangle[-1]
            if j in range(1, len(last_element)):
                next_row[j] = magic_triangle[i-1][j-1] + magic_triangle[i-1][j]
            else:
                next_row[j] = 1
    return magic_triangle














# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for i in range(2, n):
#         next_row = [1] * (i + 1)
#         for j in range(len(next_row) - 1):
#             if j in range(1, len(triangle[-1])):
#                 next_row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#             else:
#                 next_row[j] = 1
#         triangle.append(next_row)
#     return triangle
#

print(get_magic_triangle(5))
