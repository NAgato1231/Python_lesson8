
#1 задача ================================
a=int(input("Введите первый аргумент: "))
b=int(input("Введите второй аргумент: "))
c=input("Введите третий аргумент: ")

if c == "+":
      print(a, "+", b, "=", a + b)
elif c == "-":
      print(a, "-", b, "=", a - b)
elif c == "*":
      print(a, "*", b, "=", a * b)
elif c == "/":
      print(a, "/", b, "=", a/b)
else:
      print("Неизвестная операция ")

#2 задача =======================================

def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_year_leap(142), "142")
print(is_year_leap(144), "144")
print(is_year_leap(100), "100")
print(is_year_leap(400), "400")

#3 задача =========================================

def square(a):
    return "Периметр квадрата равен:  " + str(4 * a) + "\n" + "Площадь квадрата равна:  " + str(a**2) + "\n" + "длина квадрата " + str(a + a + a + a)

print(square(2))

#4 задача =========================================

def season(num):

   if num == 12 or 1 <= num <= 2:
       print("Зима")

   elif  3 <= num <= 5:
       print("Весна")

   elif 6 <= num <= 8:
       print("Лето")

   elif 9 <= num <= 11:
       print("Осень")

   else:
       print("Неверно введён номер месяца!")

n = int(input("Введите номер месяца (1-12): "))

season(n)

#5 задача =====================================

def bank (a, years):

    for i in range (years):
        a = a + (a/100*10)

    return (a)

result = bank (float(input("Введите сумму вклада: ")), int(input("На сколько лет: ")))

print (result)

#6 задача =======================================

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

print(is_prime(int(input("Введите число от 0 до 1000: "))))


