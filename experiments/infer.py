from transformers import AlbertTokenizer, TFAlbertForSequenceClassification
import tensorflow as tf

def infer (mode, batch_input):
    
    tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
    model = TFAlbertForSequenceClassification.from_pretrained('albert-base-v2')

    texts = ['This is a sentence', 'This is another sentence']
    inputs = tokenizer(texts, return_tensors="tf")

    outputs = model(inputs)
    logits = outputs.logits