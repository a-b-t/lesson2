"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    if age <=7:
        return 'Ты ходишь в детский сад'
    elif age <=16:
        return 'Ты учишься в школе'
    elif age <=21:
        return 'Ты учишься в ВУЗе'
    else:
        return 'Ты работаешь'

input_age = int(input('Введите возраст: '))
result = main(input_age)
print(result)
