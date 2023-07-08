import os

from dotenv import load_dotenv

load_dotenv()

APITOKEN = str(os.getenv("APITOKEN"))

YOOTOKEN = str(os.getenv("YOOTOKEN"))
RECEIVER = str(os.getenv("RECEIVER"))
TARGETS = str(os.getenv("TARGETS"))

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
PGHOST = str(os.getenv("PGHOST"))
PGPORT = str(os.getenv("PGPORT"))
PGDB = str(os.getenv("PGDB"))
