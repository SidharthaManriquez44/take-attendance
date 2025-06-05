import logging
import os

# Standard Format
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')

# Create File "logs" if not exists
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("investment")
logger.setLevel(logging.DEBUG)  # Capture all levels

# Handler for general logs (info, warning, etc.)
info_handler = logging.FileHandler('logs/app.log')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

# Handler exclusive for errors
error_handler = logging.FileHandler('logs/error.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Handler in Terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Principal Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Avoid Duplicates
if not logger.handlers:
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)
