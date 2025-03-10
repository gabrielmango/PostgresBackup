import os

from dotenv import load_dotenv

load_dotenv()

REQUIRED_VARS = {
    'SCSDP': ['SCSDP_DEV', 'SCSDP_TST', 'SCSDP_HML', 'SCSDP_PREPROD', 'SCSDP_PROD']
    }


def validate_env_vars(required_vars):
    missing_vars = [var for var in required_vars if os.getenv(var) is None]
    if missing_vars:
        raise EnvironmentError(
            f'As seguintes variáveis de ambiente estão ausentes: {", ".join(missing_vars)}'
        )


for category, vars_list in REQUIRED_VARS.items():
    validate_env_vars(vars_list)


scsdp_env = {
    'dev': os.getenv('SCSDP_DEV'),
    'tst': os.getenv('SCSDP_TST'),
    'hml': os.getenv('SCSDP_HML'),
    'preprod': os.getenv('SCSDP_PREPROD'),
    'prod': os.getenv('SCSDP_PROD'),
}
