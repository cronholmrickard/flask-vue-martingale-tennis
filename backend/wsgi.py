"""WSGI entrypoint"""

import os
from martingale_backend.app import create_app

app = create_app(config=os.getenv("CONFIG", default="Testing"))

if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST", default="0.0.0.0"),
        port=int(os.getenv("PORT", default="5000"))
    )
