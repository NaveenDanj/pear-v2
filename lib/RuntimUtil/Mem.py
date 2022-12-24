

mem = {}
local = {}
scope = {"func_name" : 'global' }

sample_data_types = {
    'int' : 0,
    'boolean' : True,
    'float' : 0.12,
    'string' : 'hello',
    'list' : list()
}

def var(var_name):
    if scope['func_name'] == 'global':
        return mem[var_name]['value']
    else:
        return local[var_name]['value']