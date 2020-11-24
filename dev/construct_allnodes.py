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