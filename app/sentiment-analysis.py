import json
import configparser
from confluent_kafka import Consumer, KafkaError
from transformers import pipeline, BertTokenizer, BertForSequenceClassification, BertModel

# Lire le fichier de configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Configuration du consommateur Kafka
BROKER_ADDRESS = config['Kafka']['bootstrap_servers']
TOPIC_NAME = config['Kafka']['topic_name']
GROUP_ID = config['Kafka']['group_id']

conf = {
    'bootstrap.servers': BROKER_ADDRESS,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest',
    'value.deserializer': lambda x: json.loads(x.decode('utf-8'))
}

consumer = Consumer(conf)
consumer.subscribe([TOPIC_NAME])

# Charger le tokenizer et le modèle pour l'analyse de sentiment
tokenizer_sentiment = BertTokenizer.from_pretrained(config['BERT']['sentiment_model'])
model_sentiment = BertForSequenceClassification.from_pretrained(config['BERT']['sentiment_model'])
sentiment_pipeline = pipeline("sentiment-analysis", model=model_sentiment, tokenizer=tokenizer_sentiment)

# Charger le tokenizer et le modèle pour le résumé
tokenizer_summary = BertTokenizer.from_pretrained(config['BERT']['summary_model'])
model_summary = BertModel.from_pretrained(config['BERT']['summary_model'])
summarization_pipeline = pipeline("summarization", model=model_summary, tokenizer=tokenizer_summary)

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of topic')
        else:
            print(f"Error while consuming message: {msg.error()}")
    else:
        content = msg.value()['content']  # Assurez-vous que le message contient une clé 'content' avec le texte à analyser

        # Analyse de sentiment
        sentiment = sentiment_pipeline(content)[0]
        print("Sentiment:", sentiment)

        # Résumé
        summary = summarization_pipeline(content, max_length=150, min_length=30, do_sample=False)[0]
        print("Résumé:", summary['summary_text'])

consumer.close()
