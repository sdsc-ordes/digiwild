import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(os.getcwd(), ".env")
load_dotenv(dotenv_path)
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
USER_MAIL = os.environ.get("USER_MAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")