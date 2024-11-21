import clickhouse_connect

def connect_to_clickhouse(host, port, username, password):

    return clickhouse_connect.get_client(
        host=host,
        port=port,
        username=username,
        password=password,
        secure=True
    )

def fetch_metrics_from_clickhouse(query, host, port, username, password):

    client = connect_to_clickhouse(host, port, username, password)
    results = client.query(query).result_rows
    client.close()
    return results
