"""
Axion Ingestion Service - Configuration
Loads database connection string from environment variable.
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    # Example: postgresql://postgres:postgres@10.244.0.246:5432/axiondb
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres%40123@axion-ingestion-service:8080/axiondb",
    )

settings = Settings()
