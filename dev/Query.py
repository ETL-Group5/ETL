import pandas as pd
def query_and_store(value, tables_columns_relations):

    if not value:
        return ''

    value_unique=sorted(set(value))
    print(value_unique)
    list_relations_for_query=[tables_columns_relations[i] for i in range(0, len(tables_columns_relations))
                              if (tables_columns_relations[i]['data']['id'] in value_unique)]
    # print(list_relations_for_query)

    list_tabs_in_query=[list_relations_for_query[0]['data']['source'].lower()]
    # print(list_tabs_in_query)
    query = f"""
    SELECT COUNT(*) 
    FROM {list_relations_for_query[0]['data']['source'].lower()}"""
    for i in range(0, len(list_relations_for_query)):
        if ({list_relations_for_query[i]['data']['source'].lower()} ==
                {list_relations_for_query[i]['data']['target'].lower()}):
            list_tabs_in_query.append(list_relations_for_query[i]['data']['source'].lower())
            query=query+(f"""
            JOIN {list_relations_for_query[i]['data']['target'].lower()} {list_relations_for_query[i]['data']['source'].lower()}_source ON"""
                            f"""({list_relations_for_query[i]['data']['source'].lower()}_source.{list_relations_for_query[i]['data']['col_fille'].lower()}"""
                            f"""={list_relations_for_query[i]['data']['target'].lower()}.{list_relations_for_query[i]['data']['col_mere'].lower()})""")

        else:
            if(list_relations_for_query[i]['data']['target'].lower() in list_tabs_in_query):
                key='source'
            else:
                key='target'
                list_tabs_in_query.append(list_relations_for_query[i]['data']['target'].lower())
                # print(list_tabs_in_query)
            query=query+(f"""
            JOIN {list_relations_for_query[i]['data'][key].lower()} ON"""
                            f"""({list_relations_for_query[i]['data']['source'].lower()}.{list_relations_for_query[i]['data']['col_fille'].lower()}"""
                            f"""={list_relations_for_query[i]['data']['target'].lower()}.{list_relations_for_query[i]['data']['col_mere'].lower()})""")
        """       
    # f"""
    return query

def execute_query(value,connection):
    if value is None:
        return ' '
    df = pd.read_sql_query(value, connection)
    count=df['COUNT(*)']
    return count

def test(s, q):
    return set(s).issubset(q)