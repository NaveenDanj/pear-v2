
def generate_lex_tree (content_by_lines) :
    
    for statement in content_by_lines:
        statement.line = statement.raw_line.strip()
        print(statement.line)
