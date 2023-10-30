# Python
a = int(input("Введіть а від 1 до 100: "))

while a < 1 or a > 100:
    a = int(input("Введіть ще раз a: "))

b = int(input("Введіть b від 1 до 100: "))

while b < 1 or b > 100:
    b = int(input("Введіть ще раз b: "))

if a < b:
    x = b / a - 1
elif a == b:
    x = -295
else:
    x = (a - 235) / b

print("Результат обчислення вираз:", x)
