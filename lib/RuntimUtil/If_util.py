from lib.RuntimUtil.Mem import var , mem

def handle_if_statement(statement):
    condition = statement.raw_statement.strip()
    condition = condition.split(' ' , 1)[1]
    condition_results = eval(condition)

    if condition_results == True:
        return statement.true_pointer
    elif statement.false_pointer == None:
        return statement.default_pointer
    else:
        return statement.false_pointer