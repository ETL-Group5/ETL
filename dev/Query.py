def query_and_store(value, tables_columns_relations):

    value_unique=sorted(set(value))
    print(value_unique)
    list_relations_for_query=[tables_columns_relations[i] for i in range(0, len(tables_columns_relations))
                              if (tables_columns_relations[i]['data']['id'] in value_unique)]
    print(list_relations_for_query)

    query = f"""
    SELECT COUNT(*) 
    FROM {list_relations_for_query[0]['data']['source'].lower()}"""
    for i in range(0, len(list_relations_for_query)):
        query=query+(f"""
        JOIN {list_relations_for_query[i]['data']['target'].lower()} ON"""
                        f"""({list_relations_for_query[i]['data']['source'].lower()}.{list_relations_for_query[i]['data']['col_fille'].lower()}"""
                        f"""={list_relations_for_query[i]['data']['target'].lower()}.{list_relations_for_query[i]['data']['col_mere'].lower()})""")
        """
    # f"""
    #     LIMIT 100;
    #         """
    return query