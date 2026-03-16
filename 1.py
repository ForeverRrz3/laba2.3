import json, os


def get_filename():
    while True:
        filename = input("Введите имя файла: ")
        if filename.endswith(".json") and os.path.isfile(filename): 
            return filename
        print("Введите существующий json файл")

def read_json_file(file_path: str):
    with open(file_path, 'r') as file:
        data = json.load(file)
        animals = data["animals"]
    return animals

def print_info_birds(animals: list):
    birds = list(filter(lambda x: x["animal_type"].lower() == "bird" ,animals))
    print("Данные о птицах:")
    print(birds)

def print_diurnal_animal(animals: list):
    diurnal_animals = list(filter(lambda x: x["active_time"].lower() == "diurnal" ,animals))
    print("Данные о дневных животных:")
    print(diurnal_animals)

def print_animal_weight_min(animals: list):
    min_weight_animal = min(animals, key=lambda x: x["weight_min"])
    print("Животное с наименьшим весом:")
    print(min_weight_animal)


animals = read_json_file(get_filename())
print(type(animals))
print_info_birds(animals)
print("-"*50)
print_diurnal_animal(animals)
print("-"*50)
print_animal_weight_min(animals)

