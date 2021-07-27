a = '`1`'
b = 'fdsgfargareg'
for i in a:
    if i == '`':
        b = a.replace('`', '')
print(b)
