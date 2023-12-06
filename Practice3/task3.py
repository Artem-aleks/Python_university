from flask import Flask, render_template, request


def third_task():
    app = Flask(__name__)  # Создаем объект класса

    @app.route('/', methods=['GET', 'POST'])  # привязываем к url
    def url_adress():
        if request.method == 'POST':  # Post запрос-отправка информации, get-извлечение информации
            text = request.form['text']  # Принимаем запрос и передаем данные в файл
            with open('data_localhost.txt', 'a+') as file:
                file.write(text + '\n')

        with open('data_localhost.txt', 'r') as file:
            file_1 = file.read()

        return render_template('index.html', content=file_1)

    if __name__ == '__main__':
        app.run(host="localhost", port=3000)


third_task()
