def handle_if_statement(statement):
    condition = statement.splitted[1]
    condition_results = eval(condition)

    if condition_results == True:
        return statement.true_pointer
    elif statement.false_pointer == None:
        return statement.default_pointer
    else:
        return statement.false_pointer