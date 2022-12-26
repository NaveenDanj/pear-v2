from lib.RuntimUtil.If_util import handle_if_statement
from lib.RuntimUtil.Mem import var
from lib.RuntimUtil.var_util import handle_var_statement , handle_set_var_statement
from lib.RuntimUtil.print_util import handle_print
from lib.RuntimUtil.while_util import handle_while
from lib.RuntimUtil.function_util import handle_function_call , handle_function_init , handle_endfunction , handle_return_statement

def run_pointer_statement(statement , parse_tree):
    if statement.splitted[0] == 'if':
        return handle_if_statement(statement)
    elif statement.splitted[0] == 'while':
        return handle_while(statement)
    elif statement.splitted[0] == 'var':
        return handle_var_statement(statement)  
    elif statement.splitted[0] == 'set':
        return handle_set_var_statement(statement)
    elif statement.splitted[0] == 'print':
        return handle_print(statement)
    elif statement.splitted[0] == 'call':
        next_ , parse_tree = handle_function_call(statement , parse_tree)
        return next_
    elif statement.splitted[0] == 'function':
        return handle_function_init(statement)
    elif statement.splitted[0] == 'endfunction':
        return handle_endfunction(statement , parse_tree)
    elif statement.splitted[0] == 'return':
        return handle_return_statement(statement , parse_tree)
    else:
        return statement.next


def interprete(parse_tree):
    next_pointer = run_pointer_statement(parse_tree[0] , parse_tree)
    # print(next_pointer.next.next.raw_statement)

    while next_pointer != None :
        next_next_pointer =  run_pointer_statement(next_pointer , parse_tree)
        # print(next_next_pointer.raw_statement , next_next_pointer.pointer)
        next_pointer = next_next_pointer

        # for item in parse_tree:
        #     if item.next != None:
        #         print(item.pointer , " -> " ,  item.raw_statement , item.next.pointer)

        # print('-----------------------------------')

