import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from create_file import create_file

salaries_data = ["Alex Korp,3000",
                  "Nikita Borisenko,2000",
                  "Sitarama Raju,1000"]


#create_file("task_1/salaries.txt", salaries_data)

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    salary = int(line.strip().split(",")[1])
                    total += salary
                    count += 1
        average_salary = total / count
        return total, average_salary
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0 
    except ValueError:
        print(f"Некоректний формат даних у файлі {path}.")
        return 0, 0
    except ZeroDivisionError:
        print(f"Файл {path} порожній.")
        return 0, 0

total, average = total_salary("task_1/salaries.txt")
print(f"Загальна заробітна плата: {total}\n"
      f"Середня заробітна плата: {average}"
     )