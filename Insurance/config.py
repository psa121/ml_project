
import pymongo
import pandas as pd
import numpy as np
import json
import os,sys

from dataclasses import dataclass

@ dataclass
class EnivermentVariable:
    mongo_db_url  = os.getenv("MONGO_DB_URL")


env_var = EnivermentVariable()
mongo_cleint = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "expenses"

print(env_var.mongo_db_url)

