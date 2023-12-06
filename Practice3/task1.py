from flask import Flask, render_template, request

def first_task():
    app = Flask(__name__)  # объект класса(интерфейс для взаимодействия сервера с фреймворком)

    @app.route('/')  # привязка url к функции
    def index():
        return 'hello world'

    if __name__ == "__main__":  # запуск
        app.run(host="localhost", port=4000)

first_task()