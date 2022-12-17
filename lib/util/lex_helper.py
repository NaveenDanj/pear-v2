import re

def lex_if(lexer_index , statement_list):
    for index , item in enumerate(statement_list[lexer_index :]):        
        if item.splitted[0] == 'endif' and item.white_space_before == statement_list[lexer_index].white_space_before:
            item.nested_id = statement_list[lexer_index].nested_id
        elif item.splitted[0] == 'else' and item.white_space_before == statement_list[lexer_index].white_space_before:
            item.nested_id = statement_list[lexer_index].nested_id

def lex_while(lexer_index , statement_list):
    for index , item in enumerate(statement_list[lexer_index :]):        
        if item.splitted[0] == 'endwhile' and item.white_space_before == statement_list[lexer_index].white_space_before:
            item.nested_id = statement_list[lexer_index].nested_id


def lex_blockarize_if(index , statement_list):
    root_item = statement_list[index]
    have_else = False
    true_part = []
    false_part = []
    endif_index = 0
    
    for item_index , item in enumerate(statement_list):
        if root_item.nested_id == item.nested_id:
            if item.splitted[0] == 'else':
                have_else = True
            
            if item.splitted[0] == 'endif':
                endif_index = item_index
    
    if have_else:            
        for item_index , item in enumerate(statement_list):
            if root_item.nested_id == item.nested_id:
                if item.splitted[0] == 'else':
                    true_part = statement_list[index+1 : item_index]
                    false_part = statement_list[item_index+1 : endif_index]
    else:

        for item_index , item in enumerate(statement_list):
            if root_item.nested_id == item.nested_id:
                if item.splitted[0] == 'endif':
                    true_part = statement_list[index+1 : item_index]

    return true_part , false_part , endif_index


def lex_blockarize_while(index , statement_list):
    root_item = statement_list[index]
    endwhile_index = 0
    
    for item_index , item in enumerate(statement_list):
        if root_item.nested_id == item.nested_id:
            if item.splitted[0] == 'endwhile':
                endwhile_index = item_index
    
    return endwhile_index , index



def remove_unwanted_whitespaces(string):
    out = re.sub(" +", " ", string)
    return out