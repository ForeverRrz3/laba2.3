import csv, os
from docxtpl import DocxTemplate, RichText


def get_filename():
    while True:
        filename = input("Введите имя файла: ").strip()
        if filename.endswith(".csv") and os.path.isfile(filename):
            return filename
        print("Файл не найден или не является .csv")


def read_csv_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file,
            fieldnames=["Year", "Name_winner", "Gender", "Country_winner", "Time", "Town"]
        )
        return list(reader)


def group_by_year(data: list[dict]):
    years = {}

    for row in data:
        year = row["Year"].strip()
        town = row["Town"].strip()
        gender = row["Gender"].strip()

        if year not in years:
            years[year] = {}
        if town not in years[year]:
            years[year][town] = {}

        if gender == "Male":
            years[year][town]["male"] = row
        elif gender == "Female":
            years[year][town]["female"] = row

    return dict(sorted(years.items()))


def build_context(years_data: dict):
    pages = []

    for year, towns in years_data.items():
        marathons = []
        for town, winners in towns.items():
            male   = winners.get("male",   {})
            female = winners.get("female", {})
            marathons.append(
                {
                "town": town,
                "male_name": male.get("Name_winner"),
                "male_country": male.get("Country_winner"),
                "male_time": male.get("Time"),
                "female_name": female.get("Name_winner"),
                "female_country": female.get("Country_winner"),
                "female_time": female.get("Time"),
                }
            )
        pages.append(
            {
                "year": year, 
                "marathons": marathons
            }
        )

    return pages

def generate_docx(pages: list, template_path: str, output_path: str):
    doc = DocxTemplate(template_path)
    doc.render({"pages": pages, "pb": RichText("\f")})
    doc.save(output_path)


filename = get_filename()
data = read_csv_file(filename)
years_data = group_by_year(data)
pages = build_context(years_data)
generate_docx(pages, "template.docx", "result.docx")


