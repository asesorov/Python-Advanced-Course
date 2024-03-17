def generate_latex_table(data, is_embedded=False):
    latex_begin = ''
    latex_end = '\end{tabular}'
    if not is_embedded:
        latex_begin = '\\documentclass{article}\n\\begin{document}'
        latex_end += '\end{document}'
    latex_code = latex_begin + '\\begin{tabular}{|' + 'c|' * len(data[0]) + '}\n\\hline\n'

    for row in data:
        latex_code += ' & '.join(str(cell) for cell in row)
        latex_code += ' \\\\\n'
        latex_code += '\\hline\n'

    latex_code += latex_end
    
    return latex_code
