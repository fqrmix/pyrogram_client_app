import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # root folder
CSV_PATH = ROOT_DIR + '/csv/employers.csv'

