from pathlib import Path
def total_salary(path):
    try:
        total=0
        lines=0
        with open(path, mode="r", encoding="utf-8") as file:
            for line in file:
                if not line:
                    return 0, 0
                lines+=1
                _,salary= line.strip().split(",")
                total += float(salary)
            average=total/lines
            return total,average
            
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0

    except (ValueError, IndexError):
        print("Помилка: файл пошкоджений або має неправильний формат.")
        return 0, 0
path = Path("D:/GoIT_dz/PythonCore/goit-algo-hw-04/Task_1/task_1.txt")
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")