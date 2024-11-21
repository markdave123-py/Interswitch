from utils.database import insert_metrics
from utils.clickhouse import fetch_metrics_from_clickhouse
from utils.config import get_config
from utils.config import get_config

from inpesct import inspect_db



def fetch_metrics(**context):

    query_path = get_config("QUERY_FILE_PATH")
    host = get_config("CLICKHOUSE_HOST")
    password = get_config("CLICKHOUSE_PASSWORD")
    port = get_config("CLICKHOUSE_PORT")
    user = get_config("CLICKHOUSE_USER")

    with open(query_path, "r") as query_file:
        query = query_file.read()

    return fetch_metrics_from_clickhouse(query, host, port, user, password)


def load_metrics_to_db(**context):
    db_path = get_config("DB_PATH")

    metrics = context["task_instance"].xcom_pull(task_ids="fetch_metrics")

    insert_metrics(db_path, metrics)

    inspect_db()