# Реализовать консольное приложение заметки, с 
# - сохранением,
# - чтением,
# - добавлением,
# - редактированием и
# - удалением заметок.
# Заметка должна содержать 
# - идентификатоp
# - заголовок,
# - тело заметки и
# - дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат
# (разделение полей рекомендуется делать через точку с запятой).
# Реализацию пользовательского интерфейса студент может делать как ему удобнее,
# можно делать как параметры запуска программы (команда, данные),
# можно делать как запрос команды с консоли и последующим вводом данных,
# как-то ещё, на усмотрение студента.

import pandas as pd
from datetime import datetime


tasks = dict()
idTask = 0
dataFile = 'Tasks.csv'
current_datetime = datetime.now().date()


from enum import Enum

class HeaderTask(Enum):
    """
    Enum Description: 
    """
    Homework = "HOMEWORK"
    Job = "JOB"
    Study = "STUDY"
    Training = "TRAINING"

# Write phonebook in dataFile.csv
def write_tasks_in_file():
   with open(dataFile, 'w') as data:
    for key, value in tasks.items():
        data.write(f'Задача номер: {key}\n  Время создания или послденего изменения: {value[0]}\n   Заголoвок {value[1].value}\n      Задача: {value[2]}\n')

#Add task
def add_task():
    dateTask = current_datetime
    header = header_choice()
    task = input("Введите задачу: ")
    global idTask
    idTask = idTask + 1
    tasks[idTask] = [dateTask, header, task]
    write_tasks_in_file()

# Choice header
def header_choice():
    header = HeaderTask.Training
    choiceHeader = int(input(f'Выберите заголовок:\n1 = {header.Homework.value}\n2 = {header.Job.value}\n3 = {header.Study.value}\n4 = {header.Training.value}\n'))
    match (choiceHeader):
        case (1):
            header.Homework.value 
        case (2):
            header.Job.value
        case (3):
            header.Study.value
        case (4): 
            header.Training.value
    return header


def print_data_contact(key, value):
    print(f'Задача номер: {key}  Время создания или послденего изменения: {value[0]}')
    print(f'Заголoвок{value[1]}')
    print(f'Задача: {value[2]}')


# Read tasks
def read_tasks():
    with open(dataFile, 'r') as data:
        for (key, value) in tasks.items():
            dictionary = data.read()
            print_data_contact(key, value)
        return dictionary
    
# Change data
def change_data():
    pos_task = int(input('Введите номер задачи для измении: '))
    tasks[pos_task]
    do_with_task = int(input('Нажмите номер соответствующего изменения:\n1 - изменить задачу\n2 - удалить задачу'))
    if do_with_task == 1:
        new_data = input('Введите новоую задачу:')
        tasks[pos_task][0] = new_data
        write_tasks_in_file()
    elif do_with_task == 2:
        del tasks[pos_task]
        write_tasks_in_file()



add_task()
add_task()
read_tasks()
change_data()
read_tasks()
