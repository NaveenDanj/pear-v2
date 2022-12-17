import sys
from lib.Lexer import generate_lex_tree
from lib.Parser import generate_parse_tree
from lib.const.SysConst import Line
from lib.Runtime import interprete
from lib.RuntimUtil.Mem import var

if sys.argv[1] == '--v':
    sys.exit("v1.0.0")

def readFile(filepath):

    if filepath.split(".")[-1] != 'pr' :
        return Exception("Invalid filename. Pear must in the .pr file extension.")
    
    with open(filepath, "r") as file1:
        content_by_lines = file1.readlines()
        content_by_lines = [Line(line.replace("\n" , "") , index) for index , line in  enumerate(content_by_lines)]
        return content_by_lines

content_by_lines = readFile(sys.argv[1])
lex_tree = generate_lex_tree(content_by_lines)
parse_tree = generate_parse_tree(lex_tree)
interprete(parse_tree)


print('----------------------------------------')
print(var)