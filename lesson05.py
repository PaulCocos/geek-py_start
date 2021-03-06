# coding : utf-8 

import os
import sys
import psutil # не удалось установить, поставил с помощью сайта https://www.lfd.uci.edu/~gohlke/pythonlibs/
import shutil


# функция удаления файлов с расширением .dupl в папке dirr 
# возвращает число удаленных файлов
def del_duplicate(file_list):
	i = 0
	j = 0 # счетчик удаленных файлов
	while i < len(file_list):
		curfile = file_list[i]
		if curfile.endswith('.dupl') : # проверяем, есть ли .dupl - интересный метод!
			fullname = os.path.join(dirr, curfile) # формируем полное имя файла из относительного
			os.remove(fullname)
			j += 1
			print("Удален файл: ", curfile)
		i += 1
	return(j)

# Урок 5. Программа полезных утилит
print("Программа полезных утилит")
# name = input("Введите ваше имя: ")
# print("Привет, программист", name, " !")

action = ''
while action != 0:
	os.system('cls')
	print("Выберите, что вы хотите сделать?")
	print("[1] вывести список файлов")
	print("[2] вывести информацию о системе")
	print("[3] вывести список процессов")
	print("[4] создать дубликаты файлов")
	print("[5] дублирование файла")
	print("[6] удаление .dupl файлов в заданной папке")
	print("[0] закончить работу")

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
	elif action == 4:
		print("Создание дубликатов файлов")
		file_list = os.listdir()
		i = 0
		while i < len(file_list):
			oldfile = file_list[i]
			if os.path.isfile(oldfile): # проверяем не папка ли это
				newfile = oldfile + ".dupl"
				shutil.copy(file_list[i], newfile)
			i += 1
	elif action == 5:
		print("Задайте файл для дублирования")
		fil = input()
		newfile = fil + ".dupl"
		shutil.copy(fil, newfile)
	elif action == 6:
		print("задайте имя папки для поиска")
		dirr = input()
		file_list = os.listdir(path=dirr)
		print(file_list)
#
		n_deleted=del_duplicate(file_list)
		print("Всего удалено: ", n_deleted, ". Нажмите Enter")
		input()
#
	elif action == 0:
		print("=== работа закончена ===")
	else:
		pass
	print(">нажмите пробел<")
	input()
	

	


