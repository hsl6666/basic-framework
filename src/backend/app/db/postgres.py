import psycopg2


class PostgresClient:
    def __init__(self, database_url: str, connect_timeout: int = 3) -> None:
        self._database_url = database_url
        self._connect_timeout = connect_timeout

    def ping(self) -> bool:
        try:
            with psycopg2.connect(
                self._database_url,
                connect_timeout=self._connect_timeout,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    return cursor.fetchone()[0] == 1
        except psycopg2.Error:
            return False

