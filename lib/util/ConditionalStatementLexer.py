
# def handle_if_stack(statement_list):
#     stack = []
#     out_stack = []
#     last_if_index = []
#     last_endif_index = []

#     for count , st in enumerate(statement_list):

#         stack.append([count , st])

#         if st.splitted[0] == 'if' and count not in last_if_index:
#             last_if_index.append(count)


#         if st.splitted[0] == 'endif':
#             if  count not in last_endif_index:
#                 last_endif_index.append(count)
#             print('range : ' , last_if_index , last_endif_index)
#             out_stack.append(stack[ last_if_index[-1] : last_endif_index[-1]+1  ])
#             # print(stack[ last_if_index[-1] : last_endif_index[-1]+1  ])
#             for item in stack[ last_if_index[-1] : last_endif_index[-1]+1  ]:
#                 print(item[1].raw_statement)
#             last_if_index.pop(len(last_if_index)-1)
#             last_endif_index.pop(len(last_endif_index)-1)
#             # print('-----------------------------------------------')

#         if len(last_if_index) == 0 and len(last_endif_index) == 0:
#             return out_stack

    # print(last_if_index , last_endif_index)
    
    # for i in range(len(last_if_index)-1 ,-1 , -1):
    #     print(last_if_index[i]+1 , last_endif_index[i]+1)
    #     # if i == 1:
    #     #     get_elems_in_range(last_if_index[i] , last_endif_index[i] , statement_list)
    #     # print(last_if_index[i] , last_endif_index[i])

    # print(last_if_index , last_endif_index)
    # return out_stack

# def get_elems_in_range(n1 , n2 , list_):
#     for item in list_[n1-1 : n2+1]:
#         print(item.raw_statement)

# def handle_if_tree(statement_list , ln):
   
#     stack = handle_if_stack(statement_list[ln:])
#     identifier_list = [0]
#     max_identifier = 0
#     current_identifier = ''
#     pointer_index = ln

#     if stack != None:
#         if len(stack) > 0:
#             for row in stack[len(stack)-1]:
            
#                 st = row[1]
                
#                 if st.splitted[0] == 'if':

#                     if max_identifier == 0:
#                         st.identifier = str(identifier_list[-1] + 1)
#                         current_identifier = str(identifier_list[-1] + 1)
#                     else:
#                         st.identifier = current_identifier + '->' + str(identifier_list[-1] + 1)
#                         current_identifier = current_identifier + '->' + str(identifier_list[-1] + 1)

#                     max_identifier += 1

#                 elif st.splitted[0] == 'endif':
#                     if max_identifier == 0:
#                         st.identifier = max_identifier
#                         current_identifier = str(max_identifier)
#                     else:
#                         st.identifier = current_identifier
#                         current_identifier = current_identifier + '->' + str(max_identifier)

#                     max_identifier -= 1
#                     splitter = current_identifier.split("->")
#                     splitter = splitter[0:-2]
#                     id_str = "->".join(splitter)
#                     current_identifier = id_str
#                 else:   
#                     st.identifier = current_identifier
                
#                 if max_identifier not in identifier_list: 
#                     identifier_list.append(max_identifier)

#     # for row in stack:
#     #     print(row)
#     #     for item in row:
#     #         print(item[1].raw_statement)

#     return stack