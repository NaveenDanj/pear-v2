from lib.RuntimUtil.Mem import var , mem , scope , local

def handle_function_call(statement , parse_tree):

    temp_pointer = None
    if statement.next != None:
        temp_pointer = statement.next.pointer

    function_name = statement.raw_statement.split(' ' , 1)[1]
    function_name = function_name[:function_name.index('>')-1]
    function_name = function_name.strip()
    function_start_pointer = None
    scope['func_name'] = function_name

    for index , st in enumerate(parse_tree):
        if st.splitted[0] == 'function':
            func_name = st.raw_statement.split(" ")[1]
            func_name = func_name.strip()
            if check_func_name_matching(func_name , function_name):
                function_start_pointer = parse_tree[index+1 ]
                st.default_pointer.next = statement.next
                statement.next = st.next
        elif st.splitted[0] == 'endfunction':
            if temp_pointer == None:
                st.next = None
            else:
                st.next = parse_tree[temp_pointer]

    if function_start_pointer == None:
        raise Exception('Function name '+ function_name +'undefined!')

    return function_start_pointer , parse_tree

def handle_function_init(statement):
    return statement.next


def handle_endfunction(statement , parse_tree):
    
    function_start_pointer = None
    function_end_pointer = statement.pointer
    func_name = None

    for i in range(len(parse_tree)-1 , -1 , -1):
        st = parse_tree[i]
        if st.splitted[0] == 'function':
            function_start_pointer = st.pointer
            func_name = st.raw_statement.split(" ")[1]
            func_name = func_name.strip()
            break

    for item in parse_tree[function_start_pointer : function_end_pointer + 1]:

        if item.splitted[0] == 'var':
            var_name = item.splitted[2]
            if var_name in local:
                if local[var_name]['scope'] == func_name:
                    del local[var_name]
    
    scope['func_name'] = 'global'
    return statement.next

def check_func_name_matching(n1 , n2):

    if len(n1) != len(n2):
        return False
    
    for i in range(len(n1)-1):
        if n1[i] != n2[i]:
            return False

    return True