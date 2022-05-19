import shutil

path = str(input("Введите Путь к файлу: "))
try:
    shutil.rmtree(path)
    print(path, " удалена.")
except OSError as error:
    print("Возникла ошибка.")