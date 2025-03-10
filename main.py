from postgresbackup.postgres_backup import PostgresBackup
from postgresbackup.utils.database_env import scsdp_env

def main():
    pg_backup = PostgresBackup(scsdp_env['dev'])

if __name__ == "__main__":
    main()