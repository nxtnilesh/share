# import logging

# def setup_logger(log_file):
#     logging.basicConfig(
#         filename=log_file,
#         filemode='w',
#         level=logging.INFO,
#         format='%(asctime)s - %(levelname)s - %(message)s'
#     )


import logging
import sys

def setup_logger(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # File Handler
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Console Handler with UTF-8 encoding support
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add Handlers to Logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
