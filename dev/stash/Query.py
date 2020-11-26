def query_and_store(table_name):
    query = f"""
SELECT *
FROM NEW_CLIENTS.PUBLIC.{table_name}
LIMIT 100;
    """
    #query_df = connect_read_sql(query, engine)

    #return query_df.to_json(), f"```\n{query}\n```"