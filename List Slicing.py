a=[1,2,3,4,5,6,7,8,9]
print(a[:]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:3:3]) #[2]
print(a[0:5:2]) #[1, 3, 5]
print(a[1:7])#[2, 3, 4, 5, 6, 7]
print(a[:-1]) #[1, 2, 3, 4, 5, 6, 7, 8]
print(a[2:-1])#[3, 4, 5, 6, 7, 8]


i=["a","d","c","d","e","f"]
print(i[3])
del(i[4])
print(i)
i.append("b")
print(i)
i.sort()
print(i)

print(i)