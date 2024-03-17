from pathlib import Path

from latex_generator import generate_latex_table


ARTIFACTS_PATH = Path(__file__).resolve().parent / 'artifacts'


def main():
    data = [
        ["Name", "Mark", "Group", "Comment"],
        ["Alex", 10, "M4151", "10/10 omg 10/10"],
        ["John", 6, "P8934", "Not original"],
        ["Eustegnia", 9, "PI4321", "Beautiful name!"]
    ]

    latex_code = generate_latex_table(data)

    with open(ARTIFACTS_PATH / "table.tex", "w") as file:
        file.write(latex_code)

    print(f"LaTeX код таблицы сохранен в файле {ARTIFACTS_PATH / 'table.tex'}.")

if __name__ == '__main__':
    main()
