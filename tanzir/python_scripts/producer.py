from ensurepip import bootstrap
from itertools import product
from kafka import KafkaProducer

TOPIC_NAME="greetings"
KAFKA_SERVER=["localhost:9093","localhost:9094","localhost:9095"]

producer=KafkaProducer(bootstrap_servers=KAFKA_SERVER)

print("connected")

for i in range(10):
    producer.send(
        topic="greetings",
        value=b'hello there',
        partition=i%2
    )
    print('message {} sent'.format(i))
producer.close()

