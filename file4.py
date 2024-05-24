fruits = ["Яблоко",  "Банан","Мандарин", "Киви"]
print(fruits[0])  
print(fruits[3]) 
print(len(fruits))
print(fruits[len(fruits) - 1])

fruits.append("Апельсин")
fruits.append("виноград")
fruits.append("Дыня")

fruits.pop(0)
fruits.pop()

for f in fruits:
    print(f)

while True:
    num = input("Введите число: ")
    if num == "1":
        fruits.append(input("Введите название фрукта: "))
        print("Фрукт добавлен!")
    elif num == "2":
        fruits.pop(0)
        print("Первый фрукт удален! ")
    elif num == "3":
        fruits.pop()
        print("Последний фрукт удален!")
    elif num == "4":
        print("Фрукты:")
        print("--------------------")
        for f in fruits:
            print(f)
        print("--------------------")


























































