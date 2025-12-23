import sys
from pathlib import Path
from colorama import Fore, init
init(autoreset=True)

def visualize_directory(path: Path, indent: str = ""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE} {item.name}")
            visualize_directory(item, indent + " ┃ ")
        else:
            print(f"{indent}{Fore.GREEN} {item.name}")


def main():
    if len(sys.argv) != 2:
        print("Використання: python task_3.py <шлях_до_директорії>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print("Помилка: шлях не існує")
        sys.exit(1)

    if not dir_path.is_dir():
        print("Помилка: шлях не є директорією")
        sys.exit(1)

    print(f"{Fore.YELLOW} {dir_path.name}")
    visualize_directory(dir_path)


if __name__ == "__main__":
    main()
