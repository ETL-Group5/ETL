import sqlalchemy
import cx_Oracle
import pandas as pd


def queryconstr(md_elem, connectBDD):
    if (md_elem == 'table_columns'):
        query = """
                SELECT utc.TABLE_NAME,utc.COLUMN_NAME, ucc.constraint_name, utc.DATA_TYPE, utc.DATA_LENGTH,
                       utc.DATA_PRECISION, utc.NULLABLE, nvl(to_char(coalesce(DATA_PRECISION, DATA_LENGTH)),'') AS DATA
                from user_tab_columns utc 
                LEFT JOIN (select ucc.constraint_name, ucc.COLUMN_NAME, ucc.table_name from user_cons_columns ucc
                             WHERE (ucc.constraint_name NOT LIKE 'SYS_%')) ucc
                ON (utc.COLUMN_NAME=ucc.COLUMN_NAME
                     AND utc.table_name=ucc.table_name)
                ORDER BY utc.TABLE_NAME
        """
    elif (md_elem =='tables'):
        query= """
            SELECT ut.TABLE_NAME, ut.num_rows
            FROM user_tables ut
        """
    else:
        query = """
                    SELECT uc.CONSTRAINT_NAME AS Name_Constraint_pk, uc.TABLE_NAME as Tab_Mere,
                           uc_auto.CONSTRAINT_NAME AS Name_Constraint_fk, uc_auto.TABLE_NAME as Tab_Fille,
                           ucc.COLUMN_NAME AS COL_MERE, ucc_f.column_name as COL_FILLE
                    FROM user_constraints uc
                    JOIN user_cons_columns ucc ON (uc.TABLE_NAME=ucc.TABLE_NAME
                                                   AND uc.constraint_name=ucc.constraint_name)
                    JOIN user_constraints uc_auto ON(uc.constraint_name=uc_auto.r_constraint_name)
                    JOIN user_cons_columns ucc_f ON (uc_auto.TABLE_NAME=ucc_f.TABLE_NAME
                                                     AND uc_auto.constraint_name=ucc_f.constraint_name)
                    WHERE uc_auto.constraint_type='R'
        """

    return pd.read_sql_query(query, connectBDD)

def bd_connection(dbm,user,passwd, addess,port, db):
    # engine = sqlalchemy.create_engine("oracle+cx_oracle://stagbi25:Phoenix#Icar67@51.91.76.248:15440/coursdb",
    #                                   max_identifier_length=128)
    engine = sqlalchemy.create_engine(dbm +'://'+ user+ ":" +passwd+ "@"+addess + ":" +port + "/" + db, max_identifier_length=128)
    print("connecting with engine " + str(engine))
    return engine.connect()


def readbd():
    connection=bd_connection("oracle+cx_oracle","stagbi25","Phoenix#Icar67","51.91.76.248","15440", "coursdb")
    md = ['tables','table_columns_relations', 'table_columns']
    metadata={}
    for elem in md:
        metadata[elem]=queryconstr(elem, connection)
    # print(type(metadata['table_columns_relations']))

    return metadata, connection
