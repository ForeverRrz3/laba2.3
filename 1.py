import json, os


def get_filename():
    while True:
        filename = input("Введите имя файла: ").strip()
        if not filename.endswith(".json"):
            print("Файл должен иметь расширение .json")
            continue
        if not os.path.isfile(filename):
            print("Файл не найден")
            continue
        return filename


def read_json_file(file_path: str):
    while True:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data["animals"]
        except UnicodeDecodeError:
            print(f"Ошибка декодирования")
        except json.JSONDecodeError:
            print(f"Файл не является корректным json")
        except KeyError:
            print('В JSON отсутствует ключ "animals"')
        file_path = get_filename()


def print_info_birds(animals: list):
    birds = list(filter(lambda x: x["animal_type"].lower() == "bird", animals))
    print("Данные о птицах:")
    print(birds)


def print_diurnal_animal(animals: list):
    diurnal_animals = list(filter(lambda x: x["active_time"].lower() == "diurnal", animals))
    print("Данные о дневных животных:")
    print(diurnal_animals)


def print_animal_weight_min(animals: list):
    min_weight_animal = min(animals, key=lambda x: x["weight_min"])
    print("Животное с наименьшим весом:")
    print(min_weight_animal)


animals = read_json_file(get_filename())
print_info_birds(animals)
print("-" * 50)
print_diurnal_animal(animals)
print("-" * 50)
print_animal_weight_min(animals)
