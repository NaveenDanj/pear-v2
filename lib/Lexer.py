from lib.const.Keywords import KEYWORDS

class Statement:

    def __init__(self , raw_statement , splitted ):
        self.nextStatement = None
        self.raw_statement = raw_statement
        self.splitted = splitted
        self.identifier = None
        self.line_number = None


def handle_if_tree(statement_list , ln):
   
    stack = handle_if_stack(statement_list[ln:])

    identifier_list = [0]
    max_identifier = 0
    current_identifier = ''
    pointer_index = stack[-1][-1][0]

    for row in stack[-1]:
        
        st = row[1]
        
        if st.splitted[0] == 'if':

            if max_identifier == 0:
                st.identifier = str(identifier_list[-1] + 1)
                current_identifier = str(identifier_list[-1] + 1)
            else:
                st.identifier = current_identifier + '->' + str(identifier_list[-1] + 1)
                current_identifier = current_identifier + '->' + str(identifier_list[-1] + 1)


            max_identifier += 1

        elif st.splitted[0] == 'endif':
            if max_identifier == 0:
                st.identifier = max_identifier
                current_identifier = str(max_identifier)
            else:
                st.identifier = current_identifier
                current_identifier = current_identifier + '->' + str(max_identifier)

            max_identifier -= 1
            splitter = current_identifier.split("->")
            splitter = splitter[0:-2]
            id_str = "->".join(splitter)
            current_identifier = id_str
        else:
            st.identifier = current_identifier
        
        if max_identifier not in identifier_list: 
            identifier_list.append(max_identifier)

        print( st.raw_statement + " = " + str(st.identifier))

    return stack[-1]

def handle_if_stack(statement_list):
    stack = []
    out_stack = []
    last_if_index = []
    last_endif_index = []

    for count , st in enumerate(statement_list):
        stack.append([count , st])

        if st.splitted[0] == 'if' and count not in last_if_index:
            last_if_index.append(count)


        if st.splitted[0] == 'endif':
            if  count not in last_endif_index:
                last_endif_index.append(count)
            out_stack.append(stack[ last_if_index[-1] : last_endif_index[-1]+1 ])
            last_if_index.pop(len(last_if_index)-1)
            last_endif_index.pop(len(last_endif_index)-1)

        if len(last_if_index) == 0 and len(last_endif_index) == 0:
            return out_stack

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

