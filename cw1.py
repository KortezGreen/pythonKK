"""
    a = 'napis \ndrugi napis'
print(a)
b = 5
c = 5.5
print(b, c)
d = 5+3j
print(d)

e=c+d
print(e)
f=c//b
print(f)
g= c%b
print(g)
h =b**2
print(h)
i=b**1/2
j = pow(b,1/2)
print(i)
print(j)

listy = [6]
print(listy)

owoce = [3]
owoce.insert(1, 'Figa')
print(owoce)

slownik = {'a':2, 1:2, 4: 'ab'}
print(slownik)
print(slownik[4])
slownik['klucz'] = 'wartosc'
print(slownik)

print('a=%(zm)d' % {'zm':12})
napis = 'a={}, b={}'
print(napis.format(12,12))

a=67
b=55
if a<b:
    print(a)
elif b<a:
    print(b)
else:
    print(a, b)

a = input('podaj a: ')
b = input('podaj b: ')
c = input('podaj c: ')
d = input('podaj d: ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b>a and c<a:
    print(a)
else:
    print(b+c)

for x in range(1, 6, 1):
    print(x)
else:
    print('koniec for')


lista =[6]

for i in range(0, len(listy)):
    print(i)
"""

# while licznik != len(listy):
#     print(listy[licznik])
#     licznik +=1

licznik = 0
liczby = [1,2,2,2,4,5,6]
for i in (liczby):
    if i == 2:
        liczby.remove(i)
    print(liczby)