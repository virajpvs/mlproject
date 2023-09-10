import logging
import os
from datetime import datetime

# Create a directory for logs if it doesn't exist
logs_directory = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_directory, exist_ok=True)

# Generate the log file name with a timestamp including milliseconds
log_file_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S_%f') + ".log"

# Specify the full path to the log file
log_file_path = os.path.join(logs_directory, log_file_name)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")

    # # Example log messages
    # logging.debug("This is a debug message")
    # logging.info("This is an info message")
    # logging.warning("This is a warning message")
    # logging.error("This is an error message")
    # logging.critical("This is a critical message")


# python src/logger.py