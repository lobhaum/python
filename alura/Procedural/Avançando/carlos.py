total = 0
palavra = 'Python Rocks!'
acabou = False
while(not acabou):
    acabou = (total == len(palavra))
    total += 1
print(total - 1)
