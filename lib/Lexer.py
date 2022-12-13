from lib.const.Keywords import KEYWORDS
from lib.const.SysConst import Statement
from lib.util.ConditionalStatementLexer import handle_if_tree , handle_if_stack


def generate_lex_tree (content_by_lines) :

    statement_list = []
    
    for statement in content_by_lines:
        statement.line = statement.raw_line.strip()

        splitted = statement.line.split(" ")
        _statement = Statement(statement.raw_line , splitted)
        _statement.line_number = statement.line_number
        statement_list.append(_statement)

        
    
    for statement in statement_list:

        splitted = statement.raw_statement.split(" ")

        if len(splitted) == 0:
            continue

        if splitted[0] == '~':
            continue

        if splitted[0] == '':
            continue

        if splitted[0] not in KEYWORDS:
            raise Exception("Invalid keyword")

        if splitted[0] == 'if':
            handle_if_tree(statement_list , statement.line_number)

