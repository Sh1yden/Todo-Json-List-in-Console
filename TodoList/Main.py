# Импорт нужных библиотек.
import json
from random import randint
import os
from pathlib import Path
from uuid import uuid4

# Константы
SAVE_DIR = Path("save/tasks")
SAVE_FILE = SAVE_DIR / "save.json"
DEFAULT_FILE = {"all_tasks": {}}
DEFAULT_TASK = {
    "task_name": "",
    "task_description": "",
    "task_status": "",
    "task_create_date": "",
    "task_priority": "",
    "task_deadline": "",
}


class TaskManager:
    """Класс приложения TODO LIST IN TERMINAL."""

    # Конструктор класса.
    def __init__(self):
        # Это словарь для хранения всех задач.
        self.tasks = {"all_tasks": {}}
        self._initialize_files()

    def _initialize_files(self):
        """Инициализация файлов и директорий, если они не существуют."""
        try:
            # Создаём директорию
            SAVE_DIR.mkdir(parents=True, exist_ok=True)
            # Если файла нет, создаём новый
            if not SAVE_FILE.exists():
                self._save_to_file()
        except Exception as e:
            print(f"File initialization error: {e}")

    def _load_from_file(self):
        """Загрузка данных из файла."""
        try:
            with open(SAVE_FILE, "r") as f:
                self.tasks = json.load(f)
        except Exception as e:
            print(f"Error loading data from a file: {e}")

    def _save_to_file(self):
        """Сохранение данных в файл."""
        try:
            with open(SAVE_FILE, "w") as f:
                # ensure_ascii=False для корректной записи русских символов.
                json.dump(self.tasks, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error when saving data to a file: {e}")

    def view_all_tasks(self):
        """Просмотр всех задач."""
        try:
            self._load_from_file()
            if not self.tasks["all_tasks"]:
                print("Tasks list is empty.")
                return

            print("\nCount of tasks: ", len(self.tasks["all_tasks"]))
            for task_id, task_data in self.tasks["all_tasks"].items():
                print(f"\nTask ID: {task_id}")
                for key, value in task_data.items():
                    print(f"{key.replace("task_", "").capitalize()}: {value}")
        except Exception as e:
            print(f"Error when viewing data from a file: {e}")

    def add_task(self):
        """Добавление новой задачи."""
        try:
            self._load_from_file()
            task_id = str(uuid4())

            print("\nAdding new task:")
            # Временный словарь для хранения новых данных.
            new_task = {}
            for field in DEFAULT_TASK:
                new_task[field] = input(f"Enter {field.replace("task_", "")}: ")

            self.tasks["all_tasks"][f"task_id: {task_id}"] = new_task
            self._save_to_file()
            print("Task added successfully.")

        except Exception as e:
            print(f"Error adding a task: {e}")

    def update_task(self):
        """Обновление существующей задачи."""
        try:
            self._load_from_file()
            self.view_all_tasks()
            print("\nUpdating a task:")
            task_id = input("Enter the ID of the task you want to update: ")
            if task_id not in self.tasks["all_tasks"]:
                print("Task id not found.")
                return

            print("\nCurrent task data:")
            for key, value in self.tasks["all_tasks"][task_id].items():
                print(f"{key.replace('task_', '').capitalize()}: {value}")

            print("\nEnter the new data for the task:")
            for field in DEFAULT_TASK:
                new_value = input(
                    f"Enter new {field.replace('task_', '').capitalize()}: "
                )
                if new_value:
                    self.tasks["all_tasks"][task_id][field] = new_value

            self._save_to_file()
            print("\nTask updated successfully.")
        except Exception as e:
            print(f"Error updating a task: {e}")

    def delete_task(self):
        """Удаление существующей задачи."""
        try:
            pass
        except Exception as e:
            print(f"Error deleting a task: {e}")

    def search_task(self):
        """Поиск задачи по id."""
        try:
            pass
        except Exception as e:
            print(f"Error searching a task: {e}")

    def generate_test_tasks(self, count: int = 10):
        """Генерация тестовых задач (для отладки)."""
        try:
            # Генерация тестовых задач с использованием DEFAULT_TASK.
            for i in range(count):
                task_id = str(uuid4())
                # Прикольное использование ** для распаковки словаря DEFAULT_TASK.
                self.tasks["all_tasks"][f"task_id: {task_id}"] = {
                    **DEFAULT_TASK,
                    "task_name": f"Test task {randint(1, 10000)}",
                    "task_status": "test",
                }
            self._save_to_file()
            print(f"Generated {count} test tasks.")
        except Exception as e:
            print(f"Error when generating test tasks: {e}")

    def clear_all_tasks(self):
        """Удаление всех задач."""
        try:
            confirm = input("You are sure? This delete ALL tasks! (y/N): ")
            if confirm.lower() == "y":
                self.tasks["all_tasks"] = {}
                self._save_to_file()
                print("All tasks have been successfully deleted.")
            else:
                print("Task deletion canceled.")
        except Exception as e:
            print(f"Error deleting all tasks: {e}")


def main_menu():
    manager = TaskManager()

    while True:
        print("\n" + "=" * 20)
        print("TODO LIST IN TERMINAL")
        print("=" * 20)
        print("Todo List Menu:")
        print("1. View All Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Generate Test Tasks")
        print("7. Clear All Tasks")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.view_all_tasks()
        elif choice == "2":
            manager.add_task()
        elif choice == "3":
            manager.update_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            manager.search_task()
        elif choice == "6":
            count = input("\nHow many tasks should I generate? (default 10): ")
            manager.generate_test_tasks(int(count) if count.isdigit() else 10)
        elif choice == "7":
            manager.clear_all_tasks()
        elif choice == "8":
            print("\nExiting the program...")
            break
        else:
            print("\nWrong choice. Try again.")
            return


if __name__ == "__main__":
    main_menu()
