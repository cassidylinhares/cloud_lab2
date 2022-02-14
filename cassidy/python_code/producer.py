from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9093', 'localhost:9094', 'localhost:9095'])

print("Connected!")

for i in range(10):
    part = i % 3
    if i % 2 == 0:
        producer.send(
            topic='topic',
            value=b'bla bla',
            partition=part
        )
    else:
        producer.send(
            topic='topic2',
            key=i.to_bytes(2, 'big'),
            value=b'Big blobbb',
            partition=part
        )
    print("Message sent!")

producer.close()
