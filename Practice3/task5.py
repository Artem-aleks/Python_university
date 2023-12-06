from flask import Flask, render_template, request
import sqlite3

def five_task():
    app = Flask(__name__)

    @app.route('/')
    def data_base():
        data_base = sqlite3.connect('data_base.db')  # Создаем базу данных
        cur = data_base.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (full_name TEXT,birth_year INTEGER,post TEXT);""")
        data_base = cur.fetchall()
        cur.close()
        return render_template('index1.html', data=data_base)

    @app.route('/add', methods=['POST'])
    def add():
        data_base = sqlite3.connect('database.db')
        cur = data_base.cursor()
        string = request.form['string']
        cur.execute('INSERT INTO strings (string) VALUES (?)', (string,))
        data_base.commit()
        data_base.close()
        return 'success'

    @app.route('/delete', methods=['POST'])
    def delete():
        data_base = sqlite3.connect('database.db')
        cur = data_base.cursor()
        string_id = request.form['string_id']
        cur.execute('DELETE FROM strings WHERE id=?', (string_id,))
        cur.commit()
        cur.close()
        return 'success'

    if __name__ == '__main__':
        app.run(host="localhost", port=7000)

five_task()