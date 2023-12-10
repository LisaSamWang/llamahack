from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

uri = os.getenv("MONGO_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def upload_convos():
    dbname = client['llama']
    convo_collection = dbname['convos']

    file_path = 'deposition_embedding.csv'
    datas = pd.read_csv(file_path)

    data_dicts = datas.to_dict(orient='records')

    convo_collection.insert_many(data_dicts)

