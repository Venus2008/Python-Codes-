# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# l=[
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# ]
# temp=[]
# for i in l:
#     for j in i:
#         temp.append(j)
# # TEMP=[]
# out=[]
# for k in range(0, len(temp), 3):
#    out.append(temp[k:k + 3])
# print(out)

# Original matrix
l = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose logic
out = []
for c in range(len(l[0])):  # iterate over columns
    temp = []
    for r in range(len(l)):  # iterate over rows
        temp.append(l[r][c])
    out.append(temp)

print(out)
