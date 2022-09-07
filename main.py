from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List

# from test import formatinput 

def formatinput(df):
    print(df)
    print(type(df))

    print(type(df['col']))
    df['result'] = df['col'].map(lambda x: x.lstrip('supplier_ref'))
    return df


import pandas as pd

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    supplier_ref: str
    # supplier_ref: List[str]
class Data(BaseModel):
    # id: str
    supplier_ref: str
    # messages: str

@app.get("/")
async def root():
    return {"message": "Cronjobs for onboarder"}

@app.post("/receive_df")
async def receive_df(item:List[Item]):
# async def receive_df(item:Item):
    # print(type(item))
    # print(item)

    df = pd.DataFrame({'col':item})
    # print(df)
    # print(df.shape)

    df = formatinput(df)
    # print(df)

    return item


@app.post("/predict")
async def predict(data: Data):
#    data_dict = data.dict()
    # data_dict = pd.DataFrame(data.dict())
    df = pd.DataFrame(jsonable_encoder(data))
    print(df)
  

    return {"response": "Success"}