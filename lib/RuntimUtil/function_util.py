from lib.RuntimUtil.Mem import var , mem , scope , local , param , ret

def handle_function_call(statement , parse_tree):
    temp_pointer = None
    if parse_tree[statement.pointer+1] != None:
        temp_pointer = statement.pointer+1

    function_name = statement.raw_statement.split(' ' , 1)[1]
    function_name = function_name[:function_name.index('>')-1]
    function_name = function_name.strip()
    function_start_pointer = None
    
    function_start_pointer , function_end_pointer = get_function_start_end_pointers(function_name , parse_tree)
    function_start_pointer = parse_tree[function_start_pointer]
    function_end_pointer = parse_tree[function_end_pointer]
    
    for item in parse_tree[function_start_pointer.pointer : function_end_pointer.pointer]:
        if item.splitted[0] == 'var':
            var_name = item.splitted[2]
            if var_name in local:
                if local[var_name]['scope'] == function_name:
                    del local[var_name]

    params = statement.raw_statement[statement.raw_statement.index( '(' )+1 : -1]
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
                # obj['value'] = eval( param_list[counter] )
                if 'get' in param_list[counter]:
                    val = param_list[counter]
                    function_name_ = val.split(' ' , 1)[1]
                    function_name_ = function_name_[:function_name_.index('>')-1]
                    function_name_ = function_name_.strip()
                    if function_name_ not in ret:
                        raise Exception('Function name ' + function_name_ + ' undefined!')
                    else:
                        obj['value'] = ret[function_name_]['value']
                else:
                    obj['value'] = eval( param_list[counter] )
                     
                
                param[ obj['var_name'] ] = obj
                counter += 1
    else:

        if len(param_list) > 0:
            raise Exception('Extra parameters provided for the function ' + function_name)

    # scope['func_name'] = function_name
    scope['scope_stack'].append(function_name)
    scope['func_name'] = scope['scope_stack'][-1]

    function_end_pointer = None

    for index , st in enumerate(parse_tree):

        if st.splitted[0] == 'function':
            func_name = st.raw_statement.split(" ")[1]
            func_name = func_name.strip()
            if check_func_name_matching(func_name , function_name):
                function_start_pointer = parse_tree[index+1 ]
                st.default_pointer.next = statement.next
                statement.next = st.next
        elif st.splitted[0] == 'endfunction':
            function_end_pointer = index
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

    for item , index in param.copy().items():
        if param[item]['func_name'] == func_name:
            del param[item]

    # delete the return value from the memory
    # if func_name in ret:
    #     del ret[func_name]
        
    if scope['scope_stack'][-1] != 'global':
        scope['scope_stack'].pop()
    scope['func_name'] = scope['scope_stack'][-1]
    
    return statement.next


def handle_return_statement(statement , parse_tree):
    
    function_end_pointer = None
    func_name = None

    upper_list = parse_tree[ : statement.pointer]
    upper_list.reverse()
    
    for i in range(len(upper_list)):
        st = upper_list[i]
        if st.splitted[0] == 'function':
            func_name = st.raw_statement.split(" ")[1]
            func_name = func_name.strip()
            break
    
    down_list = parse_tree[statement.pointer:]
    
    for item in down_list:
        if item.splitted[0] == 'endfunction':
            function_end_pointer = item.pointer
            break


    ret_val = statement.raw_statement.split(' ' , 1)[1]
    ret_val = eval(ret_val)

    ret[func_name] = {
        "func_name" : func_name,
        "value" : ret_val,
        'scope' : func_name
    }
        
    return parse_tree[function_end_pointer]
    

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




def get_function_start_end_pointers(function_name , parse_tree):
    
    function_start_pointer = None
    function_end_pointer = None
    
    for index , st in enumerate(parse_tree):
    
        if st.splitted[0] == 'function':
            func_name = st.raw_statement.split(" ")[1]
            func_name = func_name.strip()
            if check_func_name_matching(func_name , function_name) and function_start_pointer == None :
                function_start_pointer = index
                
        elif st.splitted[0] == 'endfunction' and function_end_pointer == None and function_start_pointer != None:
            function_end_pointer = index
            break
        
    return function_start_pointer , function_end_pointer