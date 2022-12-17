from lib.RuntimUtil.Mem import var , sample_data_types , mem


def handle_while(statement):
    st = statement.raw_statement.strip()
    condition = st.split(' ' , 1)

    condition_true = eval(condition[1])

    if condition_true:
        return statement.next
    else:
        return statement.default_pointer