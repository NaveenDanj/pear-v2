def lex_if(lexer_index , statement_list):
    for index , item in enumerate(statement_list[lexer_index :]):        
        if item.splitted[0] == 'endif' and item.white_space_before == statement_list[lexer_index].white_space_before:
            item.nested_id = statement_list[lexer_index].nested_id


def lex_while(lexer_index , statement_list):
    # print(statement_list[lexer_index].raw_statement , "-" , statement_list[lexer_index].white_space_before)
    for index , item in enumerate(statement_list[lexer_index :]):        
        if item.splitted[0] == 'endwhile' and item.white_space_before == statement_list[lexer_index].white_space_before:
            item.nested_id = statement_list[lexer_index].nested_id