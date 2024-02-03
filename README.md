# Background

This library is meant to facilitate connecting to DataBricks database environments and running SQL queries. Create a connection to an Azure SQL database, submit a SQL query, and get the results back in a pandas dataframe.

# Installation

Clone this repository. In the repo directory, run `python3 -m pip install .`


# Instructions



This tutorial assumes `protected_info/creds.yaml` is a file that contains your `server_hostname`, `http_path`, and `access_token`.

Note that `access_token` should never be shared or included in a repository. Keep it in a separate place.

Try this example to run a SQL query from some file `sql_sources/my_query.sql`.

```python
from azdb.azdb import make_connection, close_connection, SQLfileToDF
import yaml

# Get the connection info from creds.yaml
with open('protected_info/creds.yaml', 'r') as stream:
    credentials = yaml.safe_load(stream)
 
 # Make the connection
conn = make_connection(server_hostname = credentials['server_hostname'],
                        http_path = credentials['http_path'],
                        access_token = credentials['access_token'])

# Now run the query and use some parameters
results_df = SQLfileToDF('sql_sources/my_query.sql', conn, params = {'max_return' : 500})

# And close the connection
close_connection(conn)
```