from databricks import sql
import pandas as pd

def make_connection(server_hostname, http_path, access_token):
    '''Create a new DataBricks SQL Server Connection'''
    connection = sql.connect(
                        server_hostname = server_hostname, 
                        http_path = http_path, 
                        access_token = access_token)
    return(connection)

def close_connection(conn):
    conn.close()
    return ('Closed connection.')

def SQLtoDF(query, conn, catalog = "source_sys", database = "raw_clarity"):
    '''Run a query using a connection conn and return
    results as a pandas dataframe'''
    cursor = conn.cursor()
    cursor.execute(f"USE CATALOG {catalog}")
    cursor.execute(f"USE DATABASE {database}")
    res = cursor.execute(query)
    df = pd.DataFrame.from_records(iter(res), columns = [desc[0] for desc in res.description])
    # Clean up
    cursor.close()
    return (df)

def SQLfileToDF(sqlFile, conn, params = {}, catalog = "source_sys", database = "raw_clarity"):
    '''Run a query from a SQL file with params using a connection conn and return
    results as a pandas dataframe. params is a dict of params to pass to the SQL query'''
    with open(sqlFile) as f:
        raw_query = f.read()
    query = raw_query.format(**params)
    cursor = conn.cursor()
    cursor.execute(f"USE CATALOG {catalog}")
    cursor.execute(f"USE DATABASE {database}")
    res = cursor.execute(query)
    df = pd.DataFrame.from_records(iter(res), columns = [desc[0] for desc in res.description])
    # Clean up
    cursor.close()
    return (df)

def RunSQLnoResults(query, conn, catalog = "source_sys", database = "raw_clarity"):
    cursor = conn.cursor()
    cursor.execute(f"USE CATALOG {catalog}")
    cursor.execute(f"USE DATABASE {database}")
    res = cursor.execute(query)
    cursor.execute(query)
    return (None)

def RunSQLfileNoResults(sqlFile, conn, params = {}, catalog = "source_sys", database = "raw_clarity"):
    '''Run a query from a SQL file with params using a connection conn and return
    no results, e.g. creating a temp view'''
    with open(sqlFile) as f:
        raw_query = f.read()
    query = raw_query.format(**params)
    cursor = conn.cursor()
    cursor.execute(f"USE CATALOG {catalog}")
    cursor.execute(f"USE DATABASE {database}")
    res = cursor.execute(query)
    # Clean up
    cursor.close()
    return (None)
