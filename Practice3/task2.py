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

second_task()