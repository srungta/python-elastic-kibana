import pandas as pd

TRAIN_DATA_PATH = './data/train.csv'
TEST_DATA_PATH = './data/test.csv'

from datetime import datetime
from elasticsearch import Elasticsearch

CHUNK_SIZE = 100

index_name_train = "loan_train"
doc_type_train = "av-lp_train"

index_name_test = "loan_test"
doc_type_test = "av-lp_test"


def index_data(data_path, chunksize, index_name, doc_type):
    f = open(data_path)
    csvfile = pd.read_csv(f, iterator=True, chunksize=chunksize)
    es = Elasticsearch(timeout=30)
    try:
        es.indices.delete(index=index_name)
    except:
        pass
    es.indices.create(index=index_name)
    for i, df in enumerate(csvfile):
        records = df.where(pd.notnull(df), None).T.to_dict()
        list_records = [records[it] for it in records]
        try:
            es.bulk(index_name, doc_type, list_records)
        except:
            print("Error. Skipping chunk")
            pass


index_data(TRAIN_DATA_PATH, CHUNK_SIZE, index_name_train, doc_type_train)
index_data(TEST_DATA_PATH, CHUNK_SIZE, index_name_test, doc_type_test)
