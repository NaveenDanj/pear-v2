from lib.RuntimUtil.Mem import var , sample_data_types , mem
from lib.util.lex_helper import remove_unwanted_whitespaces
import uuid


def handle_var_statement(statement):
    st = remove_unwanted_whitespaces( statement.raw_statement.strip() )
    val = eval(st.split("=")[1])
    var_name = st.split(' ')[2]
    var_data_type = st.split(' ')[1]

    if type(val) != type(sample_data_types[var_data_type]):
        raise Exception('Invalid data type')

    if var_name in var:
        raise Exception('Variable name ' , var_name , ' already been initialized')

    mem[var_name] = {
        "datatype" : var_data_type,
        "value" : val,
        "name" : var_name,
        "id" : len(mem)-1
    }

    var[var_name] = val

    return statement.next


def handle_set_var_statement(statement):
    st = remove_unwanted_whitespaces( statement.raw_statement.strip() )
    val = eval(st.split("=")[1])
    var_name = st.split(' ')[1]
    var_name = get_substring(var_name , "var['" , "']")

    if var_name not in mem:
        raise Exception('Variable name ' , var_name , ' undefined')

    var_instance = mem[var_name]
    
    if type(val) != type(sample_data_types[ var_instance['datatype'] ]):
        raise Exception('Invalid data type')

    mem[var_name]['value'] = val
    var[var_name] = val

    return statement.next



def get_substring(original_string , sub1 , sub2):
    
    idx1 = original_string.index(sub1)
    idx2 = original_string.index(sub2)

    res = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1) , idx2):
        res = res + original_string[idx]

    return res


def get_object_id(var_name):
    pass