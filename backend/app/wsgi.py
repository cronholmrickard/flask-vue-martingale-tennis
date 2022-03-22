"""WSGI entrypoint"""

import os
from app import application


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", default="5000")))
