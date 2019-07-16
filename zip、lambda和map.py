#zip
a=[1,2,3]
b=[2,3,4]
print(list(zip(a,b)))

for i,j in zip(a,b):
    print(i,j)

#lambda
def fun1(x,y):
    return x+y
print(fun1(1,2))

fun2=lambda x,y:x+y
print(fun2(1,2))

#map
map(fun1,[1],[2])
print(list(map(fun1,[1],[2])))

