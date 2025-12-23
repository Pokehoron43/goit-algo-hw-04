from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line:
                    return []
                id_, name, age = line.strip().split(",")
                cats_info.append({
                    "id": id_,
                    "name": name,
                    "age": age
                })
                
                                

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []

    except (ValueError, IndexError):
        print("Помилка: файл пошкоджений або має неправильний формат.")
        return []

    return cats_info


path = Path("D:/GoIT_dz/PythonCore/goit-algo-hw-04/Task_2/task_2.txt")

for cat in get_cats_info(path):
    print(cat)
