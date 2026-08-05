"""
MCP Server Template - Configuration and Logging
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================
# Logging Configuration
# ============================================================

# Create logs directory
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

# Log format
log_format = "%(asctime)s [%(levelname)s] %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    datefmt=date_format,
)

# Create logger
logger = logging.getLogger("mcp-server")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO").upper())

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(log_format, date_format))

# File handler (rotate by size, max 10MB, keep 5 backups)
log_file = os.getenv("LOG_FILE", os.path.join(log_dir, "server.log"))
file_handler = RotatingFileHandler(
    log_file,
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5,
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format, date_format))

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# ============================================================
# Configuration
# ============================================================

# Backend API base URL
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Server port
PORT = int(os.getenv("PORT", "8001"))

# Current request API key (injected by middleware)
_current_api_key: str = ""