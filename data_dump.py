import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

# Convert the Dataframe into json to dump these records into MongoDB
    df.reset_index(drop=True,inplace=True)
    # json_record = df.T.to_json()
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

# Insert converted json record to MongoDB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
