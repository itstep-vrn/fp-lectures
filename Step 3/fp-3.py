# Python

def addGen(x):
    def go(y): return x+y
    return go

add1 = addGen(1)
add3 = addGen(3)

print (add1(1))
print (addGen(1)(1))
print (add3(1))
*/