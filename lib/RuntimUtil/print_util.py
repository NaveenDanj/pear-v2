from lib.RuntimUtil.Mem import mem , var


def handle_print(statement):
    st = statement.raw_statement.strip()
    st = st.split(' ' , 1)[1]
    prin_val = eval(st)
    print(st)
    return statement.next
