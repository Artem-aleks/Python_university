import sqlite3

def four_task():
    data_base = sqlite3.connect('data_base.db')  # Создаем базу данных
    cur = data_base.cursor()  # Для выполнения запросов

    cur.execute("""CREATE TABLE IF NOT EXISTS users (full_name TEXT,birth_year INTEGER,post TEXT);""")

    mass_list = []
    while True:
        print("Введите ФИО пользователя или стоп слово - Стоп")
        full_name = input()
        if full_name == "Стоп":
            break
        else:
            mass_list.append(full_name)
            print("Введите год рождения")
            birth_year = int(input())
            mass_list.append(birth_year)
            print("Введите род деятельности")
            post = input()
            mass_list.append(post)
            cur.execute("INSERT INTO users VALUES (?, ?, ?)", mass_list)
            mass_list.clear()

    print("Содержимое базы данных:")

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    i = 1

    for user in users:
        print("Пользователь номер -", i)
        print("ФИО: ", user[0])
        print("Год рождения: ", user[1])
        print("Род деятельности: ", user[2])
        i = i + 1

    data_base.commit()
    data_base.close()

four_task()