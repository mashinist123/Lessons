# # put your python code here
# import math
# a = math.pi
# print(format(a, '.3f'))
#
# # put your python code here
# a = float(input())
# print(f"Вы ввели число {a}")
#
import lst as lst

# put your python code here
# x = float(input())
# x = format(x, '.2f').split(".")
# x = int(x[-1])
# print(x > 50)


#Ввод 2х значений каждое с новой строки
# a, b = str(input()), str(input())
# print(a, b)


# #Ввод значений на одной строке через пробел
# a, b = input().split()
# c = (a+' ')*2 + (b+' ')*3
# print(c)


# put your python code here
# a, b = input().split('/')  # '/' указывает через какой символ надо перечислять элементы, по умолчанию ставится пробел когда в скобках ничего
#
# print('Переменная a = ' + a + ' переменная b = ' + b)

# a, b = input().split()
# c = a in b
# d = a == b
# e = a > b
# d = a < b
# print(c, d, e, f, sep = " ")


# # put your python code here
# a, b = input().split()
# a = a[:len(b):]
# print(a, b)

# a = input()
# b = a.lower()
# print(a[0]+b[1:])


# a,b = map(int,input().split())
# print(max(a,b))

# a, b, c, d = input("city"), input('street'), int(input('buildind')), int(input ('flat number'))
# print(f'г. {a}, ул. {b}, д. {c}, кв. {d}')

# a = list(map(int, input().split()))
# print(a)

# marks = list(map(int, input().split()))
# a = (marks)
# print(round(a, 1))

# a = input(), input(), int(input()), float(input())*2
# a = list(a)
# a[1] = 'Пушкин'
# del a[2]
# a[3] *= 2
# print(a)



# lst = list(map(int, input().split()))
# lst = sorted(lst, reverse = True)
# print(*lst)

# a = input().split()
# cities = ["Москва", "Тверь", "Вологда"]
# lst= cities + a
# print(*lst)
print(ord('5'))

# a = input()
# lst = a.replace("+7", "8").replace('-', '')
# print("".join(lst))



# Сергей Михайлович Балакирев
# a = input().split()
# b = a[2:]
# a.pop(2)
# for i in a:
#     b.append(i[0]+'.')
# print(f'{b[0]} {b[1]}{b[2]}')

# lst = input().split()
# print(lst[2], lst[0][0]+'.'+lst[1][0]+'.')

# lst = list(map(int, input().split()))
# a = lst[-1] % 2 != 0
# lst.pop()
# lst.append(a)
# print(*lst)


# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#      ["Я", ["Python", "выучил"], "с", "каналом"],
#      ["Балакирев", "что", "раздавал?"]]
# a = str(t)
# print(type(a))

# a = list(map(int, input()))
# if sum(a[0:3]) == sum(a[3:]):
#     print('ДА')
# else:
#     print('НЕТ')


# put your python code here
# m, n = map(int, input().split())
# a = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#
#
# if 0 < n - 1 and n + 1 <= a[m-1]:
#     print(f'{(str(m)).rjust(2, "0")}.{(n-1):02} {(str(m)).rjust(2, "0")}.{(n+1):02}')
# elif n-1 <= 0:
#     if m==1:
#         print (f'12.{(a[11]):02} {(str(m)).rjust(2, "0")}.{(n+1):02}')
#     else:
#         print(f'{(str(m-1)).rjust(2, "0")}.{(a[m-2]):02} {(str(m)).rjust(2, "0")}.{(n+1):02}')
# else:
#     if m == 12:
#         print(f'{(str(m)).rjust(2, "0")}.{(n-1):02} 01.01')
#     else:
#         print(f'{(str(m)).rjust(2, "0")}.{(n-1):02} {(str(m+1)).rjust(2, "0")}.01')


# a = 'privet'
# print(a[::-1])

a, b, c = map(int, input().split())
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a = m[a-1] if m[a-1] != 'до' and m[a-1] != "фа" else '#'+ m[a-1]
print(a)