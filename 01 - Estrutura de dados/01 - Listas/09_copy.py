lista = [1, "Python", [40, 30, 20]]

l2 =lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))  # 140721894256704 140721894256672

l2[0] = 2
l2[2][1] = 35
print(l2)  # [2, "Python", [40, 35, 20]]


