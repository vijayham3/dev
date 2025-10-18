import logging
import sys
from logging.config import dictConfig

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s | %(filename)s:%(lineno)d"
)

def setup_logging():
    """Set up logging configuration for the FastAPI app."""
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": LOG_FORMAT,
            },
            "json": {
                "format": (
                    '{"timestamp":"%(asctime)s", '
                    '"level":"%(levelname)s", '
                    '"logger":"%(name)s", '
                    '"message":"%(message)s", '
                    '"file":"%(filename)s", '
                    '"line":%(lineno)d}'
                ),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",  # change to "json" for JSON output
                "stream": sys.stdout,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "loggers": {
            "uvicorn": {"handlers": ["console"], "level": "INFO", "propagate": False},
            "uvicorn.error": {"level": "INFO", "propagate": False},
            "uvicorn.access": {"level": "INFO", "propagate": False},
            "fastapi": {"handlers": ["console"], "level": "INFO", "propagate": False},
        },
    }

    dictConfig(logging_config)
    logging.info("✅ Logging configured successfully.")
