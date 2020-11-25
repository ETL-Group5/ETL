#This code is a modified version of the code https://github.com/plotly/dash-cytoscape/blob/master/usage-elements.py
def successors_predecesseurs(table_columns_relations):

    print("Printing relations")
    print(table_columns_relations.columns)
    table_columns_relations_print=table_columns_relations[['tab_mere', 'name_constraint_fk', 'tab_fille']]
    print(table_columns_relations_print)


    following_nodes={}
    followers_nodes={}
    followers_arcs={}
    following_arcs={}

    nodes=set()

    cyto_nodes=[]
    cyto_arcs=[]

    for source, fk, target in zip(table_columns_relations['tab_fille'],
                              table_columns_relations['name_constraint_fk'],
                              table_columns_relations['tab_mere']):
        cyto_source = {"data": {"id": source, "label": str(source)}}
        cyto_target = {"data": {"id": target, "label": str(target)}}
        cyto_arc    = {'data': {'id': source+'-'+target, 'source': source, 'target': target, 'label': str(fk)}}

        if source not in nodes:
            nodes.add(source)
            cyto_nodes.append(cyto_source)
        if target not in nodes:
            nodes.add(target)
            cyto_nodes.append(cyto_target)

        cyto_arcs.append(cyto_arc)
# Dictionary of successors:
        if not following_nodes.get(source):
            following_nodes[source] = []
        if not following_arcs.get(source):
            following_arcs[source] = []

        following_nodes[source].append(cyto_target)
        following_arcs[source].append(cyto_arc)

# Dictionary of predecessors:
        if not followers_nodes.get(target):
            followers_nodes[target] = []
        if not followers_arcs.get(target):
            followers_arcs[target] = []

        followers_nodes[target].append(cyto_source)
        followers_arcs[target].append(cyto_arc)

    # list_dict_successors_predecessors=[following_nodes,following_arcs, followers_nodes, followers_arcs]
    # print(list_dict_successors_predecessors)
    return [following_nodes, following_arcs, followers_nodes, followers_arcs, cyto_nodes, cyto_arcs]




