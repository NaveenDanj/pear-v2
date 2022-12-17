

def handle_function_call(statement , parse_tree):
    
    function_name = statement.raw_statement.split(' ' , 1)[1]
    function_name = function_name[:function_name.index('>')-1]
    function_start_pointer = None
    for index , st in enumerate(parse_tree):
        if st.splitted[0] == 'function':
            function_start_pointer = parse_tree[index+1 ]
            func_name = st.raw_statement.split(" ")[1]
            if func_name == function_name:
                st.default_pointer.next = statement.next
                statement.next = st.next

    if function_start_pointer == None:
        raise Exception('Function name '+ function_name +'undefined!')

    return function_start_pointer , parse_tree

def handle_function_init(statement):
    return statement.next