
from datetime import *#добавляем библиотеку времени



def temporary_timelaps(main_time):#содаем функцию которая считывает ошибки, если пользователь некорректно ввел время
    if len(main_time) != 8:
        return "Неверный формат, попробуйте еще раз"
    else:
        if int(main_time[0:2]) > 23:
            return "Неверный формат часов, попробуйте еще раз"
        elif int (main_time[3:5]) > 59:
            return "Неверный формат минут, попробуйте еще раз"
        elif int(main_time[6:8]) > 59:
            return "Неверный формат секунд, попробуйте еще раз"
        else:
            return "Отлично!"


while True:#бесконечный цикл который будет возвращать время установки будильника
    main_time = input("Добро пожаловать в приложение будильник!\nВведите время, на которое вы хотите поставить будильник в следующем формате \'HH:MM:SS\'\nВремя будильника:")
    temporary = temporary_timelaps(main_time)#задаем переменной значение функции
    print(f"Будильник установлен на время {main_time}...\nПриятного отдыха!")
    break
#присваиваем переменным часов, минут и секунд их порядок (HH:MM:SS)
main_hour = int(main_time[0:2])
main_min = int(main_time[3:5])
main_sec = int(main_time[6:8])


while True:
    imp = datetime.now()#now - обрабатывает и принимает актуальные даннеы времени с компьютера

    time_min = imp.minute
    time_hour = imp.hour
    time_sec = imp.second
#если все значения выше совпадают со временем на компьютере, то у нас выводит надпись "Время вставать!"
    if main_hour == time_hour:
        if main_min == time_min:
            if main_sec == time_sec:
                print("Время вставать!\nБлагодарим за то что воспользовались нашем приложением")
                break






