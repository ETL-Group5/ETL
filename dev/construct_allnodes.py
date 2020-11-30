def allnodes_of_a_node(a,b):
    if ((a is None) and (b is not None)):
        all_nodes = b
    elif ((b is None) and (a is not None)):
        all_nodes = a
    elif ((b is None) and (a is None)):
        all_nodes = None
    else:
        all_nodes = a + b
    return all_nodes


def set_all_nodes_arcs(elements):
    for element in elements:
         element['selectable']=True
    return elements

def set_list_relations(current_list,list_element):
    current_list.append(list_element)
    return current_list

def make_table(table_columns, name):
    # print(table_columns)
    if(name is None):
        return table_columns
    df=table_columns[table_columns['table_name']==name]
    print(df)
    return df
    # table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    # return table