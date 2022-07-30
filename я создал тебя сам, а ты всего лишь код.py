# Считывание и задаём переменные 
file = open('26-2.txt', 'r')
n, m = map(int, file.readline().split(' '))
olympiadniki = []
typical = []
# Тело программы
for i in range(n):
    ict, russian, maths, olympiad = map(int, file.readline().split(' '))
    if olympiad == 1:
        olympiadniki.append(ict)
    else:
        change = [ict+russian+maths,ict]
        typical.append(change)


last = m-len(olympiadniki)
typical.sort(key=lambda a: (-a[0], -a[1]))
minb = typical[last][0]
ans = 0
for i in range(last):
    if typical[i].count(minb)==1:
        ans += 1
print(ans,int(sum(olympiadniki)/len(olympiadniki)))

