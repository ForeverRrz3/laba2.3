import csv, os


def get_filename():
    while True:
        filename = input("Введите имя файла: ")
        if filename.endswith(".csv") and os.path.isfile(filename): 
            return filename
        print("Введите существующий csv файл")

def read_csv_file(file_path: str):
    with open(file_path, 'r') as file:
        data = csv.DictReader(file)
        countries = list(data)
    return countries

def get_range_income():
    while True:
        income_range = input("Введите диапазон доходов в формате min-max: ").split("-")
        if len(income_range) == 2:
            try:
                low = float(income_range[0])
                high = float(income_range[1])
                if low < high:
                    return low, high    
            except ValueError:
                print("Введите числа")
        print("Неверный формат")
    

def get_countries_income_range(countries: list, income_range: tuple):
    countries_income = list(filter(lambda x: int(income_range[0]) <= float(x["Income"]) <= float(income_range[1]), countries))
    write_csv_file(countries_income, "countries_income_res.csv")
    

def sort_countries_inflation(countries: list):
    sorted_countries = sorted(countries, key=lambda x: x["Inflation"])
    write_csv_file(sorted_countries, "countries_inflatiuon_res.csv")

def write_csv_file(data: list[dict], filename: str):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)



countries = read_csv_file(get_filename())
income_range = get_range_income()
get_countries_income_range(countries, income_range)
sort_countries_inflation(countries)