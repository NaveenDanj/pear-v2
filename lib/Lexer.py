from lib.const.Keywords import KEYWORDS
from lib.const.SysConst import Statement
from lib.util.lex_helper import lex_if , lex_while , lex_blockarize_if

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

        _statement.white_space_before = len(_statement.raw_statement) - len(_statement.raw_statement.lstrip())

        statement_list.append(_statement)
        counter += 1

    statement_list = build_syntax_tree(statement_list)
    statement_list = lexer(statement_list)
    statement_list = blokerize_lex_tree(statement_list)
    
def build_syntax_tree(statement_list):

    for index , item in enumerate(statement_list):
        if index ==  len(statement_list)-1:
            break
        item.next = statement_list[index + 1]

    return statement_list

def lexer(statement_list):
    lexer_index = 1

    while statement_list[lexer_index].raw_statement != '@end':
        st = statement_list[lexer_index]
        if st.splitted[0] == 'if':
            lex_if(lexer_index , statement_list)
        elif st.splitted[0] == 'while':
            lex_while(lexer_index , statement_list)
        lexer_index += 1

    # for item in statement_list:
    #     print(item.raw_statement , "-" , item.nested_id)

    return statement_list
    
def blokerize_lex_tree(statement_list):
    
    for index , st in enumerate(statement_list):
        if st.splitted[0] == 'if':
            lex_blockarize_if(index , statement_list)
    
    return statement_list