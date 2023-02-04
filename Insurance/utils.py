import pandas as pd
import numpy as np
from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.config import mongo_cleint
import sys



def get_collection_as_dataframe(DATABASE_NAME:str,COLLECTION_NAME :str)->pd.DataFrame:
    try:
        logging.info(f"Reading data from database: {DATABASE_NAME} and collection: {COLLECTION_NAME}")
        df = df = pd.DataFrame(list(mongo_cleint[DATABASE_NAME][COLLECTION_NAME].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise InsuranceException(e, sys)

