# Дано п’ять дійсних чисел: x, y, r.
# Напишіть функцію для перевірки, чи належить точка (x, y) колу з
# центром в початку координат і радіусом r.
# Якщо точка належить колу, виведіть слово YES, інакше виведіть слово NO
import math

x = float(input("Координата х = "))
y = float(input("Координата y = "))
r = float(input("Радіус = "))

d = math.sqrt(x**2 + y**2)
if d>r :
    result = "NO"
else:
    result = "YES"

print(result)

#x = 0, y = 5, r = 3 - NO
#x = 5, y = 0, r = 3 - NO
#x = 2, y = 2, r = 3 - YES
#x = 1, y = 1, r = 2 - YES
