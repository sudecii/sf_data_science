"""Игра загадай число
Компьютер сам загадывает и сам угадывает
"""

import numpy as np 

def random_predict(number:int=1) -> int: #через двоеточие указываем тип данных, который вводим, а через равно стандарт значение этого числа, а стрелочкой, то что у нас на выходе получается
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)#предполагаемое число
        if number == predict_number:
            break #выход из цикла, если угадали число
    return(count)       

def score_game(random_predict)->int: #будем запускать тысячу раз, и выведем среднее значение
    """За какое количество в среднем угадывает за 1000 подходов наш алгортим

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #будем сохранять кол-во попыток
    np.random.seed(1) #ри одинаковых seed последовательность тоже будет одинаковая.Но seed нужен для того, чтобы при каждом запуске алгоритм выдавал разные значения (для этого вы должны подавать каждый раз разный seed).
    random_array = np.random.randint(1, 101, size=(1000))#загадали список тысячи чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))#находим среднее кол-во попыток
    print(f'Ваш алгоритм угадывает в среднем за: {score}')
    return(score)
#print(f'Количество попыток: {random_predict(10)} ')

if __name__ == "__main__":
    #RUN
    score_game(random_predict)
    