y = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
x = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
# change_pos = 0

y.sort(key=lambda e: (e[1], e[2]))
print(y)

# for i in range(1, len(x)):
#     j = i
#     while j > 0:
#         for k in range(1, len(x[j])):
#             if (x[j - 1][k] != x[j][k]):
#                 change_pos = k
#                 break
#
#         if (x[j - 1][change_pos] > x[j][change_pos]):
#             swp_h = x[j]
#             x[j] = x[j - 1]
#             x[j - 1] = swp_h
#         else:
#             break
#         j -= 1
#
# print(x)