from lib.RuntimUtil.Mem import var

def handle_var_statement(statement):
    
    val = eval(statement.raw_statement.split("=")[1])
    var_name = statement.raw_statement.split(' ')[2]
    var_data_type = statement.raw_statement.split(' ')[1]

    sample_data_types = {
        'int' : 0,
        'boolean' : True,
        'float' : 0.12,
        'string' : 'hello'
    }

    if type(val) != type(sample_data_types[var_data_type]):
        raise Exception('Invalid data type')

    if var_name in var:
        raise Exception('Variable name ' , var_name , 'already been initialized')

    var[var_name] = {
        "datatype" : var_data_type,
        "value" : val,
        "name" : var_name
    }