i = input('Digite: ')
s = ''
for c in i:
    if i.lower() in 'aeiou':
        i.append('*')
    i.append(i)
