
from dotenv import load_dotenv
import os


load_dotenv()

EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND")
EMAIL_HOST=os.environ.get("EMAIL_HOST")
EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

SECRET_KEY = os.environ.get("SECRET_KEY")

