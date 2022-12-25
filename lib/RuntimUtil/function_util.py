from lib.RuntimUtil.Mem import var , mem , scope , local , param

def handle_function_call(statement , parse_tree):
    temp_pointer = None
    if parse_tree[statement.pointer+1] != None:
        temp_pointer = statement.pointer+1

    function_name = statement.raw_statement.split(' ' , 1)[1]
    function_name = function_name[:function_name.index('>')-1]
    function_name = function_name.strip()
    function_start_pointer = None
    scope['func_name'] = function_name

    params = statement.raw_statement[statement.raw_statement.index( '(' )+1 : -2]
    param_list = params.split(',')

    for index , item in enumerate(param_list):
        param_list[index] = param_list[index].strip()
        if param_list[index] == '':
            del param_list[index]

    st = get_function_statement_by_function_name(function_name , parse_tree)[0]

    if st.parameters != None:

        if len(param_list) != len(st.parameters.items() ):
            raise Exception('Insuffient paramerts provided for the function ' + function_name)
        else:
            counter = 0
            for item  in st.parameters.items():
                obj = item[1]
                obj['func_name'] = function_name
                obj['value'] = eval( param_list[counter] )
                param[ obj['var_name'] ] = obj
                counter += 1
    else:

        if len(param_list) > 0:
            raise Exception('Extra parameters provided for the function ' + function_name)


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
                # st.next = None
                parse_tree[index].next = None
            else:
                pass
                # st.next = parse_tree[temp_pointer]
                # parse_tree[index].next = parse_tree[temp_pointer]

    if function_start_pointer == None:
        raise Exception('Function name '+ function_name +'undefined!')
    
    parse_tree[statement.pointer].next = parse_tree[statement.pointer+1]
    # print('next : ' , parse_tree[statement.pointer].next.raw_statement)
    
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

    # print('end function for : ' , func_name)
    
    for item in parse_tree[function_start_pointer : function_end_pointer + 1]:

        if item.splitted[0] == 'var':
            var_name = item.splitted[2]
            if var_name in local:
                if local[var_name]['scope'] == func_name:
                    del local[var_name]
    
    for item in param:
        if param[item]['func_name'] == func_name:
            del param[item]

    scope['func_name'] = 'global'
    return statement.next

def check_func_name_matching(n1 , n2):

    if len(n1) != len(n2):
        return False
    
    for i in range(len(n1)-1):
        if n1[i] != n2[i]:
            return False

    return True


def get_function_statement_by_function_name(function_name , parse_tree):

    for index , item in enumerate(parse_tree):
        
        if item.splitted[0] == 'function':
            func_name = item.raw_statement.split(" ")[1]
            func_name = func_name.strip()

            if func_name == function_name:
                return item , index

    return None




