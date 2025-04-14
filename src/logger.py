import logging
import os
from logging.handlers import RotatingFileHandler

class ProjectLogger:
    def __init__(self, name: str, log_file: str = "logs/app.log", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Formatter
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # File Handler
        # self.create_file_handler(log_file, formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Add handlers
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
    
    def create_file_handler(self, log_file, formatter):
        # Create logs folder
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        # File handler with rotation
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=3
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

