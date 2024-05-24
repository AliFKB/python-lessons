import time
import sys

def conversation_about_numbers(answer):
    if answer.lower() == "числа":
        print(answer + " Ок, что идет после 21? 22 или 20. У тебя ровно 10 сек")
        timer = 10
        while timer >= 0:
            time.sleep(1)
            print(timer)
            timer -= 1

        answer2 = input("Ответ: ")
        
        if answer2 == "22":
            print("Правильно! Молодец!" )
        else:
            print("Попробуй еще раз!")
            init_conversation(True)
    else:
        print("Давай попробуем еще раз! и поболтаем о числах")
        init_conversation(True)   

def init_conversation(is_repeat):
    if is_repeat == True:
        print("давай пообщаемся повторно?")
    
    answer0 = input("Ответ: ")
    if answer0.lower() == "да" or answer0.lower() == "lf":
        print("ура о чем поболтаем?")
        answer = input("Ответ: ")
        conversation_about_numbers(answer)

    elif answer0.lower() == "числа":
        conversation_about_numbers("числа")
    elif answer0.lower() == "нет" or answer0.lower() == "ytn":
        print("ну пожалуйста")
    else:
        print("Давай до свиданья!") 

sys.modules[__name__] = init_conversation