from lib.const.Keywords import KEYWORDS
from lib.const.SysConst import Statement
from lib.util.lex_helper import lex_blockarize_function , lex_if , lex_while , lex_blockarize_if , lex_blockarize_while , lex_function
import re

def generate_lex_tree (content_by_lines) :

    statement_list = []
    lexer_tree = []
    counter = 0
    for statement in content_by_lines:

        statement.line = statement.raw_line.strip()
        statement.line = re.sub(" +", " ", statement.line)
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
    statement_list = link_blocks(statement_list)

    # print('-------------------')

    # for item in statement_list:
    #     if item.next != None:
    #         print(item.pointer , " -> " ,  item.raw_statement , item.next.pointer)
    
    return statement_list

    
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
        elif st.splitted[0] == 'function':
            lex_function(lexer_index , statement_list)
        else:
            lex_expression(lexer_index , statement_list)
        lexer_index += 1

    return statement_list
    
def blokerize_lex_tree(statement_list):
    
    for index , st in enumerate(statement_list):
        if st.splitted[0] == 'if':
            true_part , false_part , endif_index = lex_blockarize_if(index , statement_list)
            st.true_pointer = true_part[0].pointer
            st.default_pointer = endif_index
            statement_list[ true_part[ len(true_part)-1 ].pointer ].next =  statement_list[endif_index]

            if len(false_part) > 0:
                st.false_pointer = false_part[0].pointer

        elif st.splitted[0] == 'while':
            endwhile_index , while_index = lex_blockarize_while(index , statement_list)
            st.default_pointer = endwhile_index+1
            statement_list[endwhile_index].next = statement_list[while_index]

        elif st.splitted[0] == 'function':
            endfunction_index , index = lex_blockarize_function(index , statement_list)
            st.default_pointer = endfunction_index
            st.next = statement_list[endfunction_index]
            statement_list[endfunction_index].next = statement_list[endfunction_index+1]

            st = statement_list[index]
            func_name = st.raw_statement.split(" ")[1]
            func_name = func_name.strip()
            param_list = st.raw_statement[st.raw_statement.index( '(' )+1 : st.raw_statement.index( ')' )].strip()
            param_list = param_list.split(',')
            param_list_out = {}


            for index , param in enumerate(param_list):
                param_list[index] =  param_list[index].strip()
                data_type = param_list[index].split(' ')[0]
                var_name = param_list[index].split(' ')[-1]
                if var_name != '':

                    param_list_out[var_name] = {
                        "var_name" : var_name,
                        "value" : None,
                        "datatype" : data_type,
                        "func_name" : func_name
                    }

            st.parameters = param_list_out

    return statement_list



def lex_expression(lexer_index , statement_list):
    if lexer_index+1 ==  len(statement_list)-1:
        statement_list[lexer_index].next = None
    else:
        statement_list[lexer_index].next = statement_list[lexer_index+1]

    if lexer_index > 0:
        statement_list[lexer_index].prev_pointer = statement_list[lexer_index-1]

    return statement_list

def link_blocks(statement_list):
    for index , st in enumerate(statement_list):
        
        if st.splitted[0] == 'if':
            st.default_pointer = statement_list[st.default_pointer]
            st.true_pointer = statement_list[st.true_pointer]

            if st.false_pointer != None:
                st.false_pointer = statement_list[st.false_pointer]

        elif st.splitted[0] == 'while':
            st.default_pointer = statement_list[st.default_pointer]

        elif st.splitted[0] == 'function':
            st.default_pointer = statement_list[st.default_pointer]

        elif st.default_pointer != None:
            st.default_pointer = statement_list[st.default_pointer]
    
    return statement_list