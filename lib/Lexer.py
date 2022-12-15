from lib.const.Keywords import KEYWORDS
from lib.const.SysConst import Statement

def generate_lex_tree (content_by_lines) :

    statement_list = []
    lexer_tree = []
    counter = 0
    for statement in content_by_lines:

        statement.line = statement.raw_line.strip()
        splitted = statement.line.split(" ")

        if len(splitted) == 0:
            continue

        if splitted[0] == '~':
            continue

        if splitted[0] == '':
            continue

        if splitted[0] not in KEYWORDS:
            raise Exception("Invalid keyword")

        _statement = Statement(statement.raw_line , splitted)
        _statement.line_number = statement.line_number
        _statement.pointer = counter
        statement_list.append(_statement)
        counter += 1
        
    for item in statement_list:
        print( str(item.pointer) +  "-" + item.raw_statement)
