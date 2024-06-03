# Функция умножения
def multiply(num1, num2):
    return num1 * num2

# Функция сложения
def sum(num1, num2):
    return num1 + num2

def playCalc():
    answer = input("Давайте сделаем вычисления! 1 - умножение, 2 - сложение или нажмите любую клавишу для выхода: ")
    if answer == "1":
        initCalc(answer)
    elif answer == "2":
        initCalc(answer)
    else:
        print("Удачи!")
        

def initCalc(type):
    if type == "2":
        numbers = input("Введите 2 числа через пробел для сложения: ") # "1 5"
        splitedString = numbers.split(" ") # ["1",  "5"]
        num1 = int(splitedString[0]) # "1" -> 1
        num2 = int(splitedString[1]) # "5" -> 5
        print("Ответ: " + str(sum(num1, num2))) # 6 -> "6"
    elif type == "1":
        numbers = input("Введите 2 числа через пробел для умножения: ")
        splitedString = numbers.split(" ")
        # ["1",  "5"]
        num1 = int(splitedString[0]) # "1" -> 1
        num2 = int(splitedString[1]) # "5" -> 5
        print("Ответ: " + str(multiply(num1, num2)))
    
    playCalc()
    

playCalc()