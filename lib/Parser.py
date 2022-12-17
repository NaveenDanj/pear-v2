from lib.util.lex_helper import remove_unwanted_whitespaces


def generate_parse_tree(lex_tree):
    
    for statement in lex_tree:
        statement.raw_statement = remove_unwanted_whitespaces( statement.raw_statement.strip() )

    return lex_tree