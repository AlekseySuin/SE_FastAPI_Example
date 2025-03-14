from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"FastApi service started!"}


@app.get("/{text}")
def get_params(text: str):
    return classifier(text)


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)

@app.post("/text-length/")
def text_length(item: Item):
    return {"text_length": len(item.text)}
