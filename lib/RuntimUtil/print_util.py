from lib.RuntimUtil.Mem import mem , var
from lib.util.lex_helper import remove_unwanted_whitespaces


def handle_print(statement):
    st = remove_unwanted_whitespaces( statement.raw_statement.strip() )
    st = st.split(' ' , 1)[1]
    exec('print(' + st + ')')
    return statement.next
