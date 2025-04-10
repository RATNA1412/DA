d={1:"hello",2:"why",3:"hello"}
print(d)

print(d.get(1))
print(d.items())
print(d.keys())
print(d.values())
d.update({4:"ratna",5:"drashti"})
print(d)
d.pop(3)
print(d)
d.popitem()
print(d)


t=(1,2,3,4)
d1={}

print(d1.fromkeys(t,24))