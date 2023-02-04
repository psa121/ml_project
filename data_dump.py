import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb+srv://aman:8755521072@cluster0.w0y5qqn.mongodb.net/?retryWrites=true&w=majority")


dATA_FILE_PATH = (r"C:\Users\Aman Pandit\Desktop\projects\ml_project\insurance.csv")


DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__ == "__main__" :
    df = pd.read_csv(dATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")


    df.reset_index(drop = True, inplace= True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME ].insert_many(json_record)


