from lib.RuntimUtil.If_util import handle_if_statement
from lib.RuntimUtil.Mem import var
from lib.RuntimUtil.var_util import handle_var_statement , handle_set_var_statement
from lib.RuntimUtil.print_util import handle_print
from lib.RuntimUtil.while_util import handle_while


def run_pointer_statement(statement):
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
    else:
        return statement.next


def interprete(parse_tree):
    next_pointer = run_pointer_statement(parse_tree[0])
    # print(next_pointer.next.next.raw_statement)

    while next_pointer != None :
        next_next_pointer =  run_pointer_statement(next_pointer)
        next_pointer = next_next_pointer
