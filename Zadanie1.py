"""
Задание 1.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input("Ведите сколько км вы пробежали в первый день:"))
b = int(input("Ведите ск км в общем вы хотите пробежать:"))

day_x = 1
result = 1
while a < b:
    result = a + 0.1 * a
    day_x += 1
result =
    print(f"Вы достигнете нужных показателей на {day_x} день")
    """

a = int(input("Ведите сколько км вы пробежали в первый день:"))
b = int(input("Ведите ск км в общем вы хотите пробежать:"))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
print(f"Вы достигнете нужных показателей на {day} день")