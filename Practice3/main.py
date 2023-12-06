from flask import Flask, render_template, request
import sqlite3

print("4 практика.Введите номер задания")
print("1 - Задание.Веб приложение")
print("2 - Задание.Консольное приложение")
print("3 - Задание.Веб приложение с кнопками")
print("4 - Задание.Приложение для записи в БД информации")
print("5 - Задание.Веб приложение для вывода БД")

number_task = int(input())


def first_task():
    app = Flask(__name__)  # объект класса(интерфейс для взаимодействия сервера с фреймворком)

    @app.route('/')  # привязка url к функции
    def index():
        return 'hello world'

    if __name__ == "__main__":  # запуск
        app.run(host="localhost", port=8000)


def second_task():
    MyFile = open("TestFile", "a")
    print("Введите данные для записи файл.Стоп слово - стоп слова")
    text = input()
    try:
        while text != "стоп слова":
            MyFile.write(text + '\n')
            text = input()
    finally:
        MyFile.close()
    print("Данные записаны в файл")

def third_task():
    app = Flask(__name__)  # Создаем объект класса

    @app.route('/', methods=['GET', 'POST'])  # привязываем к url
    def url_adress():
        if request.method == 'POST':  # Post запрос-отправка информации, get-извлечение информации
            text = request.form['text']  # Принимаем запрос и передаем данные в файл
            with open('data_localhost.txt', 'a') as file:
                file.write(text + '\n')

        with open('data_localhost.txt', 'r') as file:
            file_1 = file.read()

        return render_template('index.html', content=file_1)

    if __name__ == '__main__':
        app.run(host="localhost", port=8000)



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

def five_task():
    app = Flask(__name__)

    @app.route('/')
    def data_base():
        mass_list = ["Алексанов Артем Юрьевич", 2004, "Студент"]
        data_base = sqlite3.connect('data_base.db')  # Создаем базу данных
        cur = data_base.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (full_name TEXT,birth_year INTEGER,post TEXT);""")
        data = c.fetchall()
        conn.close()
        return render_template('index1.html', data=data)

    @app.route('/add', methods=['POST'])
    def add():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        string = request.form['string']
        c.execute('INSERT INTO strings (string) VALUES (?)', (string,))
        conn.commit()
        conn.close()
        return 'success'

    @app.route('/delete', methods=['POST'])
    def delete():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        string_id = request.form['string_id']
        c.execute('DELETE FROM strings WHERE id=?', (string_id,))
        conn.commit()
        conn.close()
        return 'success'

    if __name__ == '__main__':
        app.run(host="localhost", port=7000)

if number_task == 1:
    print("1 - Задание.Веб приложение")
    first_task()
if number_task == 2:
    print("2 - Задание.Консольное приложение")
    second_task()
if number_task == 3:
    print("3 - Задание.Веб приложение с кнопками")
    third_task()
if number_task == 4:
    print("4 - Задание.Приложение для записи в БД информации")
    four_task()
if number_task == 5:
    print("5 - Задание")
    five_task()

