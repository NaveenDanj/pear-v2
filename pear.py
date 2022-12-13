import sys
from lib.Lexer import generate_lex_tree
from lib.const.SysConst import Line


if sys.argv[1] == '--v':
    sys.exit("v1.0.0")

def readFile(filepath):

    if filepath.split(".")[-1] != 'pr' :
        return Exception("Invalid filename. Pear must in the pr file extension.")
    
    with open(filepath, "r") as file1:
        content_by_lines = file1.readlines()
        content_by_lines = [Line(line.replace("\n" , "") , index) for index , line in  enumerate(content_by_lines)]
        return content_by_lines

content_by_lines = readFile(sys.argv[1])
print(content_by_lines)
lex_tree = generate_lex_tree(content_by_lines)