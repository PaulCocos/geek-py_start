# coding : utf-8 

import os
import sys
import psutil # не удалось установить, поставил с помощью сайта https://www.lfd.uci.edu/~gohlke/pythonlibs/

# Урок 3. Программа полезных утилит
print("Программа полезных утилит")
# name = input("Введите ваше имя: ")
# print("Привет, программист", name, " !")
print("Выберите, что вы хотите сделать?")
print("[1] вывести список файлов")
print("[2] вывести информацию о системе")
print("[3] вывести список процессов")

action = int(input())
if action == 1:
	print("Список файлов: ", os.listdir())
elif action == 2:
	print("Имя текущей папки:", os.getcwd())
	print("Операционная система:", sys.platform)
	print("Кодировка файловой системы:", sys.getfilesystemencoding())
	print("Логин пользователя:", os.getlogin())
	print("Количество процессоров в системе:", os.cpu_count())
elif action == 3:
	print(psutil.pids())

else:
	print("Вы выбрали что-то непонятное!")


	


