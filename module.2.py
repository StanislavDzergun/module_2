def get_password(number):                               #Создаем функцию
    password = ''
    for i in range(1, number):                          #Создаем цикл с возвратом последовательности чисел
        for j in range(2, number):
            if j <= i:                                  #Создаем условие
                continue                                #Пропускаем операцию при условии=True
            if number % (i + j) == 0:                   #Создаем еще одно условие при котором определяем четность
                password += str(i) + str(j)
    return password                                     #Завершаем создание функции

n = int(input('Введите целое число от 3 до 20: ')) #Создаем запрос ввода с клавиатуры

result = get_password(n)                           #Создаем выполнение подбора пароля при вводе определенного числа
print('Пароль:', result)                                 #Выводим на экран