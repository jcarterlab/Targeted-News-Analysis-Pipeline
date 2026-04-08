"""
Logging configuration module.

This module sets up application-wide logging, including console and file
handlers, formatting and log levels for the NewsMonitor pipeline.
"""

import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir, log_level):
    """
    Set up console and file logging for the application.

    Args:
        log_dir (Path):
            Directory where log files will be stored.
        log_level (int):
            Logging level, e.g. logging.INFO or logging.DEBUG.
    """
    log_file = log_dir / 'newsmonitor.log'

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    root_logger.handlers.clear()
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)