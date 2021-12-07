from dotenv import load_dotenv
import os

def get_env(key: str):
    load_dotenv()
    return os.environ.get(key)