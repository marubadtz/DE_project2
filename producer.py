from kafka import KafkaProducer
import csv
from time import sleep
from json import dumps, loads

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:29092', 
    value_serializer=lambda K:dumps(K).encode('utf-8')
    )


topic = 'car7'
file_name = 'data/car7.csv'
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    for messages in reader:
        producer.send(topic, messages)
        producer.flush()
        sleep(1)


