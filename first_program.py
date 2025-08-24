# # Самый простой способ найти цифры из числа
# # 123456789  // 1 % 10 ---> 9                   (единицы)

# # 123456789   // 10 % 10 ---> 8                (десятки)

# # 123456789  // 100 % 10 ---> 7               (сотни)

# # 123456789  // 1000 % 10 ---> 6             (тысячи)

# # 123456789  // 10000 % 10 ---> 5           (десятки тысяч)

# # 123456789  // 100000 % 10 ---> 4         (сотни тысяч)

# # 123456789  // 1000000 % 10 ---> 3       (миллионы)

# # 123456789  // 10000000 % 10 ---> 2     (десятки миллионов)

# # 123456789  // 100000000 % 10 ---> 1   (сотни миллионов)

# # Способ через str
# # num = 17
# # num=str(num)
# # a = num[1]
# # b = num[0]
# # print(a)
# # print(b)

# # Способ через цикл
# # num = '497'
# # for i in num:
# #     print(i)

# # Способ по формуле
# # num = 754
# # a = num % 10             # вычисляем последнюю цифру числа
# # b = (num % 100) // 10    # вычисляем среднюю цифру числа
# # c = num // 100           # вычисляем первую цифру числа

# 6 основных операторов сравнения.
# if x > 7   → если x больше 7
# if x < 7   → если x меньше 7
# if x >= 7  → если x больше или равен 7
# if x <= 7  → если x меньше или равен 7
# if x == 7  → если x равен 7
# if x != 7  → если x не равен 7


# num1 = 6104#int(input())
# num2 = 0#int(input())
# opr = '/'#input()
# if opr == '+':
#     print(num1 + num2)
# elif opr == '-':
#     print(num1 - num2)
# elif opr == '*':    
#     print(num1 * num2)
# elif opr == '/':    
#     if num1 != 0 and num2 != 0:
#         print(num1 / num2)
#     else:
#         print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')
 
# color1 = input()
# color2 = input()
# if color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 == 'красный':
#     print('фиолетовый')
# elif color1 == 'красный' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'красный':
#     print('оранжевый')
# elif color1 == 'синий' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'синий':
#     print('зеленый')

# x = 12#int(input())
# if x == 0:
#     print('зеленый')
# if x < 0 or x > 36:
#     print('ошибка ввода')
# elif 1 <= x <= 10:
#     if x % 2 == 0:
#        print('черный')
#     else:
#         print('красный')
# elif 11 <= x <= 18:
#     if x % 2 == 0:
#        print('красный')
#     else:
#         print('черный')
# elif 19 <= x <= 28:
#     if x % 2 == 0:
#        print('черный')
#     else:
#         print('красный')
# elif 29 <= x <= 36:
#     if x % 2 == 0:
#         print('красный')    
#     else:
#         print('черный')
# number_stolb1 = int(input())
# number_cletki1 = int(input())
# number_stolb2 = int(input())
# number_cletki2 = int(input())
# if number_stolb1 % 2 == 0:
#     if number_cletki1 % 2 == 0:
#         print('YES')
#     else:
#         print('NO')
# elif number_stolb2 % 2 == 0:
#     if number_cletki2 % 2 == 0:
#         print('YES')
# else:
#     print('NO')
# elif number_stolb2 % 2 == 0:
#     if number_cletki2 % 2 == 0:
#         print('YES')
# else:
#     print('NO')
    
# x  = 5#int(input())
# if x == 1:
#     print('I')
# elif x == 2:
#     print('II')
# elif x == 3:
#     rint('IV')
# elif x == 4:
#     print('IV')
# elif x == 5:
#     print('V')
 

    #Если разность x1 и y1 равны разности x2 и y2. Или если суммы равны ,значит да. Иначе нет !ХОД СЛОНА!

dog_age = 12#float(input())
if 0 < dog_age <= 2:
    print(dog_age * 10.5)
else:
    print(21 + (dog_age -2) *4)



