from transformers import pipeline

path = "./DistilBert"

sentiment_pipeline = pipeline(task = "sentiment-analysis", model = path)

def sentiment_analyzer(params: str)->str:
    return sentiment_pipeline(params)[0]['label']