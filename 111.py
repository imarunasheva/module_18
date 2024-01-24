allPrice = 0 #общая стоимость билетов
visitorAge = {} #объявляем словарь для данных 'посетитель:возраст' при покупке более 1 билета

countTickets = int(input("Сколько билетов желаете приобрести: "))
if countTickets < 0:
    raise ValueError('Пожалуйста, введите положительное значение')
elif countTickets == 1:
    age = int(input("Укажите возраст посетителя: "))
    if age <= 0:
        raise ValueError('Пожалуйста, введите корректное значение')
    elif 0 < age < 18:
        allPrice += 0
    elif 18 <= age < 25:
        allPrice += 990
    elif age >= 25:
        allPrice += 1390
elif countTickets > 1:
    for i in range(1, countTickets+1):
        visitorAge[i] = int(input(f"Укажите возраст {i} посетителя: "))
        if visitorAge[i] <= 0:
            raise ValueError('Пожалуйста, введите корректное значение')
        elif 0 < visitorAge[i] < 18:
            allPrice += 0
        elif 18 <= visitorAge[i] < 25:
            allPrice += 990
        elif visitorAge[i] >= 25:
            allPrice += 1390
if countTickets > 3:
    allPrice *= 0.9

print(f'Итоговая стоимость билета {"%.2f" % allPrice} руб.')