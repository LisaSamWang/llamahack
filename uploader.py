from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

uri = "uri" # Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

dbname = client['llama']
convo_collection = dbname['convos']


file_path = 'deposition_embedding.csv'
datas = pd.read_csv(file_path)

data_dicts = datas.to_dict(orient='records')

convo_collection.insert_many(data_dicts)

