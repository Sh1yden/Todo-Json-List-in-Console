import json
import os
from random import randint
import uuid

# Стандартная структура базы данных для моего TODO List:
# save_todo = {
#     "all_tasks": {
#         "task_id: 0": {
#             "task_name": "",
#             "task_description": "",
#             "task_date": "",
#             "task_status": "",
#             "task_priority": "",
#             "task_deadline": "",
#         }
#     }
# }


# Идея для следующего обновления:
# Создание меню для всех подменю:
# while True:
#         print("\nDelete Menu: ")
#         print("1. Delete All Tasks")
#         print("2. Delete Single Task")
#         print("3. Back to Main Menu")


save_todo = {"all_tasks": {}}


def newEmptyJsonFile():
    with open("save\\tasks\\save.json", "w") as json_file:
        json.dump(save_todo, json_file, indent=2)


def generateTasks():
    # Создание 100 фейковых задач:
    # Создание файла чисто для отладки некоторых функций:
    for i in range(0, 100):
        save_todo["all_tasks"][f"task_id: {i}"] = {
            "task_name": "",
            "task_description": "",
            "task_status": "",
            "task_date": "",
            "task_priority": "",
            "task_deadline": "",
        }

    with open("save\\tasks\\save.json", "w") as json_file:
        json.dump(save_todo, json_file, indent=2)


def ViewAllTasks():
    # Чтение файла:
    with open("save\\tasks\\save.json", "r") as json_save_file:
        read_save_file = json.load(json_save_file)

        print("Total tasks: ", len(read_save_file["all_tasks"]))

        # Вывод на экран всех задач по одной строке:
        for i in range(len(read_save_file["all_tasks"])):
            print(read_save_file["all_tasks"][f"task_id: {i}"])


def AddTask():
    # Чтение файла:
    with open("save\\tasks\\save.json", "r") as json_file:
        read_save_file = json.load(json_file)

    # Создание уникального идентификатора для каждой задачи:
    task_id = uuid.uuid4()

    # Создание задания и его полей:
    read_save_file["all_tasks"].update({f"task_id: {task_id}": {}})
    read_save_file["all_tasks"][f"task_id: {task_id}"].update({"task_name": ""})
    read_save_file["all_tasks"][f"task_id: {task_id}"].update({"task_description": ""})
    read_save_file["all_tasks"][f"task_id: {task_id}"].update({"task_date": ""})
    read_save_file["all_tasks"][f"task_id: {task_id}"].update({"task_status": ""})
    read_save_file["all_tasks"][f"task_id: {task_id}"].update({"task_priority": ""})
    read_save_file["all_tasks"][f"task_id: {task_id}"].update({"task_deadline": ""})

    # Заполнение полей задания:
    read_save_file["all_tasks"][f"task_id: {task_id}"]["task_name"] = str(
        input("Enter the name of the task: ")
    )
    read_save_file["all_tasks"][f"task_id: {task_id}"]["task_description"] = str(
        input("Enter the description of the task: ")
    )
    read_save_file["all_tasks"][f"task_id: {task_id}"]["task_status"] = str(
        input("Enter the status of the task: ")
    )
    read_save_file["all_tasks"][f"task_id: {task_id}"]["task_date"] = str(
        input("Enter the date of the task: ")
    )
    read_save_file["all_tasks"][f"task_id: {task_id}"]["task_priority"] = str(
        input("Enter the priority of the task: ")
    )
    read_save_file["all_tasks"][f"task_id: {task_id}"]["task_deadline"] = str(
        input("Enter the deadline of the task: ")
    )

    # Сохранение всех изменений в файле:
    with open("save\\tasks\\save.json", "w") as json_file:
        json.dump(read_save_file, json_file, indent=2)


def UpdateTask():
    pass


def DeleteTask():
    with open("save\\tasks\\save.json", "r") as json_file:
        read_save_file = json.load(json_file)

    task_id = int(input("Enter the task ID to delete: "))

    read_save_file["all_tasks"].pop(f"task_id: {task_id}")

    with open("save\\tasks\\save.json", "w") as json_file:
        json.dump(read_save_file, json_file, indent=2)


def MainMenu():
    while True:
        # Main Menu
        print("\nTodo List Menu:")
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            ViewAllTasks()

        elif choice == 2:
            AddTask()

        elif choice == 3:
            pass

        elif choice == 4:
            DeleteTask()

        elif choice == 5:
            pass

        elif choice == 6:
            break


def main():
    newEmptyJsonFile()
    generateTasks()
    MainMenu()


if __name__ == "__main__":
    main()
