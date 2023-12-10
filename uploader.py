from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

uri = "mongodb+srv://llama:eG4bxsto6APUxapq@cluster0.dkkctf0.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

dbname = client['llama']
convo_collection = dbname['convo']


file_path = 'deposition_embedding.csv'
datas = pd.read_csv(file_path)

data_dicts = datas.to_dict(orient='records')

convo_collection.insert_many(data_dicts)



# for data in datas:

# data_dict = data.to_dict()
# # Creating a dictionary with each row as a key-value pair
# # Using a unique identifier (row number) as the key
# dict_data_new = {index: row.to_dict() for index, row in df_new.iterrows()}


