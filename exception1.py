"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    flag = True
    while flag:
        try:
            user_say = input()
            for i in d.keys():
                if user_say == i:
                    print(d[i])
                    flag = False
        except KeyboardInterrupt:
            print('Пока!')
            break

d = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}

if __name__ == "__main__":
    ask_user()
