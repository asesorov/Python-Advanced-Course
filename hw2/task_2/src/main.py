import argparse

from src.latex_generator_utils import generate_page, generate_latex_table, generate_latex_image


def main():
    parser = argparse.ArgumentParser(description='Generate LaTeX table from input data.')
    parser.add_argument('--data', nargs='+', help='Input data for the table (row by row)')
    parser.add_argument('--image', help='Image path')
    parser.add_argument('--output', help='Output dir', default='artifacts')
    args = parser.parse_args()

    if args.data:
        data = [row.split(',') for row in args.data]
    else:
        data = [
            ["Name", "Mark", "Group", "Comment"],
            ["Alex", 10, "M4151", "10/10 omg 10/10"],
            ["John", 6, "P8934", "Not original"],
            ["Eustegnia", 9, "PI4321", "Beautiful name!"]
        ]

    latex_code = generate_page((generate_latex_table, data), (generate_latex_image, args.image))

    with open(f"{args.output}/table.tex", "w") as file:
        file.write(latex_code)

    print(f"LaTeX table code saved to {args.output}/table.tex")


if __name__ == '__main__':
    main()
