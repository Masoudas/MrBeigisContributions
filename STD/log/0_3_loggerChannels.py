"""

Logging instances can have multiple file handlers. Use a function like this to just add another handler with the additional output path you want. Log messages will get sent to both (or all) text logs added to the instance. You can even configure the handlers to have different logging levels so you can filter messages to different logs for critical errors, info message, etc.
"""
import logging


def add_handler(output_log_path, log: logging.Logger):
    # Set up text logger and add it to logging instance
    file_logger = logging.FileHandler(output_log_path)
    file_logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s | logger name: %(name)s | module: %(module)s | lineno: %(lineno)d | %(message)s')
    file_logger.setFormatter(formatter)
    log.addHandler(file_logger)
    return log
