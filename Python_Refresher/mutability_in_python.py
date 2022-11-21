a=[]
b=a

a.append(35)
print(id(a))
print(id(b))

print(a)
print(b)

c=100
d=100

print(id(c))
print(id(d))

c=110

print(id(c))
print(id(d))

e="hello"
f=e

print(id(e))
print(id(f))

e+="world"

print(id(e))
print(id(f))
