# s = 'tehnikum' cherez # delayem kommenti
s = [1, 2, 3, 4]# this is list of element
print(s[2:100])
print(s[-1])
print(s[len(s)-1]) # to je samoye chto i s[-1]

s = 'tehnikum'
print(s[1:-3]) # poydet te obratno, poydet s 1go elementa do -3go
print(s[0:4:2]) # poslednyaya 2 eto shag
print(s[6:0:-1]) # perviy vkluyaetsa, vtoroy net
print(s[::-1]) # v obratnom poryadke

s = '+998 90 567 5678'
print(s[-1:])

# kod dlya resheniya odnoy iz proshlix domashek bez ciklov
x = int(input('Vvedi chislo: '))
print(list(range(1, x + 1)))
print(sum(list(range(1, x + 1))))

summa = 0
for i in range(20):
    summa = summa + i
    print('summa', summa, 'i', i)

if 2 in range(10):
    print(True)

a = []
for i in range(10):
    a.append(input())
    print(a)


for i in ['a', 'b', 'c']:
    print(i)


for i in [['a', 'b', 'c'],
          ['d', 'e' 'f']]:
    print(i[0])



for i in [['Anna', 19, 'female'],
          ['Daniel', 22, 'male'],
          ['Vasiliy', 10, 'male']]:
    if i[1] > 18:
        print(i[0])
    print(i[1] > 18)
male_list = []
    if i[2] == 'male':
        male_list.append(i[0])
        print(male_list)

male_counter = 0
database = [['Anna', 19, 'female'],
          ['Daniel', 22, 'male'],
          ['Vasiliy', 10, 'male']]
for i in database:
    if i[2] == 'male':
        male_counter += 1
print(male_counter)




