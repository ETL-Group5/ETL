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
    return df[['column_name', 'constraint_name', 'data_type',
           'data_length', 'data_precision', 'nullable', 'data']]


    # infos_tables = '|________ Les colonnes de la table :' + '{:^18}'.format(Data['id']) + ' ________|' + '\n'
    # for index, col in enumerate(df_tab[['column_name', 'data_type']][df_tab['table_name'] == Data['id']].values):
    #     infos_tables += '| La colonne n° {} : {:<18} | Type Data : {}'.format(index + 1, col[0], col[1]) + '\n'
    # return infos_tables
    # figure = {
    #     'layout': go.Layout(title='graph',
    #                         paper_bgcolor='rgba(0,0,0,0)',
    #                         plot_bgcolor='rgba(0,0,0,0)',
    #                         font=dict(color='blue', size=10))

    return df
    # table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    # return table