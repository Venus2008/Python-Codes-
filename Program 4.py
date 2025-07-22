l=[1, 2, 3, 4, 5]
#k=list(map(lambda x: x*2, filter((lambda y:y%2==0),l)))
#print(k)

print(list(map(lambda x: x*2, filter(lambda y:y%2==0,l))))


