import math
from mod import calculate_average


def calculate_z():
  m = float(input("Введіть число m: "))
  if m >= 0:
    z = math.sqrt(m) + 10
    return z
  else:
    return "Некоректне значення m. Введіть число більше або дорівнює нулю."


while True:
  choice = int(
      input(
          "Виберіть опцію (1 - обчислити z, 2 - знайти середнє арифметичне парних чисел): "
      ))
  if choice == 1:
    result = calculate_z()
    print("Результат обчислення z:", result)
    break
  elif choice == 2:
    x = int(input("Введіть початкове число x: "))
    y = int(input("Введіть кінцеве число y: "))
    average = calculate_average(x, y)
    print("Середнє арифметичне парних чисел від", x, "до", y, "дорівнює",
          average)
    break
  else:
    print("Невірний вибір опції. Оберіть 1 або 2.")
