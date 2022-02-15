import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'])

print("Connected!")

i = random.randrange(10)
if i > 5:
    producer.send(
        topic='cars',
        value=b'Civic',
        partition=1
    )
else:
    producer.send(
        topic='cars',
        value=b'Accord',
        partition=1
    )
print("Message sent!")

producer.close()