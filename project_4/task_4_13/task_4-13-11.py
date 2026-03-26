n = int(input("Введите количество элементов массива: "))
A = []
print("Введите элементы массива: ")
for i in range(n):
    A.append(int(input())) #добавляем каждый элемент в массив
i = 0
sum = 0
count = 0
while i < n:
    if i % 2 == 0:
        sum = sum + A[i]
        count = count + 1
    i = i + 1
mean = sum / count    
print("Среднее арифметическое среди всех элементов в произвольно заданном массиве с четными индексами: ", sum)   