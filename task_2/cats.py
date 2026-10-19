import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from create_file import create_file

cats_data =["60b90c1c13067a15887e1ae1,Tayson,3"
,"60b90c2413067a15887e1ae2,Vika,1"
,"60b90c2e13067a15887e1ae3,Barsik,2"
,"60b90c3b13067a15887e1ae4,Simon,12"
,"60b90c4613067a15887e1ae5,Tessi,5"
]

#create_file("task_2/cats.txt", cats_data)

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    id, name, age = line.strip().split(",")
                    cats_info.append({"id": id, "name": name, "age": int(age)})
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except ValueError:
        print(f"Некоректний формат даних у файлі {path}.")
    return cats_info

print(get_cats_info("task_2/cats.txt"))
