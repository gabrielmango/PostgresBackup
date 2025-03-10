import subprocess
import os
from urllib.parse import urlparse
from postgresbackup.utils.setup_log import setup_logging, logging

setup_logging(__file__)

class PostgresBackup:
    def __init__(self, conn_str: str):
        """Inicializa a classe a partir da string de conexão."""
        conn_str = conn_str.replace('postgresql+psycopg2', 'postgresql')

        if not isinstance(conn_str, str):
            logging.error("A string de conexão (conn_str) deve ser uma string válida.")
        
        self.conn_str = conn_str
        parsed = urlparse(conn_str)
        self.user = parsed.username
        self.password = parsed.password
        self.host = parsed.hostname
        self.port = parsed.port if parsed.port else 5432
        self.dbname = parsed.path.lstrip('/')

