import random
import shutil
import os

print("Введите номер задания:")
number_task = int(input())


def one_task():
    print("Введите время в секундах:")
    time_drive = int(input())

    print("Начальная координата отправления равняетсяя нулю(x = 0)")
    print("Ускорение и скорость - рандомные значения")

    speed = random.choice(range(5, 25))
    boost = random.choice(range(1, 10))
    print("Скорость: ", speed)
    print("Ускорения: ", boost)

    x = speed * time_drive + float((boost * (time_drive ** 2)) / 2)
    print("Вывод конечного значения:", x)


def two_task():
    print("Введите целое число:")
    number = int(input())
    sum_number = 0

    while number != 0:
        sum_number += number % 10
        number //= 10

    print("Сумма цифр числа:", sum_number)


def three_task():
    product = ["рыба", "мясо", "овощи", "фрукты", "зелень", "орехи", "приправа", "электроника",
               "хозяйственные принадлежности", "продукты для домашних животных", "лекарство", "одежда", "инструменты",
               "товары для стройки"]

    product_1 = set()
    product_2 = set()
    product_1.update(random.choices(product, k=random.randint(15, 25)))
    product_2.update(random.choices(product, k=random.randint(15, 25)))

    print("Вывод первого множества:")
    print(product_1)
    print("Вывод второго множества:")
    print(product_2)

    print("Вывод уникальных товаров:")
    print(*(set(product_1) ^ set(product_2)))


def four_task():
    mass_name = ["Богданов Семён Матвеевич", "Калинина Анастасия Марковна", "Лукьянов Александр Антонович",
                 "Николаева Алёна Михайловна", "Жукова Дарья Даниэльевна", "Смирнов Илья Никитич",
                 "Михеев Михаил Матвеевич", "Матвеев Иван Никитич", "Лебедев Арсений Романович"]
    mass_post = ["Начальник", "Хозяин", "Главный металлург", "Менеджер", "Диспетчер", "Инженер по качеству",
                 "Переводчик"]
    mass_secret = ["Есть доступ", "Нет доступа"]

    print("Введите кол-во работников:")
    numbers = int(input())

    dict_1 = {}
    i = 1

    while i <= numbers:
        dict_1[i] = {"ФИО": random.choice(mass_name), "Возраст": random.randint(20, 55),
                     "Должность": random.choice(mass_post), "Номер рабочего места": random.randint(1, 100),
                     "Наличие доступа к тайне": random.choice(mass_secret)}
        i += 1

    dict_1 = list(dict_1.items())
    print("Вывод базы данных:")
    print(dict_1, "\n")
    kol_vo = 1

    for i in dict_1:
        print(kol_vo, "Работник")
        print("ФИО:", i[1]['ФИО'])
        print("Возраст:", i[1]['Возраст'])
        print("Должность:", i[1]['Должность'])
        print("Номер рабочего места:", i[1]['Номер рабочего места'])
        print("Наличие доступа к тайне:", i[1]['Наличие доступа к тайне'], "\n")
        kol_vo += 1
def five_task():
    number = (random.randint(0, 1))
    print("Число -", number)
    try:
        10 / number
    except ArithmeticError:
        print("Деление на ноль")
    else:
        print("Успешно -", 10 / number)


def six_task():
    print("Задание - запись в файл")
    print("Введите строку, которую хотите занести в файл:")
    data = input()
    my_file = open("TestFile.txt", "a+")
    my_file.write(data + '\n')
    print("Данные записаны в файл")
    my_file.close()


def seven_task():
    print("Задание - чтение файла")
    my_file = open("TestFile.txt", "r")
    my_file_1 = my_file.read()
    check_size = os.stat("TestFile.txt").st_size
    if check_size > 0:
        print(my_file_1)
    else:
        print("Файла нет")
    my_file.close()


def eight_task():
    print("Задание - сделать копию файла")
    shutil.copyfile("TestFile.txt", "TestFile1.txt")
    os.remove("TestFile.txt")
    print("Копия файла сделана")


if number_task == 1:
    one_task()
elif number_task == 2:
    two_task()
elif number_task == 3:
    three_task()
elif number_task == 4:
    four_task()
elif number_task == 5:
    five_task()
elif number_task == 6:
    six_task()
elif number_task == 7:
    seven_task()
elif number_task == 8:
    eight_task()
