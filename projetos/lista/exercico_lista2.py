l = []
l.append('x')
l.append('y')
l.append('z')
print(l)

l.insert(0, 'w')
l.insert(0, 'k')
print(l)

l_roubo = []
l_roubo = l.pop(0)
l_roubo += l.pop(0)
print(l_roubo)

l[0] = 'X'
l[1] = 'Y'
l[2] = 'Z'
print(l)

l.insert(0, 'A')
print(l)