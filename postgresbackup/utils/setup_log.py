import logging
from pathlib import Path

def setup_logging(nome, level=logging.INFO):
    script_name = Path(nome).stem
    log_folder = Path("logs")
    log_file = log_folder / f"{script_name}.log"

    log_folder.mkdir(parents=True, exist_ok=True)

    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file, encoding="utf-8"),
                logging.StreamHandler(),
            ],
        )
