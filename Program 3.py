l=[
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
temp=[]
for i in l:
    for j in i:
        temp.append(j)

out=[]
for k in range(0, len(temp), 3):
   out.append(temp[k:k + 3])
print(out)