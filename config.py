from dotenv import load_dotenv
import os

load_dotenv()

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
MIN_HEADLINE_LENGTH = int(os.getenv("MIN_HEADLINE_LENGTH", 25))