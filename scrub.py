import pandas as pd

TRAIN_DATA_PATH = './data/train.csv'
TEST_DATA_PATH = './data/test.csv'

train = pd.read_csv(TRAIN_DATA_PATH)
print(train.shape)
test = pd.read_csv(TEST_DATA_PATH)
print(test.shape)

print("TRAIN DATA : ")
print(train.head())

print("TEST DATA : ")
print(test.head())