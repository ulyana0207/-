x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))
f = float(input("Введите четвёртое число: "))
min = x
if y < min:
    min = y
if z < min:
    min = z
if f < min:
    min = f
print("Минимальное:", min)