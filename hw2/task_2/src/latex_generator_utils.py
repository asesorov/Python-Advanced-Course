def generate_page(*funcs_and_params):
    latex_begin = '\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n'
    latex_end = '\\end{document}'

    content = ''
    for func_and_params in funcs_and_params:
        if callable(func_and_params):
            # function without params
            content += func_and_params() + '\n'
        else:
            # tuple (function, params)
            func, params = func_and_params[0], func_and_params[1:]
            content += func(*params) + '\n'

    return latex_begin + content + latex_end


def generate_latex_table(data):
    latex_end = '\\end{tabular}'
    latex_code = '\\begin{tabular}{|' + 'c|' * len(data[0]) + '}\n\\hline\n'

    for row in data:
        latex_code += ' & '.join(str(cell) for cell in row)
        latex_code += ' \\\\\n'
        latex_code += '\\hline\n'

    latex_code += latex_end
    
    return latex_code


def generate_latex_image(image_path):
    image_code = '\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{' + image_path + '}\n\\end{figure}\n'
    return image_code
