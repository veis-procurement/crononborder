import pandas as pd
import requests

df = pd.read_csv('RSCOMPfile (chank 522).csv')

df1 = df.head()



def formatinput(df):
    df['result'] = df['col'].map(lambda x: x.lstrip('supplier_ref'))
    return df

# payload={"df_in":df.to_json()}
# requests.post("http://0.0.0.0:8000/receive_df", json=df.to_json(orient='records'))


# payload={"df_in":df.to_json()}
# requests.post("http://0.0.0.0:8000/receive_df", data=payload)


# # df_json = df1.to_json(orient='records', date_format='iso') 


df_json = df1.to_json(orient='records', date_format='iso') 
requests.post('http://0.0.0.0:8000/receive_df', data=df_json)



# requests.post('http://0.0.0.0:8000/predict', json=df1.to_json(orient='records', date_format='iso'))
# # df_json = df1.to_dict(orient='list') 

# requests.post('http://localhost:8000/api/v0/add-new', data=df_json) 
# requests.post('http://0.0.0.0:8000/receive_df', data=df_json)