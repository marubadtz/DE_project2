from kafka import KafkaConsumer
from json import dumps, loads

consumer = KafkaConsumer(
    bootstrap_servers='127.0.0.1:29092',
    #value_deserializer = lambda K:dumps(K).decode('utf-8')
    )

topic = 'car7'

consumer.subscribe(topics=topic)
for message in consumer:
  print (message.value)