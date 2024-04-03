from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from model_app import sentiment_analyzer

class Sentiment_Params(BaseModel):
    sentence : str

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello World'}

@app.post('/sentiment')
async def sentiment(msg_params: Sentiment_Params):
    params_json = jsonable_encoder(msg_params)
    return {'message' : sentiment_analyzer(params_json['sentence'])}
